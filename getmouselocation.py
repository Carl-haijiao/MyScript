# -*- coding: utf-8 -*-
"""
Created on Fri Jun 11 13:49:35 2021

@author: haijiao
"""

import time
import subprocess

while 1:
    subprocess.Popen('xdotool  getmouselocation',shell=True)
    time.sleep(2)
else:
    pass
