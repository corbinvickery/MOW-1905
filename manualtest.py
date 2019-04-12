#used for testing Manual mode for mower using keyboard input

#Used to bump and then turn

import time
import RPi.GPIO as GPIO
import curses

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)              #Sonalert "stone" signal
GPIO.setup(17,GPIO.OUT)             #Driving motor Right signal
GPIO.setup(27,GPIO.OUT)             #Driving motor Left  signal
GPIO.setup(22,GPIO.OUT)             #Reverse trigger Right
GPIO.setup(23,GPIO.OUT)             #Reverse trigger Left
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)              #Bump sense Right
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP)              #Bump sense Left

sonar = GPIO.PWM(4,500)            #GPIO17 PWM, with 100Hz
driver = GPIO.PWM(17,100)           #GPIO17 PWM, with 100Hz frequency used for Right motor
drivel = GPIO.PWM(27,100)           #GPIO27 PWM, with 100Hz frequency used for Left  motor

pwmr = 0
pwml = 0
sonar.start(0)
driver.start(pwmr)
drivel.start(pwml)
lowt = 90





def forward():
    print ("Forward")
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    global pwmr
    global pwml
    for x in range (99):                          #
       if pwmr < 100: 
              pwmr += 1
              pwml += 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.001)                           #sleep for 10m second


def fstop():
    print ("Stop forward")
    global pwmr
    global pwml
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr > 0:
              pwmr -= 1
              pwml -= 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.001)                           #sleep for 10m second

def rstop():
    print ("Stop reverse")
    global pwmr
    global pwml
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr > 0:
              pwmr -= 1
              pwml -= 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.001)                           #sleep for 10m second
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
      
def reverse():
    print ("Reverse")
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
    global pwmr
    global pwml
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr < 100:
              pwmr += 1
              pwml += 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.001)                           #sleep for 10m second

def rightpivot():
    print ("Turn right")
    global pwmr
    global pwml
    GPIO.output(22,GPIO.HIGH)
    pwmr = 0
    pwml = 0
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr < 100:
              pwmr += 1
              pwml += 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
def rightstop():
    print ("Stop turning right")
    global pwmr
    global pwml
    GPIO.output(22,GPIO.HIGH)
    pwmr = 99
    pwml = 99
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr > 0:
              pwmr -= 1
              pwml -= 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
      
    GPIO.output(22,GPIO.LOW)
   
def leftpivot():
    print ("Turn left")
    global pwmr
    global pwml
    GPIO.output(23,GPIO.HIGH)
    pwmr = 0
    pwml = 0
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr < 100:
              pwmr += 1
              pwml += 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
def leftstop():
    print ("Stop turning left")
    global pwmr
    global pwml
    GPIO.output(23,GPIO.HIGH)
    pwmr = 99
    pwml = 99
    for x in range (99):                          #execute loop for 60000 times, x being incremented from 0 to 60000.
       if pwmr > 0:
              pwmr -= 1
              pwml -= 1
              driver.ChangeDutyCycle(pwmr)               #change duty cycle for varying the PWM.
              drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
      
    GPIO.output(23,GPIO.LOW)
 

sonar.ChangeDutyCycle(lowt)
time.sleep(.6)
sonar.ChangeDutyCycle(0)
print ("Sonar test successful")

for x in range (1):
    forward()
    time.sleep(1)
    fstop()
    time.sleep(1)
    reverse()
    time.sleep(1)
    rstop()
    time.sleep(1)
    rightpivot()
    rightstop()
    time.sleep(1)
    leftpivot()
    leftstop()
    print ("done")
    time.sleep(1)
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
      
screen = curses.initscr()
curses.noecho()
curses.cbreak()
screen.keypad(True)

try:
       while True:
              char = screengetch()
              if char == ord('q'):
                     break
              elif char == curses.KEY_UP:
                     forward()
              elif char == curses.KEY_DOWN:
                     reverse()
              elif char == curses.KEY_RIGHT:
                     rightpivot()
              elif char == curses.KEY_LEFT:
                     leftpivot()
              elif char == curses.KEY_SP:
                     global pwmr
                     global pwml
                     pwmr = 0
                     pwml = 0
finally:
       curses.nobreak(); screen.keypad(0); curses.echo()
       curses.endwin()

