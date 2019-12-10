
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
    def __int__(MAX31856):
        self.T0 = MAX31856(hardware_spi=SPI.SpiDev(0,0))
        self.T1 = MAX31856(hardware_spi=SPI.SpiDev(0,1))
        self.temp[] = readit()
        self.internal[] = readint()

    def readtc():
        for cs in self.CS:
            self.temp[] = self.T0.read_temp_c(),self.T1.read_temp_c()
            print('T'+str(i)+': {0:0.3F}*C'.format(self.temp[cnt]))
        return  

    def readint():
        for cs in self.CS:
            internal[] = self.Tx.read_internal_temp_c()
            print('Ti'+str(i)+': {0:0.3F}*C'.format(internal[cnt]))
        return


