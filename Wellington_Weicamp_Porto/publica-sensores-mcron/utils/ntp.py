import ntptime

HOST = "1.europe.pool.ntp.org"

def synchronize_time():
    ntptime.host = HOST
    ntptime.settime()    