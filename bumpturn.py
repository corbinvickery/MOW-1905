#Used to bump and then turn
import time
import RPi.GPIO as gpio

GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)

pr = GPIO.PWM(17,500)          #GPIO17 as PWM output, with 100Hz frequency
pl = GPIO.PWM(27,500)          #GPIO27 as PWM output, with 100Hz frequency
pwm = 40.0
pr.start(pwm)
pl.start(pwm)

#t = 3
#while t>0:                               #execute loop
   # t -= 1


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


def forward(pw):
print "Speed up forward"
for x in range (60000):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm += .001
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       #time.sleep(0.01)                           #sleep for 10u second


def fstop(pw):
print "Change from forword to stop"
for x in range (60000):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm -= .001
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       #time.sleep(0.01)                           #sleep for 10u second

def rstop(pw):
print "Change from reverse to stop"
for x in range (40000):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm += .001
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       #time.sleep(0.01)                           #sleep for 10u second

def reverse(pw):
print "Speed up Reverse"
for x in range (40000):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       pwm -= .001
       pr.ChangeDutyCycle(pwm)               #change duty cycle for varying the PWM.
       pl.ChangeDutyCycle(pwm)
       #time.sleep(0.01)                           #sleep for 10u second

def turn(pw):
print "Turn right then stop"

