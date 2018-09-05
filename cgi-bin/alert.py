#!/usr/bin/env python3

# version 0.9.5 - 9/4/18
# https://github.com/the-amaya/sysTAMI

import sys
import glob
import time
import smtplib
import os.path

type = (sys.argv[1])
value = (sys.argv[2])
name = (sys.argv[3])

debug = 0
receiver = [''] #where to send the alert -this can also be a phone number and sms gateway
sender = '' #who the message is from
smtpObj = smtplib.SMTP('your.mail.server', 587) #your smtp server and port this host will need to be in the trusted networks, or you can configure a valid account to send from
multireadwait = "./loc/" + type + "-" + name + "-multi-read.loc" #used to wait for two readings outside of range within 15 minutes before sending alerts
lock = "./loc/" + type + "-" + name + ".loc" #used to only send 1 alert per sensor/location per 15 minutes

message_humidity = """From: sender <sender@example>
To: receiver <receiver@example>
Subject: Humidity sensor outside accepted range
Humidity in location """ + name + """ is outside of expected range. Current value= """ + value + """ expected range 15~85
view live data at https://example.com"""

message_temp = """From: sender <sender@example>
To: receiver <receiver@example>
Subject: Temperature sensor outside accepted range
Temperature in location """ + name + """ is outside of expected range. Current value= """ + value + """ expected range 45~85
view live data at https://example.com"""

def mailtype():
	if type == 'temp':
		sendmail(message_temp)
	elif type == 'humidity':
		sendmail(message_humidity)
	else:
		exit()

def sendmail(message):
	try:
		smtpObj.sendmail(sender, receiver, message)
		if debug == 1:
			with open("debug.txt", "a+") as myfile:
				myfile.write("%s - %s\n" % (now, "message sent"))
	except:
		if debug == 1:
			with open("debug.txt", "a+") as myfile:
				myfile.write("%s - %s\n" % (now, "unable to send email"))

if os.path.isfile(multireadwait):
	if (time.time() - os.path.getmtime(multireadwait) < (60 * 15)): #time that multiple reads must happen within in to trigger an alert
		open(multireadwait, 'w+').close()
		if os.path.isfile(lock):
			if (time.time() - os.path.getmtime(lock) > (60 * 15)): #time to wait before resending an alert
				open(lock, 'w+').close()
				mailtype()
		else:
			open(lock, 'w+').close()
			mailtype()
	else:
		open(multireadwait, 'w+').close()
else:
	open(multireadwait, 'w+').close()