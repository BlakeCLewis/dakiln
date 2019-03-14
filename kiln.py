
import RPi.GPIO as GPIO
from Adafruit_GPIO import SPI
from Adafruit_MAX31856 import MAX31856


class kiln():
    """
       3 rings, 2 elements each
       3 relays
       current sensors
       kilnsitter
       thermocouple
       display
       logger


       Firing
         ramp
         hold
       Idle
         test, current draw, kilnsitter, thermocouple
         monitor
    """


class kilnsitter(pin=27):
   def __init__():
       self.ksio = pin
       GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
   # armed == False if kilnsitter is open
   def armed():
       state = GPIO.input(self.ksio)
       return state

class thermocouple(pins):
    def __int__(MAX31856): #inherits ?
        self.CS[] = pins
        self.Tx = MAX31856(hardware_spi=SPI.SpiDev(0,0))
        for cs in self.CS:
            GPIO.setup(cs, GPIO.OUT)
            GPIO.output(cs, GPIO.LOW)
        self.temp[] = self.read()
        self.internal[]
        #hardware spi w/ software chip select

    def readtc():
        cnt = 0
        for cs in self.CS:
            GPIO.output(cs, GPIO.HIGH) #is HIGH select?
            self.temp[cnt] = self.Tx.read_temp_c()
            GPIO.output(cs, GPIO.LOW)
            print('T'+str(i)+': {0:0.3F}*C'.format(self.temp[cnt]))
            ++cnt 
        return  

    def readint():
        cnt = 0
        for cs in self.CS:
            GPIO.output(cs, GPIO.HIGH) #is HIGH select?
            internal[] = self.Tx.read_internal_temp_c()
            GPIO.output(cs, GPIO.LOW)
            print('Ti'+str(i)+': {0:0.3F}*C'.format(internal[cnt]))
            ++cnt 
        return
       #need shed temp reading
