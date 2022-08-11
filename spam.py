import telebot
import config
import asuBD
bot = telebot.TeleBot(config.token)
def spamCommutators(id):
    result = []
    result = asuBD.sql(f"select * from Comutators where id = {id};")
    if len(result)!=0:
        userAsu = asuBD.sql("select * from userAsu;")
        for a in userAsu:
            if (result[0]['status'] == 'False'):
                bot.send_message(a['id'], f"❌Нет пинга с коммутатором!❌ \n {result[0]['ip']} - {result[0]['name']}")
            else:
                bot.send_message(a['id'], f"✅Работа коммутатора восстановлена!✅ \n {result[0]['ip']} - {result[0]['name']}")


def spamServers(id):
    result = []
    result = asuBD.sql(f"select * from Servers where id = {id};")
    if len(result)!=0:
        userAsu = asuBD.sql("select * from userAsu;")
        for a in userAsu:
            if (result[0]['status'] == 'False'):
                bot.send_message(a['id'], f"❌Нет пинга с сервером!❌ \n {result[0]['ip']} - {result[0]['name']}")
            else:
                bot.send_message(a['id'], f"✅Работа сервера восстановлена!✅ \n {result[0]['ip']} - {result[0]['name']}")

def spamCamers(id):
    result = []
    result = asuBD.sql(f"select * from Camers where id = {id};")
    if len(result)!=0:
        userAsu = asuBD.sql("select * from userAsu;")
        for a in userAsu:
            if (result[0]['status'] == 'False'):
                bot.send_message(a['id'], f"❌Нет пинга с камерой!❌ \n {result[0]['ip']} - {result[0]['name']}")
            else:
                bot.send_message(a['id'], f"✅Работа камеры восстановлена!✅ \n {result[0]['ip']} - {result[0]['name']}")
