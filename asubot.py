import telebot
import config
import asuBD
from random import randint
from array import *
from datetime import datetime, timedelta, date
from telebot import types

global textZayavka, Location, Mobily, vaschnost


bot = telebot.TeleBot(config.token)


markupASU = types.InlineKeyboardMarkup(row_width=2)
itemA1 = types.InlineKeyboardButton('Заявки', callback_data="bt1")
itemA2 = types.InlineKeyboardButton('Сотрудники', callback_data="bt2")
itemA3 = types.InlineKeyboardButton('Дополнительные функции', callback_data="bt3")
markupASU.add(itemA1, itemA2, itemA3)


markup3 = types.InlineKeyboardMarkup(row_width=2)
itemM31 = types.InlineKeyboardButton('Добавить', callback_data="bt2_1")
itemM32 = types.InlineKeyboardButton('Назад', callback_data="back")
markup3.add(itemM31, itemM32)

markup2 = types.InlineKeyboardMarkup(row_width=2)
itemM21 = types.InlineKeyboardButton('Создать заявку', callback_data="bt1_1")
itemM22 = types.InlineKeyboardButton('Заявки', callback_data="bt1_2")
itemM23 = types.InlineKeyboardButton('Выполненные', callback_data="bt1_3")
itemM24 = types.InlineKeyboardButton('Назад', callback_data="back")
markup2.add(itemM21, itemM22, itemM23, itemM24)

markup8 = types.InlineKeyboardMarkup(row_width=2)
itemM81 = types.InlineKeyboardButton('Выполнена', callback_data="bt8_1")
itemM82 = types.InlineKeyboardButton('Удалить', callback_data="bt8_2")
itemM83 = types.InlineKeyboardButton('Назад', callback_data="back")
markup8.add(itemM81, itemM82, itemM83)

markup4 = types.InlineKeyboardMarkup(row_width=2)
itemM41 = types.InlineKeyboardButton('❌ коммутаторы', callback_data="bt3_1")
itemM42 = types.InlineKeyboardButton('❌ сервера', callback_data="bt3_2")
itemM43 = types.InlineKeyboardButton('Устройства', callback_data="bt4")
itemM44 = types.InlineKeyboardButton('Сообщение', callback_data="bt3_3")
itemM45 = types.InlineKeyboardButton('Логи', callback_data="bt3_4")
itemM46 = types.InlineKeyboardButton('Назад', callback_data="back")
markup4.add(itemM41, itemM42, itemM43, itemM44, itemM45, itemM46)

markup5 = types.InlineKeyboardMarkup(row_width=2)
itemM51 = types.InlineKeyboardButton('коммутаторы', callback_data="bt5")
itemM52 = types.InlineKeyboardButton('сервера', callback_data="bt6")
itemM53 = types.InlineKeyboardButton('Назад', callback_data="bt3")
markup5.add(itemM51, itemM52, itemM53)

markup6 = types.InlineKeyboardMarkup(row_width=2)
itemM61 = types.InlineKeyboardButton('Удалить', callback_data="bt5_1")
itemM62 = types.InlineKeyboardButton('Добавить', callback_data="bt5_2")
itemM63 = types.InlineKeyboardButton('Назад', callback_data="bt4")
markup6.add(itemM61, itemM62, itemM63)

markup7 = types.InlineKeyboardMarkup(row_width=2)
itemM71 = types.InlineKeyboardButton('Удалить', callback_data="bt6_1")
itemM72 = types.InlineKeyboardButton('Добавить', callback_data="bt6_2")
itemM73 = types.InlineKeyboardButton('Назад', callback_data="bt4")
markup7.add(itemM71, itemM72, itemM73)

