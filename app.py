from flask import Flask, render_template,jsonify,request
from flask import make_response
#from sense_hat import SenseHat
import threading
import time as t


app = Flask(__name__)

data=[
    {
        'time':u'2017-08-08 15:30:00',
        'temperature':u'100',
        'pressure':u'101.325',
        'humidity':u'1',
        'latitude':u'32',
        'longitude':u'121',
        'source':u'test00'
    },
    {'time':u'2017-08-08 15:30:00',
        'temperature':u'100',
        'pressure':u'101.325',
        'humidity':u'1',
        'latitude':u'32',
        'longitude':u'121',
        'source':u'test01'
    }
    ]
data1={'testStr':'ddddddddddd'}

#def insert_data():
    #sense = SenseHat()
    #ISOTIMEFORMAT='%Y-%m-%d %X'
    #temperature = round(sense.get_temperature(),3)
    #humidity = round(sense.get_humidity(),3)
    #pressure = round(sense.get_pressure(),3)
    #time = t.strftime(ISOTIMEFORMAT)
    #sensedata={'time':time,'temperature':temperature,
    #    'pressure':pressure,'humidity':humidity }
    #data.append(sensedata)
    #print(time)
    #print(sensedata)

    #count=threading.Timer(10.0,insert_data)
    #if(event.action == "")

@app.route('/data',methods=['GET'])
def get_data():
    return jsonify({'data':data})
    #return data

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/infos',methods=['POST'])
def infos():
##    print request.headers
##    print (request.form)
##    #print (request.form['time'])
##    print (request.form.get('temperature'))
##    print (request.form.getlist('name'))
##    print (request.form.get('nickname', default='little apple'))
####--------------------json-------------------##
##    #time = request.json['time']
    time = t.strftime('%Y-%m-%d %X')
    
    temperature = request.json['temp']
    humidity = request.json['humidite']
    pressure = request.json['pression']
    latitude = request.json['lat']
    longitude = request.json['long']
    compass = request.json['compass']
    source = request.json['login']
    sensedata={'time':time,'temperature':temperature,
        'pressure':pressure,'humidity':humidity ,
        'latitude':latitude,'longitude':longitude,
        'compass':compass,'source':source}
    data.append(sensedata)
    return 'server got data'

##    request1=request.json['rasb_sec']
##    time = t.strftime('%Y-%m-%d %X')
##    
##    temperature =request.form.get('temp')
##    humidity = request.form.get('humidite')
##    pressure = request.form.get('pression')
##    latitude = request.form.get('lat')
##    longitude = request.form.get('long')
##    compass =request.form.get('compass')
##    source =request.form.get('login')
##    sensedata={'time':time,'temperature':temperature,
##        'pressure':pressure,'humidity':humidity ,
##        'latitude':latitude,'longitude':longitude,
##        'compass':compass,'source':source}
##    data.append(sensedata)
##    return 'server got data'
##--------------------TEXT-------------------##
##    #time = request.form.get('time')
##    time = t.strftime('%Y-%m-%d %X')
##    temperature = request.form.get('temperature')
##    humidity = request.form.get('humidity')
##    pressure = request.form.get('pressure')
##    sensedata={'time':time,'temperature':temperature,
##        'pressure':pressure,'humidity':humidity }
##    data.append(sensedata)
##    return 'server got data'
##-------------------------------------------##
#@app.route('/about')
#def about():
#    return render_template('about.html')

#@app.route('/login')
#def login():
# return render_template('login.html')

#@app.route('/page')
#def hello():
#   return render_template('page.html')

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not found'}),404)

if __name__=='__main__':
    #count = threading.Timer(10.0,insert_data)
    #count.start()
    #insert_data()
    app.run(debug=True, host='172.20.12.168',port=5000)

