from machine import Pin
import time

def main():

    led = Pin(2,Pin.OUT)

    #MULTIPINES
    # led1 = Pin(2,Pin.OUT)
    # led2 = Pin(13,Pin.OUT)
    # led3 = Pin(12,Pin.OUT)
    # led4 = Pin(14,Pin.OUT)
    
    # leds = (led1,led2,led3,led4)

    while True:
        
        led.on()
        time.sleep(0.5)
        led.off()
        time.sleep(0.5)

        #MULTIPINES
        # for led_prende in leds:
        #     led_prende.on()
        #     time.sleep(0.5)
            
        # for led_apaga in leds:
        #     led_apaga.off()
        #     time.sleep(0.5)
        
        
if __name__ == "__main__":
    main()