#!/usr/bin/python
#Program used for testing LED functions using
#GPIO outputs

import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


GPIO.setwarnings(False)
GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
#Turn LEDs  on
print "Turn on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs  off
print "Turn off"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
#Turn LEDs  on
print "Turn on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs  off
print "Turn off"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
#Turn LEDs  on
print "Turn on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs  off
print "Turn off"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
#Turn LEDs  on
print "Turn on"
GPIO.output(17,GPIO.HIGH)
GPIO.output(27,GPIO.HIGH)
time.sleep(1)
#Turn LEDs  off
print "Turn off"
GPIO.output(17,GPIO.LOW)
GPIO.output(27,GPIO.LOW)
time.sleep(1)
print "DONE"

GPIO.cleanup
