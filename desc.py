
#!/usr/bin/python
# -*- coding: utf-8 -*-

#<--Import lib
import matplotlib.pyplot as plt
import numpy as np
import threading

from math import *
from ezprint import *
from tkinter import *
from main import *


def main_frame(a, b, c, D, xo, yo, x_null_0, x_null_1, x_null_2, x_list, y_list, func_name):
	global thirdFrame

	#<--Settings for secondFrame
	thirdFrame = Tk()

	thirdFrame.title(func_name)

	thirdFrame.resizable(0, 0)

	xo = round(xo, 3)
	label1 = Label(thirdFrame, text = 'Your args:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c), bg='grey', fg='black')
	label2 = Label(thirdFrame, text = 'Discriminant: ' + str(D), bg='grey', fg='black')
	label3 = Label(thirdFrame, text = 'TOPS FUNC.', bg='grey', fg='black')
	label4 = Label(thirdFrame, text = 'x tops: ' + str(xo), bg='grey', fg='black')
	label5 = Label(thirdFrame, text = 'y tops: ' + str(yo), bg='grey', fg='black')
	label6 = Label(thirdFrame, text = 'NULL FUNC.', bg='grey', fg='black')
	
	if D == 0:
		label7 = Label(thirdFrame, text = 'x: ' + str(x_null_0), bg='grey', fg='black')
	elif D > 0:
		label7 = Label(thirdFrame, text = 'x1: ' + str(x_null_1) + '\n' + 'x2: ' + str(x_null_2), bg='grey', fg='black')
	else:
		label7 = Label(thirdFrame, text = 'Not exist', bg='grey', fg='white')
	label8 = Label(thirdFrame, text = 'PROPERTIES:', bg='grey', fg='white')
	if a > 0:
		label9 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=[0; +∞)\n3) Even function\n4)The function decreases in the interval (-∞; ' + str(xo) + ')\n  The function increases in the interval (' + str(xo) + '; +∞)\n5) Asymptote has not', bg='grey', fg='black')
	else:
		label9 = Label(thirdFrame, text = '1) D(f)=R or (-∞; +∞)\n2) E(f)=(-∞; 0]\n3) Even function\n4)The function decreases in the interval (' + str(xo) + '; +∞)\n  The function increases in the interval (-∞; ' + str(xo) + ')\n5) Asymptote has not', bg='grey', fg='black')
	if a > 0:
		label10 = Label(thirdFrame, text = '6) Min value of x: ' + str(round(np.amin(x_list), 5)) + '\n   Min value of y: ' + str(round(min(y_list), 5)), bg='grey', fg='black')
		label11 = Label(thirdFrame, text = '   Max value of x: not exist' + '\n   Max value of y: not exist', bg='grey', fg='black')
	else:
		label10 = Label(thirdFrame, text = '6) Min value of x: not exist' + '\n   Min value of y: not exist', bg='grey', fg='black')
		label11 = Label(thirdFrame, text = '   Max value of x: ' + str(round(np.amax(x_list), 5)) + '\n   Max value of y: ' + str(round(max(y_list), 5)), bg='grey', fg='grey')
	#<--Configs
	label1.config(font = ('Arial', 15, 'bold'))
	label2.config(font = ('Arial', 15, 'bold'))
	label3.config(font = ('Arial', 15, 'bold'))
	label4.config(font = ('Arial', 15, 'bold'))
	label5.config(font = ('Arial', 15, 'bold'))
	label6.config(font = ('Arial', 15, 'bold'))
	label7.config(font = ('Arial', 15, 'bold'))
	label8.config(font = ('Arial', 15, 'bold'))
	label9.config(font = ('Arial', 15, 'bold'))
	label10.config(font = ('Arial', 15, 'bold'))
	label11.config(font = ('Arial', 15, 'bold'))

	#<--Grids
	label1.grid(column = 0, row = 0)
	label2.grid(column = 0, row = 1)
	label3.grid(column = 0, row = 2)
	label4.grid(column = 0, row = 3)
	label5.grid(column = 0, row = 4)
	label6.grid(column = 0, row = 5)
	label7.grid(column = 0, row = 6)
	label8.grid(column = 0, row = 7)
	label9.grid(column = 0, row = 8)
	label10.grid(column = 0, row = 9)
	label11.grid(column = 0, row = 10)

	#<--Start
	thirdFrame.mainloop()
