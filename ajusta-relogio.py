import network
import ntptime
import time

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('EXEHDA_2G', '!luz@azul#')
        while not sta_if.isconnected():
            pass # wait till connection
    print('network config:', sta_if.ifconfig())

connect_wifi()

ntptime.host = "1.europe.pool.ntp.org"

try:
  print("Horário antes da sincronizacao：%s" %str(time.localtime()))

  ntptime.settime()
  print("Horário após sincronizacao：%s" %str(time.localtime()))
  
except:
  print("Erro ao sincronizar o relogio")
