import sys

filesyn0 = open(sys.argv[1])
file1 = open(sys.argv[2])
file2 = open(sys.argv[3],"w")

syn0 = filesyn0.readlines()

wordlist = file1.readlines()

for word in wordlist:
	lineData = 0
	for line in syn0:
		data = line.split()
		#print(data[0]+"_"+data[1])
		if data[0]+"_"+data[1] == word[:len(word)-1]:
			lineData = data
			break
	for i in range(2,len(data)):
		file2.write(data[i]+" ")
	file2.write("\n")
	print(lineData)

file2.close()
