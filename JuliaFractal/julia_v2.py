import math
from datetime import datetime
import time

def write_out(point_list, filename):
	f = open(filename, 'w')
	for x in point_list:
		f.write(x+'\n')

def sqcomplex(nums): ##list of doubles [a, b]
	a = nums[0]**2
	b = 2 * nums[0]*nums[1] ##has i component
	c = -1 * (nums[1]**2) ##has i**2 component, so nums[1]^2 is multiplied by i^2 (-1)
	result = [a+c , b]
	return result

def multcompreal(comp, real):
	result = [comp[0]*real, comp[1]*real]
	return result
	
def add2complex(a, b): #2 lists of doubles
	result = [a[0]+b[0], a[1]+b[1]]
	return result

def add1complex(comp, real):
	comp[0] += real
	return comp
	
## c is the same for every pixel
## iterates using z = z^2 + c    <--- not anymore
##zk+1 = zk2 + c + P·zk-1

def calcnewz(z, c, p, oldz):
	return (add2complex(add1complex(sqcomplex(z), c), multcompreal(oldz, p)))

def test(z, c, p):
	iter = 0
	oldz = z
	z = calcnewz(z, c, p, oldz)
	while (z[0]**2 + z[1]**2) <= 4 and iter <= 100:   ##check that |z| < 2
		#print(z)
		z = calcnewz(z, c, p, oldz)
		#print (iter)
		oldz = z
		iter += 1
	print (iter)
	return iter

begin_time = datetime.now()

c = 0.59967
p = -0.7
z = [-2, -2] #[a, b] of a+bi

inc = 0.005 ## increment for z

z_list = [] # a, b, iterations taken to escape

while z[0] <= 2:
	while z[1] <= 2:
		i = test(z, c, p)
		if i > 0:
			z_list.append(str(z[0])+","+str(z[1])+ ","+ str(i))
		##print (z[0], z[1])
		z[1] += inc
	z[1] = -2
	z[0] += inc

print (z_list)
print("Almost done!")
filename = 'julia_v2_6.csv'  	## <<<<<<<<---- BEFORE RUNNING, SPECIFY NEW CSV FILENAME!!!!!!!
write_out(z_list, filename)  

now_time = datetime.now()		
print (now_time)
tdelta = now_time - begin_time		##shows how long program took to run
sec = tdelta.total_seconds()
print(sec)
print(sec/60) ## minutes

print ("This is v2 of julia set - inc = " + str(inc))
print("wrote out to " + filename)
print ("c = " + str(c) + str(p))