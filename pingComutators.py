import asuBD
import spam
import time
from ping3 import ping, verbose_ping

def pings():
    result = []
    result = asuBD.sql('select id, ip, status from Comutators;')
    if len(result)!=0:
        for a in result:
            ip = str(a['ip'])
            check = ping(ip)
            if (type(check) == float):
                if a['status']=='False':
                    asuBD.sql(f"update Comutators set status = 'True' where id = {a['id']}")
                    spam.spamCommutators(a['id'])
            elif a['status']=='True':
                i = 0
                cheking = True
                while i<5:
                    ip = str(a['ip'])
                    check = ping(ip)
                    if (type(check) == float):
                        cheking = False
                        break
                    i+=1
                if cheking:
                    asuBD.sql(f"update Comutators set status = 'False' where id = {a['id']}")
                    spam.spamCommutators(a['id'])
    pingall()

def pingall():
    time.sleep(300)
    pings()

pings()
