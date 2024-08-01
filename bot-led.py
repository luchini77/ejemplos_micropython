from machine import Pin
import time, network, utelegram

# telegram API key
telegram_api_key = "tu-token"

# I2C Pin Definitions
led = Pin(2, Pin.OUT)

# Wifi Credentials and Wifi Conenctions
ssid = 'tu-red'
pswd = 'pass de tu red'

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(ssid, pswd)

print("Conectado al Wifi.", end='')

while not wlan.isconnected() and wlan.status() >= 0:
    print('.', end='')
    time.sleep(0.5)

print('')
print(wlan.ifconfig())
print("WiFi Conectado")

# Telegram default callback
def get_message(message):
    bot.send(message['message']['chat']['id'], 'Bienvenido \nAl Sistema.\nIntroduzca /menu.')

# send Menu text as ping reply
def reply_ping(message):
    print(message)
    bot.send(message['message']['chat']['id'], 'Encender = /led on\nApagar = /led off')
    
# change led status with given parameters in message text
def led_cb(message):
    msg = message['message']['text']
    msg_sp = msg.split(' ')
    print(msg_sp)
    if len(msg_sp) != 2:
        bot.send(message['message']['chat']['id'], "Encender = /led on\nApagar = /led off")
        return
    
    if msg_sp[0] == '/led':
        if msg_sp[1] == 'on':
            led.on()
            bot.send(message['message']['chat']['id'], "LED PRENDIDO")
        elif msg_sp[1] == 'off':
            led.off()
            bot.send(message['message']['chat']['id'], "LED APAGADO")
        else:
            bot.send(message['message']['chat']['id'], "No existe ese comando!!!")
          
    
# start telegram bot 
bot = utelegram.ubot(telegram_api_key)
bot.register('/menu', reply_ping)       # ping message callback
bot.register('/led', led_cb)            # led message callback
bot.set_default_handler(get_message)    # default message callback

print('BOT ESCUCHANDO')

bot.listen()
