#!/usr/bin/python

from Adafruit_CharLCD import Adafruit_CharLCD
from subprocess import *
from time import sleep, strftime
from datetime import datetime
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

lcd = Adafruit_CharLCD()

cmd = "ip addr show wlan0 | grep inet | awk '{print $2}' | cut -d/ -f1"

lcd.begin(16,1)

def run_cmd(cmd):
	p = Popen(cmd, shell=True, stdout=PIPE)
	output = p.communicate()[0]
	print output
	return output

#while 1:
	#lcd.clear()
	#ipaddr = run_cmd(cmd)
	#lcd.message(datetime.now().strftime('%b %d  %H:%M:%S\n'))
	#lcd.message('IP %s' % (ipaddr))
	#sleep(2)
	
	#str = raw_input().replace('\\n', '\n')
	#lcd.clear()
	#lcd.message("{0}\n".format(str))
	
lcd.message("Hi, I am\nRaspberry Pi :)")

input = raw_input()
lower_input = input.lower()
while(lower_input != "quit"):
	lcd.clear()
	if (lower_input == "open the pod bay doors"):
		lcd.message("I'm afraid I\ncan't do that")
	else:
		if (len(input) > 16):
			lcd.message(input[:16] + '\n' + input[16:])
		else:
			lcd.message(input)
	input = raw_input()
	lower_input = input.lower()