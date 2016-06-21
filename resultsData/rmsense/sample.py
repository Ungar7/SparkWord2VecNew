import sys
from numpy import random

listWords = ['bank', 'good', 'juice', 'google', 'apple', 'book']

filesyn0 = open(sys.argv[1])
file1 = open(sys.argv[2],"w")
file2 = open(sys.argv[3],"w")

syn0 = filesyn0.readlines()

#wordlist = file1.readlines()

for line in syn0:
	data = line.split()
	if data[0] in listWords or random.rand() < float(sys.argv[4]):
		for i in range(2,len(data)):
			file2.write(data[i]+" ")
		file2.write("\n")
		file1.write(data[0]+"_"+data[1]+"\n")
		

file1.close()
file2.close()
