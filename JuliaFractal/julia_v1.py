import math
from datetime import datetime
import time

def write_out(point_list, filename):
	f = open(filename, 'w')
	for x in point_list:
		f.write(x+'\n')

def sqcomplex(nums): ##double list
	a = nums[0]**2
	b = 2 * nums[0]*nums[1] ##has i component
	c = -1 * (nums[1]**2) ##has i**2 component, so nums[1]^2 is multiplied by i^2 (-1)
	result = [a+c , b]
	return result
	
def addcomplex(a, b): #2 double lists
	result = [a[0]+b[0], a[1]+b[1]]
	return result
	
	
## c is the same for every pixel
## iterates using z = z^2 + c

def calcnewz(z, c):
	return addcomplex(sqcomplex(z), c)

def test(z, c):
	iter = 0
	while (z[0]**2 + z[1]**2) <= 4 and iter <= 200:   ##check that |z| < 2
		#print(z)
		z = calcnewz(z, c)
		iter += 1
	return iter

begin_time = datetime.now()

c = [0.56667, -0.5] #[a, b] of a+bi 	Stays constant
z = [-2, -2] #[a, b] of a+bi

inc = 0.002 ## increment for z

z_list = [] # a, b, iterations taken to escape

while z[0] <= 2:
	while z[1] <= 2:
		z_list.append(str(z[0])+","+str(z[1])+ ","+ str(test(z, c)))
		print (z[0], z[1])
		z[1] += inc
	z[1] = -2
	z[0] += inc

print (z_list)
print("Almost done!")
filename = 'julia_v1_5.csv'  	## <<<<<<<<---- BEFORE RUNNING, SPECIFY NEW CSV FILENAME!!!!!!!
write_out(z_list, filename)   ##WRITES OUT. BEFORE RUNNING, SPECIFY NEW CSV FILENAME!!!!!!!

now_time = datetime.now()		
print (now_time)
tdelta = now_time - begin_time		##shows how long program took to run
sec = tdelta.total_seconds()
print(sec)
print(sec/60) ## minutes

print ("This is v1 of julia set - inc = " + str(inc))
print ("c = " + str(c[0]) + str(c[1]))
print ("filename: " + filename)

with open("log1.txt", "a") as myfile:
    myfile.write("This is v1 of julia set: inc = " + str(inc)+ "c = "+ str(c[0]) + str(c[1])+ "saved to: "+ filename + "\n")