import sys
from numpy import random

file = open(sys.argv[2])
file1 = open(sys.argv[3],"w")
flag = False
for line in file.readlines():
	data = line.split()
	if data[1] =="0": 
		flag = False
		if random.rand() < float(sys.argv[1]):
			flag = True
			file1.write(line)
	elif flag:
		file1.write(line)
		
file1.close()

