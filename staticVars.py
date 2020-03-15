from tkinter import *
from win32.win32api import GetSystemMetrics

""" ONLY STORE STATIC VARIABLES """
#GUI variables
root = Tk()
height = GetSystemMetrics(1) - 200
width = GetSystemMetrics(0) - 200
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