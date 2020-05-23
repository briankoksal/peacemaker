#!/usr/bin/python

#features to implement
#remote kill switch (read value from azure database, if it can't for any reason then cancel it)
#randomness 
#read config values from online database, remotely reload config

#https://www.raspberrypi.org/documentation/usage/audio/
#ps -e -o pid,args --forest

import random
import time
import subprocess
import os
import signal

#config variables
mode= 0 #0=simple fixed volume, 1=random volume
default_runtime = .5*60; #seconds
min_volume = 0
max_valume = -4000
current_volume = (max_valume-min_volume) / 2


#used only in mode 1 (random mode)
randomness_factor = 0  #(runtime in minutes, volume range)
volume_range_min = min_volume
volume_range_max = max_valume


#simple mode
if mode ==0:

  #https://stackoverflow.com/questions/17809409/how-to-start-kill-application-with-python-script
  p = subprocess.Popen(["omxplayer", "--no-keys", "--loop", "/root/piano2.wav", "--vol", str(current_volume) ])
  print "Process ID of subprocess %s" % p.pid

  #wait the default_runtime before killing the process
  time.sleep(default_runtime) 

  # Send SIGTER (on Linux)
  #p.terminate()
  #https://stackoverflow.com/questions/42648803/python-subprocess-popen-kill-process-with-child-processes
  os.killpg(p.pid, signal.SIGTERM)
  # Wait for process to terminate
  returncode = p.wait()
  print "Returncode of subprocess: %s" % returncode

#rondom mode
elif mode==1:
  print "Not yet implemented!"

  umber = random.randint(1, 20)
  print ('Well, {0}, I am thinking of a number between 1 and 20.'.format('Brian'))

  #kill = False
  #while (kill == False):