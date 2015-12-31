import math
from datetime import datetime
import time

def write_out(point_list, filename):
	f = open(filename, 'w')
	for x in point_list:
		f.write(x+'\n')

##def find_magn(vector):  ##integer list
	##return (math.sqrt(vector[0]**2 + vector[1]**2))

def sqcomplex(nums): ##integer list
	a = nums[0]**2
	b = 2 * nums[0]*nums[1] ##has i component
	c = -1 * (nums[1]**2) ##has i**2 component, so nums[1]^2 is multiplied by i^2 (-1)
	result = [a+c , b]
	return result

def addcomplex(a, b): #2 integer lists
	result = [a[0]+b[0], a[1]+b[1]]
	return result

##the Mandelbrot set consists of all the choices for C 
##we can find (where Z starts at zero and C is a complex 
##number)
##so that the iterations never grow beyond the number 2

def calcnewz(c_vals, z):
	return addcomplex(sqcomplex(sqcomplex(sqcomplex(z))), c_vals)   ## z = z^4 + c

def test(c_vals, z):
	iter = 0
	while (z[0]**2 + z[1]**2) <= 4 and iter <= mi:
		#print(z)
		z = calcnewz(c_vals, z)
		iter += 1
	return iter

begin_time = datetime.now()

mi = 40 # global variable for max iterations
c = [-2, -2] #[a, b] of a+bi
z = [0, 0] #[a, b] of a+bi
inc = 0.002 ## increment for c
#print (addcomplex(c,z))
c_list = [] # a, b, iterations taken to escape

while c[0] <= 2:
	while c[1] <= 2:
		i = test(c, z)
		if i > 2:
			c_list.append(str(c[0])+","+str(c[1])+ ","+ str(i))
		print (c[0], c[1])
		c[1] += inc
	c[1] = -2
	c[0] += inc

print (c_list)
print("Almost done!")
filename = 'octmandy_v1_2.csv'    ## <<<<<<< 	CHANGE THIS EVERY TIME
write_out(c_list, filename)

now_time = datetime.now()
print (now_time)

tdelta = now_time - begin_time
sec = tdelta.total_seconds()
print(sec)
print(sec/60) ## minutes
print ("This is v2 - inc = 0.002")

with open("log1.txt", "a") as myfile:
    myfile.write("This is v1 of octic mandelbrot: inc = " + str(inc)+ ", maxiter = " + str(mi) + ", saved to: "+ filename + " at " + str(now_time) + "\n")

