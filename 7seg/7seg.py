#!/usr/bin/python

import sys
import time
import RPi.GPIO as GPIO

DATA = 22
LATCH = 23
SHIFT = 24

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

GPIO.setup(DATA, GPIO.OUT)
GPIO.setup(LATCH, GPIO.OUT)
GPIO.setup(SHIFT, GPIO.OUT)

digits = [
	0b11111101,
	0b01100001,
	0b11011011,
	0b11110011,
	0b01100111,
	0b10110111,
	0b10111111,
	0b11100001,
	0b11111111,
	0b11100111
]

next = 0
try:
	while True:
		GPIO.output(LATCH, GPIO.LOW)
		digit = digits[next]
		mask = 1
		for i in range(8):
			GPIO.output(SHIFT, GPIO.LOW)
			GPIO.output(DATA, GPIO.HIGH if (mask & digit) == 0 else GPIO.LOW)
			GPIO.output(SHIFT, GPIO.HIGH)
			mask <<= 1
		GPIO.output(LATCH, GPIO.HIGH)
		#print next
		next = (next + 1) % 10
		time.sleep(0.52)
except:
	print "exception: {0}".format(sys.exc_info()[0])

print "cleaning up"
GPIO.cleanup()