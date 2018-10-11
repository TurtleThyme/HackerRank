#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    startspace = n - 1
    intnum = ""
    asd = 1
    for i in range(n):
        for i in range(startspace):
            intnum = intnum + " "
        for i in range(asd):
            intnum = intnum + "#"
        print(intnum)
        startspace -= 1
        asd += 1
        intnum = ""