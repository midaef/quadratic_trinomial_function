
import matplotlib.pyplot as plt
from ezprint import *
import numpy as np
from math import *

x_null_0 = 0
x_null_1 = 0
x_null_2 = 0
x_list = []
y_list = []
xo = 0
yo = 0
D = 0


def create_plot(a, b, c):
	global x_list
	global y_list

	if D < 0:
		x_list.append(xo)
		y_list.append(yo)
		for i in range(1, 6):
			x_list.append(i)
		for j in range(len(x_list)):
			for k in x_list:
				func = a * k**2 + b *k + c
				y_list.append(func)
		# plt.plot(x_list, y_list)
		# plt.show()
		return x_list, y_list

	elif D > 0:
		for i in range(1, 6):
			x_list.append(i)
		for j in range(1, 6):
			for k in x_list:
				func = a * k**2 + b *k + c
				y_list.append(func)
		# plt.plot(x_list, y_list)
		# plt.show()
		return x_list, y_list


def f(a, b, c):
	# a * x**2 + b * x + c
	global x_null_1
	global x_null_2
	global xo
	global yo
	global D

	#search tops
	xo = -b / (2 * a)
	yo = -((b**2 - 4 * a * c) / 4 * a)
	#search Disc.
	D = b**2 - 4 * a * c
	if D > 0:
		#search null func.
		x_null_1 = ((-b + sqrt(D)) / 2 * a)
		x_null_2 = (-b - sqrt(D)) / 2 * a
	elif D == 0:
		x_null_0 = -b / (2 * a)
	elif D < 0:
		p('Discriminant < 0')


def main():
	a = int(input('Input a: '))
	b = int(input('Input b: '))
	c = int(input('Input c: '))
	f(a, b, c)
	p(create_plot(a, b, c))
	cls()
	p('Your args:\na= ' + str(a) + '\nb= ' + str(b) + '\nc= ' + str(c))
	p('Discriminant: ' + str(D))
	p('TOPS FUNC.')
	p('x tops: ' + str(xo))
	p('y tops: ' + str(yo))
	p('NULL FUNC.')
	p('x_1 null: ' + str(x_null_1))
	p('x_2 null: ' + str(x_null_2))
	


if __name__ == '__main__':
	main()