import upip
import network

def connect_wifi():
    sta_if = network.WLAN(network.STA_IF)
    if not sta_if.isconnected():
        sta_if.active(True)
        sta_if.connect('SSID', 'Password')
        while not sta_if.isconnected():
            pass # wait till connection
    print('network config:', sta_if.ifconfig())

connect_wifi()

upip.install("micropython-mcron")
