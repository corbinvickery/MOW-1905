#Used to bump and then turn
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setup(4,GPIO.OUT)              #Sonalert "sonar" signal
GPIO.setup(17,GPIO.OUT)             #Driving motor Right signal
GPIO.setup(27,GPIO.OUT)             #Driving motor Left  signal
GPIO.setup(22,GPIO.OUT)             #Reverse trigger Right
GPIO.setup(23,GPIO.OUT)             #Reverse trigger Left
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)              #Bump sense Right
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)              #Bump sense Left

sonar = GPIO.PWM(4,500)            #GPIO17 PWM, with 500Hz for smoother sound
#driver = GPIO.PWM(17,100)           #GPIO17 PWM, with 100Hz frequency used for Right motor
#drivel = GPIO.PWM(27,100)           #GPIO27 PWM, with 100Hz frequency used for Left  motor

#pwmr = 0
#pwml = 0
sonar.start(0)                     #start sonar pwm
#driver.start(pwmr)                 #start pwm right     
#drivel.start(pwml)                 #start pwm left
lowt = 90                          # sonar low tone


def forward():                                   #speed up to top speed
    print ("Speed up forward")
    GPIO.output(22,GPIO.HIGH)                     #reverse triggers off
    GPIO.output(23,GPIO.HIGH)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    return
    

def stop():                                     #slow to a stop
    print ("Stop")
    GPIO.output(22,GPIO.LOW)                               #reverse triggers off
    GPIO.output(23,GPIO.LOW)
    GPIO.output(27,GPIO.LOW)
    GPIO.output(17,GPIO.LOW)
    return
                            #sleep for 1 millisecond
      
def reverse():                                   #Reverse top speed
    print ("Reverse")
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    return                      

def rightpivot():
    print ("Turn right")
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)                                  #reverse triggers off
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    return
              
   
def leftpivot():
    print ("Turn left")
    GPIO.output(23,GPIO.LOW)
    GPIO.output(22,GPIO.HIGH)  
    GPIO.output(27,GPIO.HIGH)
    GPIO.output(17,GPIO.HIGH)
    return
    
      
def bumpright(channel):   
    print ("Right Bumper")
    stop()
    reverse()
    time.sleep(1)
    stop()
    time.sleep(1)
    leftpivot()
    time.sleep(1)
    stop()
    time.sleep(1)
    print ("Done")
    forward()
    return
 

def bumpleft(channel):
    print ("Left Bumper")
    stop()
    reverse()
    time.sleep(1)
    stop()
    time.sleep(1)
    rightpivot()
    time.sleep(1)
    stop()
    time.sleep(1)
    print ("Done")
    forward()
    return

GPIO.add_event_detect(24, GPIO.FALLING, callback=bumpright, bouncetime=3000)
GPIO.add_event_detect(25, GPIO.FALLING, callback=bumpleft, bouncetime=3000)

sonar.ChangeDutyCycle(lowt)
time.sleep(.6)
sonar.ChangeDutyCycle(0)
print ("Sonar test successful")

for x in range (1):
    forward()
    time.sleep(1)
    stop()
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

while True:
       #forward()
       time.sleep(1)