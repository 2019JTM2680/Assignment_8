#!/usr/bin/python3
#The below functios are declared to format the text(like adding colors and alignment)
import shutil
columns = shutil.get_terminal_size().columns
def prRed(skk): print("\033[91m {}\033[00m" .format(skk)) 
def prGreen(skk): print("\033[92m {}\033[00m" .format(skk)) 
#main program starts here
prRed("TIC-TAC-TOE".center(columns))
