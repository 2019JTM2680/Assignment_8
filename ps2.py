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



