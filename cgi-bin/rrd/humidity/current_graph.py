#!/usr/bin/env python

# version 0.9.5 - 9/4/18
# https://github.com/the-amaya/sysTAMI

import glob
import os
import rrdtool
import time
os.utime('cgi-bin/rrd/humidity/time.txt', None) #may need full path
imagePath = '/var/www/demo/images' #no trailing /
rrdLocation = "/var/www/demo/cgi-bin/rrd/humidity/" #with trailing /
rrdPath = rrdLocation + "*.rrd"
pathLength = len(rrdLocation)

def line_name(a):
 while len(a) < 20:
  a = a + ' '
 return a

def cus_color(a): #define colors based on location name. If a color is not defined for a location here, black will be used
 if a == 'test':
  a = 'ff00ff'
 elif a == 'example1':
  a = '990000'
 elif a == 'example2':
  a = 'cc7a00'
 elif a == 'example3':
  a = 'cccc00'
 elif a == 'example4':
  a = '669900'
 elif a == 'example5':
  a = '33cccc'
 elif a == 'example6':
  a = '6666ff'
 else:
  a = '000000'
 return a

def one_hour():
 a = """rrdtool.graph('""" + imagePath + """/humidity/01hr.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-3600', '--step', '60', '--title="Humidity over the past hour"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %', '--alt-y-grid'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a

def three_hours():
 a = """rrdtool.graph('""" + imagePath + """/humidity/03hr.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-10800', '--title="Humidity over the past three hours"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (3 * 60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a

def one_day():
 a = """rrdtool.graph('""" + imagePath + """/humidity/24hr.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-86400', '--title="Humidity over the past day"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (24 * 60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a

def one_week():
 a = """rrdtool.graph('""" + imagePath + """/humidity/1week.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-604800', '--title="Humidity over the past week"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (7 * 24 * 60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a

def four_weeks():
 a = """rrdtool.graph('""" + imagePath + """/humidity/4weeks.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-2419200', '--title="Humidity over the past month"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (4 * 7 * 24 * 60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a

def three_months():
 a = """rrdtool.graph('""" + imagePath + """/humidity/3months.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-7257600', '--title="Humidity over the three months"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (3 * 4 * 7 * 24 * 60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a

def one_year():
 a = """rrdtool.graph('""" + imagePath + """/humidity/1year.png', '--imgformat', 'PNG', '--width', '750', '--height', '350', '--start', '-29030400', '--title="Humidity over the past year"', '--disable-rrdtool-tag', '--vertical-label', 'Humidity %'"""
 for files in sorted(glob.glob(rrdPath)):
  if time.time() - os.path.getmtime(files) < (4 * 3 * 4 * 7 * 24 * 60 * 60):
   fname = files
   hex = files[pathLength:-4]
   lname = line_name(hex)
   hex = cus_color(hex)
   a = a + """, 'DEF:""" + hex + """=""" + files + """:temp:AVERAGE', """
   a = a + """'LINE1:""" + hex + """#""" + hex + """:""" + lname + """', """
   a = a + """'GPRINT:""" + hex + """:LAST:Curr %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MAX:Max %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:MIN:Min %6.2lf%s', """
   a = a + """'GPRINT:""" + hex + """:AVERAGE:Avg %6.2lf%s\l'"""
 a = a + ')'
 return a


fileCMD = rrdLocation + "cmd.py"
f = open(fileCMD, 'w+')
f.write("#!/usr/bin/env python\n")
f.write("import rrdtool\n")
f.write("try: ")
f.write(one_hour())
f.write("\nexcept:\n pass\ntry: ")
f.write(three_hours())
f.write("\nexcept:\n pass\ntry: ")
f.write(one_day())
f.write("\nexcept:\n pass\ntry: ")
f.write(one_week())
f.write("\nexcept:\n pass\ntry: ")
f.write(four_weeks())
f.write("\nexcept:\n pass\ntry: ")
f.write(three_months())
f.write("\nexcept:\n pass\ntry: ")
f.write(one_year())
f.write("\nexcept:\n pass\n")
f.close()
os.system(fileCMD)
