#!/usr/bin/python
#Reading the number
bin = int(input("Enter the binary number to br encoded:	"))
print (bin)
#Splitting the number into digits and storing it to a list
digits = [int(d) for d in str(bin)]
print (digits)
count=0
#counting the number of ones to implement parity check
for i in digits:
	if i==1:
		count+=1
print (count) 
