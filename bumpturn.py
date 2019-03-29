#Used to bump and then turn
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)              #Sonalert "stone" signal
GPIO.setup(17,GPIO.OUT)             #Driving motor Right signal
GPIO.setup(27,GPIO.OUT)             #Driving motor Left  signal
GPIO.setup(22,GPIO.OUT)             #Reverse trigger Right
GPIO.setup(23,GPIO.OUT)             #Reverse trigger Left
GPIO.setup(24,GPIO.IN)              #Bump sense Right
GPIO.setup(25,GPIO.IN)              #Bump sense Left

sonar = GPIO.PWM(4,100)            #GPIO17 PWM, with 100Hz
driver = GPIO.PWM(17,100)           #GPIO17 PWM, with 100Hz frequency used for Right motor
drivel = GPIO.PWM(27,100)           #GPIO27 PWM, with 100Hz frequency used for Left  motor

pwmr = 35.0
pwml = 35.0
driver.start(pwmr)
drivel.start(pwml)
lowt = 90

#t = 3
#while t>0:                               #execute loop
   # t -= 1




def forward():
    print ("Speed up forward")
    global pwmr
    global pwml
    for x in range (150):                          #
       
       pwmr += .1
       pwml += .1
       driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second


def fstop():
    print ("Slow down forward")
    global pwmr
    global pwml
    for x in range (150):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr -= .1
       pwml -= .1
       driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second

def rstop():
    print ("Slow down reverse")
    global pwmr
    global pwml
    for x in range (100):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr += .1
       pwml += .1
       driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second

def reverse():
    print ("Speed up Reverse")
    global pwmr
    global pwml
    for x in range (100):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
      
       pwmr -= .1
       pwml -= .1
       driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)                           #sleep for 10m second

def turn():
    print ("Turn right then stop")
    global pwmr
    global pwml
    for x in range (100):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
      
       pwmr -= .1
       pwml += .1
       driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
    for x in range (100):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       
       pwmr += .1
       pwml -= .1
       driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
      
sonar.ChangeDutyCycle(lowt)
time.sleep(.3)
sonar.ChangeDutyCycle(0)
time.sleep(.2)
sonar.ChangeDutyCycle(lowt)
time.sleep(.3)
sonar.ChangeDutyCycle(0)
time.sleep(.2)

for x in range (1):
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
   # while True:
   # input_state = GPIO.input(18)
    #if input_state == False:
     #  print('Button Pressed')
      #  time.sleep(0.2)
