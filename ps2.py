#!/usr/bin/python3
#The sys function is used for exiting program
import sys 
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
#Function to check success
def check (index):
#Checking whether all three elements are inserted and whether their sum is 15 vertically, horizontally and diagonally
	if index[0] != " " and index[1] != " " and index[2] != " ":
		if index[0] + index[1] + index[2] == 15:
			return 1
	elif index[3] != " " and index[4] != " " and index[5] != " ":
		if index[3] + index[4] + index[5] == 15:
			return 1
	elif index[6] != " " and index[7] != " " and index[8] != " ":
		if index[6] + index[7] + index[8] == 15:
			return 1
	if index[0] != " " and index[4] != " " and index[8] != " ":
		if index[0] + index[4] + index[8] == 15:
			return 1
	if index[0] != " " and index[3] != " " and index[6] != " ":
		if index[0] + index[3] + index[6] == 15:
			return 1
	if index[6] != " " and index[4] != " " and index[2] != " ":
		if index[6] + index[4] + index[2] == 15:
			return 1
	if index[2] != " " and index[5] != " " and index[8] != " ":
		if index[2] + index[5] + index[8] == 15:
			return 1
	if index[1] != " " and index[4] != " " and index[7] != " ":
		if index[1] + index[4] + index[7] == 15:
			return 1
	else:
		return 0 	
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
#Game starts
prCyan("Let's begin the Game!!!" .center(columns))
index = [" "," "," "," "," "," "," "," "," "]
board()
while True:
	#Accepting the input
	prCyan ("Player A, Enter your number and positon")
	num1 = int(input("Number : "))
	pos1 = int(input("Position : "))
#checking whether position is between 1-9
	if num1>0 and num1<10 and pos1>0 and pos1<10:
#checking whether odd number for player A
		if num1%2 != 0:
			index[pos1-1] = num1
			break
		else:
			prRed ("Invalid input for Player A. Please enter an odd number\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
#Displaying the board
board()
while True:
	prCyan ("Player B, Enter your number and positon")
	num2 = int(input("Number : "))
	pos2 = int(input("Position : "))
#checking whether odd number for player A
	if num2>0 and num2<10 and pos2>0 and pos2<10:
#checking whether it is an already entered postion or number
		if num2 != num1 and pos2 != pos1:
#checking whether even number for player B
			if num2%2 == 0:
				index[pos2-1] = num2
				break
			else:
				prRed ("Invalid input for Player B. Please enter an even number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
while True:
	prCyan ("Player A, Enter your number and positon")
	num3 = int(input("Number : "))
	pos3 = int(input("Position : "))
	if num3>0 and num3<10 and pos3>0 and pos3<10:
		if num3 != num1 and num3 != num2 and pos3 != pos1 and pos3 != pos2:
			if num3%2 != 0:
				index[pos3-1] = num3
				break
			else:
				prRed ("Invalid input for Player A. Please enter an odd number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
#checking for success
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER A WINS!!!" .center(columns))
	sys.exit()
while True:
	prCyan ("Player B, Enter your number and positon")
	num4 = int(input("Number : "))
	pos4 = int(input("Position : "))
	if num4>0 and num4<10 and pos4>0 and pos4<10:
		if num4 != num1 and num4 != num2 and num4 != num3 and pos3 != pos1 and pos3 != pos2 and pos4 != pos3:
			if num4%2 == 0:
				index[pos4-1] = num4
				break
			else:
				prRed ("Invalid input for Player B. Please enter an even number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER B WINS!!!" .center(columns))
	sys.exit()
while True:
	prCyan ("Player A, Enter your number and positon")
	num5 = int(input("Number : "))
	pos5 = int(input("Position : "))
	if num5>0 and num5<10 and pos5>0 and pos5<10:
		if num5 != num1 and num5 != num2 and num5 != num3 and num5 != num4 and pos5 != pos1 and pos5 != pos2 and pos5 != pos3 and pos5 != pos4:
			if num5%2 != 0:
				index[pos5-1] = num5
				break
			else:
				prRed ("Invalid input for Player A. Please enter an odd number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER A WINS!!!" .center(columns))
	sys.exit()
while True:
	prCyan ("Player B, Enter your number and positon")
	num6 = int(input("Number : "))
	pos6 = int(input("Position : "))
	if num6>0 and num6<10 and pos6>0 and pos6<10:
		if num6 != num1 and num6 != num2 and num6 != num3 and num6 != num4 and num6 != num5 and pos6 != pos1 and pos6 != pos2 and pos6 != pos3 and pos6 != pos4 and pos6 != pos5:
			if num6%2 == 0:
				index[pos6-1] = num6
				break
			else:
				prRed ("Invalid input for Player B. Please enter an even number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER B WINS!!!" .center(columns))
	sys.exit()
while True:
	prCyan ("Player A, Enter your number and positon")
	num7 = int(input("Number : "))
	pos7 = int(input("Position : "))
	if num7>0 and num7<10 and pos7>0 and pos7<10:
		if num7 != num1 and num7 != num2 and num7 != num3 and num7 != num4 and num7 != num5 and num7 != num6 and pos7 != pos1 and pos7 != pos2 and pos7 != pos3 and pos7 != pos4 and pos7 != pos5 and pos7 != pos6:
			if num7%2 != 0:
				index[pos7-1] = num7
				break
			else:
				prRed ("Invalid input for Player A. Please enter an odd number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER A WINS!!!" .center(columns))
	sys.exit()
while True:
	prCyan ("Player B, Enter your number and positon")
	num8 = int(input("Number : "))
	pos8 = int(input("Position : "))
	if num6>0 and num6<10 and pos6>0 and pos6<10:
		if num8 != num1 and num8 != num2 and num8 != num3 and num8 != num4 and num8 != num5 and num8 != num6 and num8 != num7 and pos8 != pos1 and pos8 != pos2 and pos8 != pos3 and pos8 != pos4 and pos8 != pos5 and pos8 != pos6 and pos8 != pos7:
			if num8%2 == 0:
				index[pos8-1] = num8
				break
			else:
				prRed ("Invalid input for Player B. Please enter an even number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER B WINS!!!" .center(columns))
	sys.exit()
while True:
	prCyan ("Player A, Enter your number and positon")
	num9 = int(input("Number : "))
	pos9 = int(input("Position : "))
	if num9>0 and num9<10 and pos9>0 and pos9<10:
		if num9 != num1 and num9 != num2 and num9 != num3 and num9 != num4 and num9 != num5 and num9 != num6 and num9 != num7 and num9 != num78 and pos9 != pos1 and pos9 != pos2 and pos9 != pos3 and pos9 != pos4 and pos9 != pos5 and pos9 != pos6 and pos9 != pos7 and pos9 != pos8:
			if num9%2 != 0:
				index[pos9-1] = num9
				break
			else:
				prRed ("Invalid input for Player A. Please enter an odd number\n")
		else:
			prRed ("Invalid input. Already occupied postion. Enter a valid input\n")
	else:
		prRed ("The number/position entered is invalid. Enter a number or position in range 1-9\n")
board()
i = check(index)
if i == 1:
	prGreen("\nCONGRATULATIONS!!!! PLAYER A WINS!!!" .center(columns))
	sys.exit()
else:
	prGreen("\nGAME DRAWN!!!" .center(columns))
