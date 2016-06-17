import sys

file = open(sys.argv[1])
file1 = open(sys.argv[2],"w")
file2 = open(sys.argv[3],"w")
for line in file.readlines():
	d = line.split()
	file2.write(d[0]+"_"+d[1]+"\n")
	for i in range(2,len(d)):
		file1.write(d[i]+" ")
	file1.write("\n")
file1.close()
file2.close()

