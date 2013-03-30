#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

#print GPIO.VERSION

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(25, GPIO.OUT)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

button_on = False
#print "BUTTON {0}".format(button_on)

GPIO.add_event_detect(24, GPIO.RISING)

def cb():
	global button_on
	button_on = not button_on
	#print "BTN {0}".format(button_on)

GPIO.add_event_callback(24, cb)

#GPIO.add_event_detect(24, GPIO.BOTH, callback=cb)

#print "starting loop"

try:
	while True:
		#print 'loop {0}'.format(button_on)
		#time.sleep(1)
		if button_on:
			#print 'x'
			GPIO.output(25, GPIO.HIGH)
			time.sleep(0.1)
			GPIO.output(25, GPIO.LOW)
			time.sleep(0.1)
		else:
			GPIO.output(25, GPIO.LOW)
except:
	print "exception: {0}".format(sys.exc_info()[0])

print "cleaning up"
GPIO.cleanup()
