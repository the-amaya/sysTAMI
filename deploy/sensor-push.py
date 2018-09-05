#!/usr/bin/python

# version 0.9.5 - 9/4/18
# https://github.com/the-amaya/sysTAMI

import glob
import time
import Adafruit_DHT
import urllib
import urllib2

sensor = Adafruit_DHT.DHT22
pin = 4
with open("/home/pi/location.txt", "r") as locationfile:
	loc = locationfile.read()
	loc = loc.rstrip()
url = 'example.com/sensor.php' #webserver address to push data to- can be local or web facing
key = '' #API key if set in sensor.php on the server


def readsensor():
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
	temperature = temperature * 9.0 / 5.0 + 32.0 #the sensor is going to read Celsius, if you prefer that then just comment out this line
	query_t = '%f%s%f'%(time.time(), '&value=', temperature)
	query_h = '%f%s%f'%(time.time(), '&value=', humidity)
	return temperature, humidity;

def pushtemp(temperature, humidity):
	uri = urllib.urlencode({'time' : time.time(), 'temp' : temperature, 'humidity' : humidity, 'name' : loc, 'key' : key})
	req = urllib2.Request(url, uri)
	f = urllib2.urlopen(req)

temperature1, humidity1 = readsensor()
time.sleep(1)
temperature2, humidity2 = readsensor()
while abs(temperature1 - temperature2) > 3 or abs(humidity1 - humidity2) > 3: #take 2 reads and compare them to make sure we didnt get a false read
	time.sleep(1)
	temperature1, humidity1 = readsensor()
	time.sleep(1)
	temperature2, humidity2 = readsensor()

pushtemp(temperature1, humidity1)
