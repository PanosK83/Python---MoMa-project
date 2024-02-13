
#LIBRARIES
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import sqlite3
from urllib.request import Request, urlopen
from io import BytesIO
import matplotlib.pyplot as plt
#import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import re

#CREATE MAIN GUI WINDOW
root=tk.Tk()
#min μέγεθος του παραθύρου ώστε να γίνονται display οι πληροφορίες
root.minsize(width=800, height=400) 
root.rowconfigure(0, weight=1)
root.columnconfigure(0, weight=1)
