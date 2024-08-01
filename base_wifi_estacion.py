import network
import time

RED = 'nombre de tu red'
PASSWORD = 'contraseña de la red'

def conectar_wifi(RED,PASSWORD):
    global mi_red
    mi_red = network.WLAN(network.STA_IF)
    
    if not mi_red.isconnected():  		# Si no esta conectado
        mi_red.active(True)				# activa la interface
        mi_red.connect(RED,PASSWORD)	# Intenta conectar con la red
        print('Conectando a la red ',RED + '.....')
        timeout = time.time()
        
        while not mi_red.isconnected():	# Mientras no se conecte...
            if(time.ticks_diff(time.time(), timeout) > 10):
                return False
    return True

#---------------[ Respuesta de conexion WIFI ]---------------

if conectar_wifi(RED,PASSWORD):
    print('Conexion exitosa!')
    print('Datos de la red (IP/netmask/gw/DNS):',mi_red.ifconfig())
    print('Conexión WiFi establecida!')
    
else:
    print('Imposible conectar')
    mi_red.active(False)