def start(message):
    result = []
    result = asuBD.sql(f"select * from userAsu where id = {str(message.from_user.id)}")
    if len(result) != 0:
        bot.send_message(message.chat.id, "Меню!-------------------->", reply_markup = markupASU)
    else:
        bot.send_message(message.chat.id, "Вы не авторизованы!")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    start(message)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "bt1":
            bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.id, text = "Меню - заявки", reply_markup=markup2)
        elif call.data == "back":
            bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.id, text = "Меню!-------------------->", reply_markup=markupASU)
        elif call.data == "bt2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            sotr(call.message)
        elif call.data == "bt3":
            bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.id, text = "Меню - Дополнительные функции", reply_markup=markup4)
        elif call.data == "bt4":
            bot.edit_message_text(chat_id = call.message.chat.id, message_id=call.message.id, text = "Меню - Дополнительные функции - Устройства", reply_markup=markup5)
        elif call.data == "bt5":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            commutatorsInsert(call.message)
        elif call.data == "bt6":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            serversInsert(call.message)
        elif call.data == "bt1_1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            zayavka(call.message)
        elif call.data == "bt1_2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            vseHelpMy(call.message)
        elif call.data == "bt1_3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            vseHelpMyEZNedel(call.message)
        elif call.data == "bt2_1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            pinCode(call.message)
        elif call.data == "bt3_1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            commutators(call.message)
        elif call.data == "bt3_2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            servers(call.message)
        elif call.data == "bt3_3":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            spamMessage(call.message)
        elif call.data == "bt3_4":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            log(call.message)
        elif call.data == "bt5_1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            commutatorsD(call.message)
        elif call.data == "bt5_2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            commutatorsIN(call.message)
        elif call.data == "bt6_1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            serversD(call.message)
        elif call.data == "bt6_2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            serversIN(call.message)
        elif call.data == "bt8_1":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            zayavkaIn(call.message)
        elif call.data == "bt8_2":
            bot.delete_message(call.message.chat.id, call.message.message_id)
            zayavkaD(call.message)

def realAsu(id):
    print(id)
    result = []
    result = asuBD.sql(f"select * from userAsu where id = {id};")
    print(result)
    if len(result)!=0:
        return True
    else:
        return False

@bot.message_handler(content_types=['text'])
def send_welcome(message):
    result = []
    result = asuBD.sql(f"select * from userAsu where id = {str(message.from_user.id)};")
    if len(result) != 0:
        if (message.text == "Удалить сотрудника"):
            sotrMarkup(message)
        else:
            bot.send_message(message.chat.id, "Меню!-------------------->", reply_markup = markupASU)
    else:
        if (message.text == "Хочу в АСУ"):
            registerASU(message)
        else:
            bot.send_message(message.chat.id, "ВЫ не авторизованы!")

def sotr(message):
    result = []
    result = asuBD.sql(f"select * from userAsu;")
    if len(result)!=0:
        sotr = ''
        for a in result:
            sotr = sotr + f"{a['id']} - {a['name']} \n"
        bot.send_message(message.chat.id, f"{sotr}", reply_markup = markup3)
    else: bot.send_message(message.chat.id, f"Сотрудников как бы нет, но как вы тогда это получили???", reply_markup = markupASU)

def log(message):
    if realAsu(message.chat.id):
        result = []
        dateT = date.today() - timedelta(days=3)
        result = asuBD.sql(f"select LogBase.id, action, textV, dateV, name from LogBase, userAsu where userAsu.id=humen and dateV>='{dateT}';")
        if len(result)!=0:
            log = ''
            for a in result:
                log = log + f"{a['action']} - {a['dateV']}- {a['name']} \n- \n"
            bot.send_message(message.chat.id, f"{log}", reply_markup = markup4)
        else: bot.send_message(message.chat.id, f"Логов нет", reply_markup = markup4)

def commutators(message):
    if realAsu(message.chat.id):
        result = []
        result = asuBD.sql(f"select * from Comutators where status = 'False';")
        if len(result)!=0:
            com = ''
            for a in result:
                com = com + f"❌ {a['id']} - {a['ip']} - {a['name']} \n"
            bot.send_message(message.chat.id, f"{com}", reply_markup = markup4)
        else: bot.send_message(message.chat.id, f"Все коммутаторы работают!", reply_markup = markup4)

