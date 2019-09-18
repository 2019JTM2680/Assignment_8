#!/usr/bin/python3
#The below functios are declared to format the text(like adding colors and alignment)
import shutil
columns = shutil.get_terminal_size().columns
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk))
def prYellow(skk): print("\033[93m {}\033[00m" .format(skk)) 
def prCyan(skk): print("\033[96m {}\033[00m" .format(skk)) 
# Creating a function to display board
def board ():
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'-------------')
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'|' ,index[0],'|',index[1] ,'|', index[2],'|')
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'-------------')
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'|' ,index[3],'|',index[4] ,'|', index[5],'|')
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'-------------')
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'|' ,index[6],'|',index[7] ,'|', index[8],'|')
	print ("\t\t\t\t\t\t\t\t\t\t\t\t"'-------------')		    
#main program starts here
prRed("TIC-TAC-TOE".center(columns))
prGreen("Welcome to the Game!".center(columns))
#Game instructions
prCyan("The index numbers and the index for game is indicated below:" .center(columns))
prCyan("Player A has numbers 1,3,5,7,9" .center(columns))
prCyan("Player B has numbers 2,4,6,8" .center(columns))
# index indicates the positions of board
index = [1,2,3,4,5,6,7,8,9]
board()
prCyan("Let's begin the Game!!!" .center(columns))
index = [" "," "," "," "," "," "," "," "," "]
board()
while True:
	print ("Player A, Enter your number and positon")
	num1 = int(input("Number : "))
	pos1 = int(input("Position : "))
	if num1%2 != 0:
		index[pos1-1] = num1
		break
	else:
		print ("Invalid input for Player A. Please enter an odd number\n")
board()
while True:
	print ("Player B, Enter your number and positon")
	num2 = int(input("Number : "))
	pos2 = int(input("Position : "))
	if num2 != num1 and pos2 != pos1:
		if num2%2 == 0:
			index[pos2-1] = num2
			break
		else:
			print ("Invalid input for Player B. Please enter an even number\n")
	else:
		print ("Invalid input. Already occupied postion. Enter a valid input\n")
board()
while True:
	print ("Player A, Enter your number and positon")
	num3 = int(input("Number : "))
	pos3 = int(input("Position : "))
	if num3 != num1 and num3 != num2 and pos3 != pos1 and pos3 != pos2:
		if num3%2 != 0:
			index[pos3-1] = num3
			break
		else:
			print ("Invalid input for Player A. Please enter an odd number\n")
	else:
		print ("Invalid input. Already occupied postion. Enter a valid input\n")
board()	
	




