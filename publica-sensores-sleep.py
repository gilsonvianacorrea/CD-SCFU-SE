from umqtt.simple import MQTTClient
from machine import Pin
from time import sleep
import ujson
import time
import ntptime
import dht

def connect_scfu():
    import network
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('Lula_La', 'Marmelada')
        while not sta_if.isconnected():
            pass # wait till connection
    print('network config:', sta_if.ifconfig())
    
connect_scfu()

ntptime.host = "1.europe.pool.ntp.org"
ntptime.settime()

# mqtt client setup
CLIENT_NAME = 'pi-iv-a'
BROKER_ADDR = 'broker.hivemq.com'
mqttc = MQTTClient(CLIENT_NAME, BROKER_ADDR, keepalive=60)
mqttc.connect()

BTN_TOPIC = CLIENT_NAME.encode() + b'/dados'
print(BTN_TOPIC)
### -----------------------

i=1
while True:
    print(i)
    i=i+1
    
    sensor = dht.DHT22(Pin(23))
    try:
        sensor.measure()
        temp = sensor.temperature()
        print("Temperatura lida é ", temp)
        #Umid = sensor.humidity()
        #print("Umidade lida é ", Umid)
        
    except OSError as err:
        print("Falha na leitura dos dados")
          
    ano=time.localtime()[0]
    mes=time.localtime()[1]
    dia=time.localtime()[2]
    hora=time.localtime()[3]
    hfl=[21,22,23,0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
    horalocal=hfl[hora]
    minuto=time.localtime()[4]
    segundo=time.localtime()[5]
    datahora=str(ano)+"-"+str(mes)+"-"+str(dia)+" "+str(horalocal)+ ":"+str(minuto)+ ":"+str(segundo)
    print(datahora)
  
    dict = {}
    dict["Valor"] = temp
    dict["DataHora"] = datahora
    dict["Descricao"] = "Temperatura"
    dict["Origem"] = "Tiago"
    print(dict)
    
    publicacao = ujson.dumps(dict)
    print(publicacao)
    
    mqttc.publish( BTN_TOPIC, publicacao.encode() )

    sleep(120)
