from tkinter import *
from screeninfo import get_monitors

""" ONLY STORE STATIC VARIABLES """
#GUI variables
root = Tk()
monitors = get_monitors()
height = monitors[0].height- 200
width = height
root.title("Lin-Kernighan")
root.iconbitmap('./graphics/favicon.ico')
wndw = Canvas(root, width = width, height = height)
wndw.pack(expand = YES, fill=BOTH)

#GUI option
option = "1" #1: GUI; 2: w/o GUI

#weighted graph
wg = [] #initially empty. Modified by main.py

#coordinates and names
cityNames = []
rawCoords = []
guiCoords = []