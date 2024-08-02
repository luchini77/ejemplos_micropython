from machine import Pin
from time import sleep
import _thread

rojo1 = Pin(23,Pin.OUT)
amarillo1 = Pin(22,Pin.OUT)
verde1 = Pin(21,Pin.OUT)

rojo2 = Pin(19,Pin.OUT)
amarillo2 = Pin(18,Pin.OUT)
verde2 = Pin(5,Pin.OUT)


def main():

    def semaforo1():
        while True:
            rojo1.on()
            sleep(5)
            rojo1.off()
            verde1.on()
            sleep(3)
            verde1.off()
            amarillo1.on()
            sleep(2)
            amarillo1.off()
            
    _thread.start_new_thread(semaforo1,())
        
        
    while True:
        verde2.on()
        sleep(3)
        verde2.off()
        amarillo2.on()
        sleep(2)
        amarillo2.off()
        rojo2.on()
        sleep(5)
        rojo2.off()


if __name__ == '__main__':
    main()