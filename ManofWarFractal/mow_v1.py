import math
from datetime import datetime
import time

def write_out(point_list, filename):
	f = open(filename, 'w')
	for x in point_list:
		f.write(x+'\n')

def addcomplex(a, b): #2 integer lists
	result = [a[0]+b[0], a[1]+b[1]]
	return result
	
def sqcomplex(nums): ##double list
	a = nums[0]**2
	b = 2 * nums[0]*nums[1] ##has i component
	c = -1 * (nums[1]**2) ##has i**2 component, so nums[1]^2 is multiplied by i^2 (-1)
	result = [a+c , b]
	return result

def calcnewz(c_vals, z, oz):
	return addcomplex(addcomplex(sqcomplex(z), c_vals), oz)    # z = z(sub k)^2 + c + z(sub k-1)

def test(c_vals, z):
	iter = 0
	oldz = z
	z = calcnewz(c_vals, z, oldz)
	while (z[0]**2 + z[1]**2) <= 4 and iter <= mi:
		#print(z)
		z = calcnewz(c_vals, z, oldz)
		oldz = z
		iter += 1
	print (iter)
	return iter
	
	
begin_time = datetime.now()

mi = 40 # global variable for max iterations
c = [-2, -2] #[a, b] of a+bi
z = [0, 0] #[a, b] of a+bi
inc = 0.005 ## increment for c
#print (addcomplex(c,z))
c_list = [] # a, b, iterations taken to escape

while c[0] <= 2:
	while c[1] <= 2:
		i = test(c, z)
		if i > 1:
			c_list.append(str(c[0])+","+str(c[1])+ ","+ str(i))
		print (c[0], c[1])
		c[1] += inc
	c[1] = -2
	c[0] += inc

print (c_list)
print("Almost done!")

filename = 'mow_v1_3.csv'			##<<<<<<< CHANGE EVERY TIME
write_out(c_list, filename)


now_time = datetime.now()
print (now_time)

tdelta = now_time - begin_time
sec = tdelta.total_seconds()
print(sec)
print(sec/60) ## minutes
print ("This is v1 of manowar - inc = " + str(inc))

with open("log1.txt", "a") as myfile:
    myfile.write("This is v1 of manowar: inc = " + str(inc)+ ", maxiter = " + str(mi) + ", saved to: "+ filename + " at " + str(now_time) + "\n")