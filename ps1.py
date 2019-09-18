#!/usr/bin/python3
#Reading the number
bin = input("Enter the binary number to br encoded:	")
#Splitting the number into digits and storing it to a list
digits = [int(d) for d in str(bin)]
count=0
#counting the number of ones to implement parity check
for i in digits:
	if i==1:
		count+=1
#checking odd parity
if (count%2)==0:
	digits.append(int(1))
else:
	digits.append(int(0))
#converting the splitted list back to string
parity = ("".join(map(str, digits)))
#Output for fisrt part
print ("Parity bit data : ", parity)
#Encodind the message by adding 0 to the patter 010
temp = parity.replace("010","0100")
#Adding  string 0101 is used as the bit string or flag to indicate the end of the frame
final = temp + "0101"
print ("Transmitting data : ", final)
		 
