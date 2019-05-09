#Used to bump and then turn as automation program
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(4,GPIO.OUT)              #Sonalert "sonar" signal
GPIO.setup(17,GPIO.OUT)             #Driving motor Right signal
GPIO.setup(27,GPIO.OUT)             #Driving motor Left  signal
GPIO.setup(22,GPIO.OUT)             #Reverse trigger Right
GPIO.setup(23,GPIO.OUT)             #Reverse trigger Left
GPIO.setup(24,GPIO.IN, pull_up_down=GPIO.PUD_UP)              #Bump sense Right
GPIO.setup(25,GPIO.IN, pull_up_down=GPIO.PUD_UP)              #Bump sense Left
GPIO.setup(5,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)              #Right Boundary
GPIO.setup(6,GPIO.IN, pull_up_down=GPIO.PUD_DOWN)              #left Boundary

sonar = GPIO.PWM(4,500)            #GPIO 4 PWM, with 500Hz
driver = GPIO.PWM(17,100)           #GPIO 17 PWM, with 100Hz frequency used for Right motor
drivel = GPIO.PWM(27,100)           #GPIO 27 PWM, with 100Hz frequency used for Left  motor

pwmr = 0                            #pwm signal right
pwml = 0                            #pwm signal right
sonar.start(0)
driver.start(pwmr)
drivel.start(pwml)
lowt = 90                           #number used for changing sonar tone, this one is slightly lower pitch than normal




def forward():                                        #function sets relays both to forward
    print ("Speed up forward")                        #print statements for debugging while using the terminal window
    GPIO.output(22,GPIO.HIGH)                         #reverse relays reverse polarity to motors
    GPIO.output(23,GPIO.HIGH)                         #setting HIGH is forward LOW is reverse
    global pwmr
    global pwml
    for x in range (99):                          
       if pwmr <= 100 and pwml <= 100:                #slowly increases forward speed
         pwmr += 1
         pwml += 1
       driver.ChangeDutyCycle(pwmr)               
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.001)                          


def fstop():                                          #slows down PWM until stopped
    print ("Slow down forward")
    global pwmr
    global pwml
    for x in range (99):                          
      if pwmr > 0 and pwml > 0:
         pwmr -= 1
         pwml -= 1
         driver.ChangeDutyCycle(pwmr)               
         drivel.ChangeDutyCycle(pwml)
      time.sleep(0.001)                           

def rstop():
    print ("Slow down reverse")                    #slows down then sets relays from reverse to forward when done
    global pwmr
    global pwml
    for x in range (99):                          
       if pwmr > 0 and pwml > 0:
         pwmr -= 1
         pwml -= 1
       driver.ChangeDutyCycle(pwmr)               
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.001)                           
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
      
def reverse():
    print ("Speed up Reverse")                  #sets relays to reverse then speeds up
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.LOW)
    global pwmr
    global pwml
    for x in range (99):                          
      if pwmr <= 100 and pwml <= 100:
         pwmr += 1
         pwml += 1
      driver.ChangeDutyCycle(pwmr)               
      drivel.ChangeDutyCycle(pwml)
      time.sleep(0.001)                          

def rightturn():                               #sets right relay reverse, left relay forward to turn
    print ("Turn right then stop")
    global pwmr
    global pwml
    GPIO.output(22,GPIO.LOW)
    GPIO.output(23,GPIO.HIGH)
    pwmr = 0
    pwml = 0
    for x in range (99):                         
      
       pwmr += 1
       pwml += 1
       driver.ChangeDutyCycle(pwmr)               
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
    for x in range (99):                          
       
       pwmr -= 1
       pwml -= 1
       driver.ChangeDutyCycle(pwmr)               
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)

    GPIO.output(22,GPIO.HIGH)  
    GPIO.output(23,GPIO.HIGH)
   
def leftturn():
    print ("Turn left then stop")           #sets left relay reverse, right relay forward to turn
    global pwmr
    global pwml
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.LOW)
    pwmr = 0
    pwml = 0
    for x in range (99):                         
      
       pwmr += 1
       pwml += 1
       driver.ChangeDutyCycle(pwmr)              
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
    for x in range (99):                          
       
       pwmr -= 1
       pwml -= 1
       driver.ChangeDutyCycle(pwmr)              
       drivel.ChangeDutyCycle(pwml)
       time.sleep(0.01)
      
    GPIO.output(22,GPIO.HIGH)
    GPIO.output(23,GPIO.HIGH)
 

sonar.ChangeDutyCycle(lowt)               #intitial sonar test tone
time.sleep(.6)
sonar.ChangeDutyCycle(0)
print ("Sonar test successful")

for x in range (1):                       #startup procedure to test functionality
    forward()
    time.sleep(1)
    fstop()
    time.sleep(1)
    reverse()
    time.sleep(1)
    rstop()
    time.sleep(1)
    rightturn()
    time.sleep(1)
    leftturn()
    print ("done")                        #ready tone
    time.sleep(1)
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
while True:                            #MAIN LOOP
   input_state = GPIO.input(24)
   if input_state == False:               #checks right bumper switch
    print ("Right Bumper")
    fstop()
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
    reverse()
    time.sleep(1)
    rstop()
    leftturn()
    forward()

   input_state = GPIO.input(25)
   if input_state == False:             #checks left bumper switch
    print ("Left Bumper")
    fstop()
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
    reverse()
    time.sleep(1)
    rstop()
    rightturn()
    forward()

   input_state = GPIO.input(5)
   if input_state == True:          #checks right boundary sensor
    print ("Right Boundary")
    fstop()
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
    reverse()
    time.sleep(1)
    rstop()
    leftturn()
    forward()

   input_state = GPIO.input(6)
   if input_state == True:          #checks left boundary sensor
    print ("Left Boundary")
    fstop()
    sonar.ChangeDutyCycle(lowt)
    time.sleep(.1)
    sonar.ChangeDutyCycle(0)
    time.sleep(.1)
    reverse()
    time.sleep(1)
    rstop()
    rightturn()
    forward()
    