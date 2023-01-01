import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)

#defined for motor-1
DIR = 20
STEP = 21
CW = 1
CCW = 0
SPR = 200
EN_pin = 16 # enable pin (LOW to enable)

#GPIO pin define of motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(DIR, CCW)
GPIO.setup(EN_pin,GPIO.OUT) # set enable pin as output


#Step count adn delay tine define
step_count = SPR
delay = .0015
#defined for motor-2
DIR1 = 19
STEP1 = 26
CW1 = 1
CCW1 = 0
SPR1 = 200
EN_pin1 = 13 # enable pin (LOW to enable)

#GPIO pin define of motor
GPIO.setmode(GPIO.BCM)
GPIO.setup(DIR1, GPIO.OUT)
GPIO.setup(STEP1, GPIO.OUT)
GPIO.output(DIR1, CCW1)
GPIO.setup(EN_pin1,GPIO.OUT) # set enable pin as output

#Step count adn delay tine define
step_count1 = SPR1
delay = .001


def stepper2():
   for x in range(step_count):
      GPIO.output(EN_pin,GPIO.LOW) # pull enable to low to enable motor
      GPIO.output(STEP, GPIO.HIGH)
      sleep(delay)
      GPIO.output(STEP, GPIO.LOW)
      sleep(delay)
def stepper1():
   for x in range(step_count1):
      GPIO.setup(EN_pin1,GPIO.OUT) # set enable pin as output
      sleep(delay)
      GPIO.output(STEP1, GPIO.HIGH)
      sleep(delay)
      GPIO.output(STEP1, GPIO.LOW)
      sleep(delay)
      
#test change