#Used to bump and then turn
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

pr = GPIO.PWM(17,500)          #GPIO17 as PWM output, with 100Hz frequency
pl = GPIO.PWM(27,500)          #GPIO27 as PWM output, with 100Hz frequency
pwm = 50.0
pr.start(pwm)
pl.start(pwm)

#t = 3
#while t>0:                               #execute loop
   # t -= 1




def forward(pwm):
    print ("Speed up forward")
    for x in range (499):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm += .1
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       time.sleep(0.01)                           #sleep for 10m second


def fstop(pwm):
    print ("Change from forword to stop")
    for x in range (499):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm -= .1
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       time.sleep(0.01)                           #sleep for 10m second

def rstop(pwm):
    print ("Change from reverse to stop")
    for x in range (499):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm += .1
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       time.sleep(0.01)                           #sleep for 10m second

def reverse(pwm):
    print ("Speed up Reverse")
    for x in range (499):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm -= .1
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       time.sleep(0.01)                           #sleep for 10m second

def turn(pwm):
    print ("Turn right then stop")

forward(pwm)
time.sleep(1)
fstop(pwm)
time.sleep(1)
reverse(pwm)
time.sleep(1)
rstop(pwm)
time.sleep(1)
turn(pwm)
time.sleep(1)