def servers(message):
    if realAsu(message.chat.id):
        result = []
        result = asuBD.sql(f"select * from Servers where status = 'False';")
        if len(result)!=0:
            ser = ''
            for a in result:
                ser = ser + f"❌ {a['id']} - {a['ip']} - {a['name']} \n"
            bot.send_message(message.chat.id, f"{ser}", reply_markup = markup4)
        else: bot.send_message(message.chat.id, f"Все серверы работают!", reply_markup = markup4)

def sotrMarkup(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Введите id сотрудника! Или напишите 'stop'.")
        bot.register_next_step_handler(message, sotrDelete)

def sotrDelete(message):
    if message.text.lower() != 'stop':
        asuBD.sql(f"delete from userAsu where id = {message.text};")
        bot.send_message(message.chat.id, "Сотрудник удален!", reply_markup = markupASU)
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Сотрудник удален', '{message.text}', '{date}','{message.from_user.id}')")
        sotr(message)
    else: sotr(message)

def pinCode(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Введите пинкод", reply_markup = types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, pinCodeDelete)

def spamMessage(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Внимание это сообщение получать все сотрудники АСУ!")
        bot.send_message(message.chat.id, "Введите ваше сообщение! Или напишите 'stop'.")
        bot.register_next_step_handler(message, spamText)

def spamText(message):
    if message.text.lower() != 'stop':
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Рассылка', '{message.text}', '{date}','{message.from_user.id}')")
        userAsu = asuBD.sql("select * from userAsu;")
        for a in userAsu:
            bot.send_message(a['id'], message.text)
        start(message)
    else: start(message)

def registerASU(message):
    result = []
    result = asuBD.sql(f"select * from PinCode;")
    if len(result)!=0:
        bot.send_message(message.chat.id, "Введите пинкод")
        bot.register_next_step_handler(message, pinCodeRegi)
    else: bot.send_message(message.chat.id, "Пинкод не задан!")

def pinCodeRegi(message):
    text = message.text
    result = []
    result = asuBD.sql(f"select * from PinCode where pincode = '{text}';")
    if len(result)!=0:
        bot.send_message(message.chat.id, "Как мне вас называть?")
        bot.register_next_step_handler(message, pinCodeRegi_1)
    else:
        bot.send_message(message.chat.id, "Пинкод не правильный!")
        registerASU(message)

def pinCodeRegi_1(message):
    text = message.text
    result = asuBD.sql(f"insert into userAsu values({message.from_user.id}, '{text}', 'асу сти');")
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    asuBD.sql(f"insert into LogBase values (Null, 'Добавлен новый сотрудник', '{message.text}', '{date}','{message.from_user.id}')")
    bot.send_message(message.chat.id, f"Идущие на смерть приветствуют тебя!", reply_markup = markupASU)

def pinCodeDelete(message):
    if realAsu(message.chat.id):
        asuBD.sql(f"insert into PinCode values ( '{ message.text}' );")
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Добавлен новый пинкод', '{message.text}', '{date}','{message.from_user.id}')")
        bot.send_message(message.chat.id, "Напишите любой текст для удаления пинкода!")
        bot.register_next_step_handler(message, pinCodeDelete2)

def pinCodeDelete2(message):
    asuBD.sql(f"truncate table PinCode")
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    asuBD.sql(f"insert into LogBase values (Null, 'Пинкоды удалены', '', '{date}','{message.from_user.id}')")
    bot.send_message(message.chat.id, "Пинкод удален", reply_markup = markupASU)


def vseHelpMyEZNedel(message):
    result = []
    date = datetime.today() - timedelta(days=2)
    result = asuBD.sql(f"select * from HelpMyEZ where dateV>='{date}'")
    if len(result)!=0:
        ez = ''
        for a in result:
            ez = ez + f"Текст заявки: \n{a['help']} \nВыполнил: \n- {a['v']} \n\n\n"
        bot.send_message(message.chat.id, f"Выполнено за сегодня: \n\n{ez}", reply_markup = markup2)
    else: bot.send_message(message.chat.id, f"Еще ничего не обработали!", reply_markup = markup2)

def vseHelpMy(message):
    if realAsu(message.chat.id):
        result = []
        result = asuBD.sql(f"select * from HelpMy;")
        if len(result) != 0:
            for a in result:
                textVse = f"Номер - {a['id']} от {a['dateV']} \n{a['help']} \nЛокация - {a['location']} \nТелефон для связи - {a['number']}"
                bot.send_message(message.chat.id, f"{textVse}")
            bot.send_message(message.chat.id, "Это все текущие заявки!", reply_markup = markup8)
        else:
            bot.send_message(message.chat.id, "Заявок нет!", reply_markup = markup2)

def zayavkaIn(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Укажите номер!", reply_markup = types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, obrabotkaEZ)

def zayavkaD(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Укажите номер!", reply_markup = types.ReplyKeyboardRemove())
        bot.register_next_step_handler(message, obrabotkaDEL)

def obrabotkaEZ(message):
    result = asuBD.sql(f"select * from HelpMy where id = {message.text}")
    sotr = asuBD.sql(f"select name from userAsu where id = {message.from_user.id}")
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    bot.send_message(result[0]['userID'], f"Заявка номер {message.text} выполнена \n{result[0]['help']} \nЛокация - {result[0]['location']} \nОтветственный - {sotr[0]['name']}!")
    asuBD.sql(f"insert into HelpMyEZ values ({result[0]['id']}, {result[0]['userID']}, '{date}', '{result[0]['help']}', '{result[0]['location']}', '{result[0]['number']}', '{sotr[0]['name']}');")
    asuBD.sql(f"delete from HelpMy where id = {message.text}")
    asuBD.sql(f"insert into LogBase values (Null, 'Заявка выполнена', '{message.text}', '{date}','{message.from_user.id}')")
    vseHelpMy(message)

def obrabotkaDEL(message):
    asuBD.sql(f"delete from HelpMy where id = {message.text}")
    date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
    asuBD.sql(f"insert into LogBase values (Null, 'Заявка удалена', '{message.text}', '{date}','{message.from_user.id}')")
    vseHelpMy(message)

def zayavka(message):
    if realAsu(message.chat.id):
        if message.text.lower() != 'стоп':
            bot.send_message(message.chat.id, "Кратко опишите вашу проблему! \nИли же напишите стоп.")
            bot.register_next_step_handler(message, korpus)
        else: start(message)

def korpus(message):
    textZayavka = message.text
    if message.text.lower() != 'стоп':
        bot.send_message(message.chat.id, "Укажите место проблемы! \nКорпус, кабинет, компьютер! \nИли же напишите стоп.")
        bot.register_next_step_handler(message, numbers, textZayavka)
    else: start(message)

def numbers(message, textZayavka):
    Location = message.text
    if message.text.lower() != 'стоп':
        bot.send_message(message.chat.id, "Укажите внутренний или мобильный номер телефона! \nИли же напишите стоп.")
        bot.register_next_step_handler(message, Srochnost, textZayavka, Location)
    else: start(message)

def Srochnost(message, textZayavka, Location):
    if message.text.lower() != 'стоп':
        Mobily = message.text
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into HelpMy (id, userID, dateV, help, location, number) values (Null, {str(message.from_user.id)}, '{ str(date) }', '{textZayavka}', '{Location}', '{Mobily}');")
        idMax = asuBD.sql(f"select max(id) from HelpMy;")
        bot.send_message(message.chat.id, f"Заявка {idMax[0]['max(id)']} отправлена! Мы оповестим о выполнении.")
        spam()
        start(message)
    else: start(message)

def spam():
    result = []
    result = asuBD.sql("select * from HelpMy;")
    if len(result)!=0:
        userAsu = asuBD.sql("select * from userAsu;")
        maxID = asuBD.sql("select max(id) from HelpMy;")
        HelpMy = asuBD.sql(f"select * from HelpMy where id={maxID[0]['max(id)']};")
        for a in userAsu:
            bot.send_message(a['id'], f"❗️ Новая заявка! ❗️ \nНомер - {HelpMy[0]['id']} от{HelpMy[0]['dateV']} \n{HelpMy[0]['help']} \nЛокация - {HelpMy[0]['location']}\nТелефон для связи - {HelpMy[0]['number']}")

def commutatorsInsert(message):
    if realAsu(message.chat.id):
        result = []
        result = asuBD.sql(f"select * from Comutators;")
        if len(result) != 0:
            com = ''
            for a in result:
                com = com + f"{a['id']} - {a['ip']} - {a['name']} - {a['status']} \n"
                if com.count('\n') > 20:
                    bot.send_message(message.chat.id, f"{com}")
                    com = ""
            if com != "":
                bot.send_message(message.chat.id, f"{com}", reply_markup = markup6)
            else:
                bot.send_message(message.chat.id, f"Меню", reply_markup = markup6)
        else:
            bot.send_message(message.chat.id, "Коммутаторов нет!", reply_markup = markup5)

def commutatorsIN(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Введите IP коммутатора! Или напишите 'stop'.")
        bot.register_next_step_handler(message, commutatorsInsert1)

def commutatorsD(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Введите номер коммутатора! Или напишите 'stop'.")
        bot.register_next_step_handler(message, commutatorsDelete)

def commutatorsInsert1(message):
    ipText = message.text
    if message.text.lower() != 'stop':
        bot.send_message(message.chat.id, "Кратко опишите коммутатор! Или напишите 'stop'.")
        bot.register_next_step_handler(message, commutatorsInsert2, ipText)
    else: commutatorsInsert(message)

def commutatorsInsert2(message, ipText):
    if message.text.lower() != 'stop':
        asuBD.sql(f"insert into Comutators values(Null, '{ipText}', ' {message.text} ', 'False');")
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Добавлен коммутатор', '{ipText}', '{date}','{message.from_user.id}')")
        bot.send_message(message.chat.id, "Добавлен коммутатор")
        commutatorsInsert(message)
    else: commutatorsInsert(message)

def commutatorsDelete(message):
    if message.text.lower() != 'stop':
        asuBD.sql(f"delete from Comutators where id = {message.text};")
        bot.send_message(message.chat.id, "Коммутатор удален!")
        commutatorsInsert(message)
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Удален коммутатор', '{message.text}', '{date}','{message.from_user.id}')")
    else: commutatorsInsert(message)

def serversInsert(message):
    if realAsu(message.chat.id):
        result = []
        result = asuBD.sql(f"select * from Servers;")
        if len(result) != 0:
            ser = ''
            for a in result:
                ser = ser + f"{a['id']} - {a['ip']} - {a['name']} - {a['status']} \n"
            bot.send_message(message.chat.id, f"{ser}", reply_markup = markup7)
        else:
            bot.send_message(message.chat.id, "Серверов нет!", reply_markup = markup5)

def serversIN(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Введите IP сервера! Или напишите 'stop'.")
        bot.register_next_step_handler(message, serversInsert1)

def serversD(message):
    if realAsu(message.chat.id):
        bot.send_message(message.chat.id, "Введите номер сервера! Или напишите 'stop'.")
        bot.register_next_step_handler(message, serversDelete)

def serversInsert1(message):
    ipText = message.text
    if message.text.lower() != 'stop':
        bot.send_message(message.chat.id, "Кратко опишите сервер!")
        bot.register_next_step_handler(message, serversInsert2, ipText)
    else: serversInsert(message)

def serversInsert2(message, ipText):
    nameText = message.text
    if message.text.lower() != 'stop':
        asuBD.sql(f"insert into Servers values(Null, '{ipText}', ' {nameText} ', 'False');")
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Добавлен сервер', '{ipText}', '{date}','{message.from_user.id}')")
        bot.send_message(message.chat.id, "Добавлен сервер!")
        serversInsert(message)
    else: serversInsert(message)

def serversDelete(message):
    if message.text.lower() != 'stop':
        asuBD.sql(f"delete from Servers where id = {message.text};")
        bot.send_message(message.chat.id, "Сервер удален!")
        date = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
        asuBD.sql(f"insert into LogBase values (Null, 'Удален сервер', '{message.text}', '{date}','{message.from_user.id}')")
        serversInsert(message)
    else: serversInsert(message)


try:
    bot.polling(none_stop=True)
except Exception as errors:
    print(f"Внимание ОШИБКА 😳")
    print(errors)
    bot.polling(none_stop=True)
