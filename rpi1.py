import requests
import time as t
import json
from sense_hat import SenseHat
import random

testinfos ={
        #'time':u'1111-11-11 11:11:11',
        'temperature':u'11',
        'pressure':u'111.111',
        'humidity':u'l1'    
    }
infos={}

user={'login':'raspberry001','password':'000000'}
gps={'lat':48.390834,'long':-4.485556}
vitessevent={'vitessevent':0.001}

def insert_data_sensehat():
    sense = SenseHat()
    #ISOTIMEFORMAT='%Y-%m-%d %X'
    #time = t.strftime(ISOTIMEFORMAT)
    temperature = round(sense.get_temperature(),3)
    humidity = round(sense.get_humidity(),3)
    pressure = round(sense.get_pressure(),3)

    sense.set_imu_config(True,True,True)
    north = round(sense.get_compass(),3)
    #print("North: %s" %north)
    
    
    sensedata={'temp':temperature,'pression':pressure,'humidite':humidity
               ,'compass':north}
    sensedata.update(user)
##    gps={'lat':round(random.uniform(48.350,48.450),3),
##         'long':round(random.uniform(-4.499,-4.401),3)}
    sensedata.update(gps)
    sensedata.update(vitessevent)
    #infos.append(sensedata)
    #infos=sensedata
    #print(time)
    #print(sensedata)
    #print(infos)
    return sensedata

def send_data():
    while True:
        #headers={'Connection': 'close'}
        infos=insert_data_sensehat()
        headers = {'content-type':'application/json'}
        r = requests.post("http://172.20.12.168:5000/infos", data=json.dumps(infos),
                      headers=headers)
        #print r.headers
        print r.text
        t.sleep(10)
        
def send_data_json():
    while True:
        #headers={'Connection': 'close'}
        infos=insert_data_sensehat()
        test={'rasb_sec':infos}
        headers = {'content-type':'application/json'}

        http_proxy  = "http://192.168.1.17:8080"
        https_proxy = "https://192.168.1.17::8080"
        ftp_proxy   = "ftp://192.168.1.17::8080"

        proxyDict = { 
              "http"  : http_proxy, 
              "https" : https_proxy, 
              "ftp"   : ftp_proxy
            }

##        r = requests.post("http://172.20.12.168:5000/infos", data=json.dumps(test),
##                      headers=headers)

##        r = requests.post("http://192.168.10.114:5000/infos", data=json.dumps(test),
##                      headers=headers)
        
        r=requests.post("http://95.85.46.87/rasb_secs/sign_in", data=json.dumps(test),
                      headers=headers, proxies=proxyDict)
        #print r.headers
        ##print r.text
        print test
        t.sleep(10)
        
##########test################
##def send_data():
##    while True:
##        #headers={'Connection': 'close'}
##        r = requests.post("http://172.20.12.168:5000/infos", data=testinfos)
##                      #headers=headers,timeout=1)
##        print r.text
##        t.sleep(10)
        
if __name__=='__main__':
    #insert_data_sensehat()
##    send_data()
    send_data_json()   
