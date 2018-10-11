#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the birthdayCakeCandles function below.
def birthdayCakeCandles(ar):
    start = 0
    count = 0
    for i in range(len(ar)):
        if start < ar[i]:
            start = ar[i]
    for i in range(len(ar)):
        if start == ar[i]:
            count += 1
    return count