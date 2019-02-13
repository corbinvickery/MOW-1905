#!/usr/bin/python

import RPi.GPIO as GPIO		 #calling header file which helps us use GPIOs of PI

import time                            #calling time to provide delays in program

GPIO.setwarnings(False)           #do not show any warnings

GPIO.setmode (GPIO.BCM)         #we are programming the GPIO by BCM pin numbers. (PIN35 as GPIO17)

GPIO.setup(17,GPIO.OUT)           # initialize GPIO19 as an output.

p = GPIO.PWM(17,500)          #GPIO17 as PWM output, with 100Hz frequency
pwm = 50
p.start(pwm)                              #generate PWM signal with 0 duty cycle

for x in range (49):

    print (pwm)
    pwm += 1 
    p.ChangeDutyCycle(pwm)
    time.sleep(.5)
for x in range (49):

    print (pwm)
    pwm -= 1 
    p.ChangeDutyCycle(pwm)
    time.sleep(.5)



# t = 3
# while t>0:                               #execute loop
#     t -= 1
#     for x in range (4999):                          #execute loop for 50 times, x being incremented from 0 to 49.
#        pwm += .01
#        p.ChangeDutyCycle(pwm)               #change duty cycle for varying the brightness of LED.
#        time.sleep(0.001)                           #sleep for 10m second
#     print (pwm)
#     time.sleep(.5)
#     for x in range (4999):                         #execute loop for 50 times, x being incremented from 0 to 49.
#         pwm -= .01
#         p.ChangeDutyCycle(pwm)        #change duty cycle for changing the brightness of LED.
#         time.sleep(0.001)                          #sleep for 10m second
#     print (pwm)
#     time.sleep(.5)

# print (pwm)

# time.sleep(1)


