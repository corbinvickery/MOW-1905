#Used to sonar alert "beeper"

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)  

sonar = GPIO.PWM(4,500)            #GPIO17 PWM, with 100Hz

lowt = 80			#low freq for low sonar alert tone
medt = 90			#medium freq for mid level tone
hight = 100			#high freq for high pitch tone

sonar.start(0)

# testing low pitch timing

for x in range (3):
  
  sonar.ChangeDutyCycle(lowt)
  time.sleep(.5)
  sonar.ChangeDutyCycle(0)
  time.sleep(.2)

  sonar.ChangeDutyCycle(lowt)
  time.sleep(.5)
  sonar.ChangeDutyCycle(0)
  time.sleep(.2)

  sonar.ChangeDutyCycle(lowt)
  time.sleep(1)
  sonar.ChangeDutyCycle(0)
  time.sleep(.2)












