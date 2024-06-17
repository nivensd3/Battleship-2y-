import RPi.GPIO as GPIO
#import GPIOmock as GPIO
import threading
import time
import random
import os
from subprocess import call

# Lights
RLIGHTS = [7, 13, 29, 18, 37, 33, 12, 40, 36]
GLights = [23, 15, 11, 12, 35, 31, 22, 38, 18]
OLights = [7+23, 13+15, 11+29, 18+12, 37+35, 33+31, 2+12, 40+38, 36+18]