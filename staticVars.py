from tkinter import *
from screeninfo import get_monitors

""" ONLY STORE STATIC VARIABLES """
#GUI variables
monitors = get_monitors()
height = monitors[0].height- 200
width = height

#weighted graph
wg = [] #initially empty. Modified by main.py

#coordinates and names
cityNames = []
rawCoords = []
guiCoords = []