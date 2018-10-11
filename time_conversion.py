#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    arr = s.split(':')
    hh = int(arr[0])
    mm = int(arr[1])
    ss = int(arr[2][:2])
    isam = True if arr[2][2:] == 'AM' else False
    if hh == 12 and isam == True:
        hh = 0
    if isam == False:
        if hh == 12:
            pass
        else:
            hh += 12
    return '{:02}:{:02}:{:02}'.format(hh, mm, ss)