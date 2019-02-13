#!/usr/bin/python
import time
import RPi.GPIO as gpio
import sys
import Tkinter as tk

def init():
	gpio.setmode(gpio.BCM)
	gpio.setwarnings(False)
	gpio.setup(17,gpio.OUT)
	gpio.setup(27,gpio.OUT)

def turn_on(tf):
	#Turn LEDs  on
	print "Turn on"
	gpio.output(17,gpio.HIGH)
	gpio.output(27,gpio.HIGH)
	time.sleep(tf)

def turn_off(tf):
	#Turn LEDs  off
	print "Turn off"
	gpio.output(17,gpio.LOW)
	gpio.output(27,gpio.LOW)
	time.sleep(tf)
	gpio.cleanup

def key_input(event):
	init()
	print 'Key:' , event.char
	key_press = event.char
	sleep_time = 0.030

	if key_press.lower() == 'w':
		turn_on(sleep_time)
	elif key_press.lower() == 's':
			turn_off(sleep_time)
	else:
		gpio.cleanup

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()