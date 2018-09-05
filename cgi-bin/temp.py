#!/usr/bin/env python

# version 0.9.5 - 9/4/18
# https://github.com/the-amaya/sysTAMI

import sys
import glob
import time
import os
import rrdtool
import smtplib

time = (sys.argv[1])
value = (sys.argv[2])
name = (sys.argv[3])
checkfloat = float(value)
debug = 0
alert = "./alert.py temp " + value + " " + name #may require absolute path

if (45 < checkfloat < 85): #acceptable temp range
	pass
else:
	pass #comment this line and uncomment the next if you are using the alert function
	#os.system(alert)

query_q = str(time + ':' + value)
filerrd = (name + '.rrd')
outName = str('./rrd/temp/' + filerrd) #may require absolute path
if not os.path.exists(outName):
 rrdtool.create( outName,
 '--start', '-300',
 '--step', '60',
 'DS:temp:GAUGE:1200:-50:250',
 'RRA:AVERAGE:0.5:1:2880',
 'RRA:AVERAGE:0.5:5:2016',
 'RRA:AVERAGE:0.5:60:2192',
 'RRA:AVERAGE:0.5:180:2920',
 'RRA:AVERAGE:0.5:720:1500',
 'RRA:AVERAGE:0.5:1440:2000',
 'RRA:MIN:0.5:1:2880',
 'RRA:MIN:0.5:5:2016',
 'RRA:MIN:0.5:60:2192',
 'RRA:MIN:0.5:180:2920',
 'RRA:MIN:0.5:720:1500',
 'RRA:MIN:0.5:1440:2000',
 'RRA:MAX:0.5:1:2880',
 'RRA:MAX:0.5:5:2016',
 'RRA:MAX:0.5:60:2192',
 'RRA:MAX:0.5:180:2920',
 'RRA:MAX:0.5:720:1500',
 'RRA:MAX:0.5:1440:2000' )

rrdtool.update(outName, query_q)
