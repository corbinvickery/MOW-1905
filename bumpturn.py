#Used to bump and then turn
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

pr = GPIO.PWM(17,500)          #GPIO17 as PWM output, with 100Hz frequency
pl = GPIO.PWM(27,500)          #GPIO27 as PWM output, with 100Hz frequency
pwmr = 40.0
pwml = 40.0
pr.start(pwmr)
pl.start(pwml)

#t = 3
#while t>0:                               #execute loop
   # t -= 1




def forward():
    print ("Speed up forward")
    global pwmr
    global pwml
    for x in range (599):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr += .1
       pwml += .1
       pr.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second


def fstop():
    print ("Change from forword to stop")
    global pwmr
    global pwml
    for x in range (599):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr -= .1
       pwml += .1
       pr.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second

def rstop():
    print ("Change from reverse to stop")
    global pwmr
    global pwml
    for x in range (399):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr += .1
       pwml += .1
       pr.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second

def reverse():
    print ("Speed up Reverse")
    global pwmr
    global pwml
    for x in range (399):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
      
       pwmr -= .1
       pwml += .1
       pr.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second

def turn():
    print ("Turn right then stop")
    global pwmr
    global pwml
    for x in range (399):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
      
       pwmr -= .1
       pwml += .1
       pr.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwml)
       time.sleep(0.01)
       for x in range (399):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr += .1
       pwml -= .1
       pr.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwml)
       time.sleep(0.01)

for x in range (3):
    forward()
    time.sleep(1)
    fstop()
    time.sleep(1)
    reverse()
    time.sleep(1)
    rstop()
    time.sleep(1)
    turn()
    time.sleep(1)
