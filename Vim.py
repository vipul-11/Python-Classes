#!/usr/bin/python3

#Debugged_by_Yash: Shebang has to be the very first line

'''
vim mimic program.
line one uses shebang which let's you use the 
program without specifying the Name of the 
intrepretor.
'''

#Debugged_by_Yash: Inconsistant and mixed used of spaces and tabs
#converted in to pure tabs only code

#imported under used libraries
import sys 
import os
import time
#following class has static charachters which enables colors when concatinated with strings 
class color:
	#Start with any of these
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	#End with color.ENDC always
	ENDC = '\033[0m'

def splashScreen():
	#splash screen for two seconds
	print(color.HEADER + color.BOLD + color.UNDERLINE + "\t\tWelcome to Vim Mimic 1.0" + color.ENDC)
	time.sleep(2)

#To create a newfile and write Data to it.
#To be used when file with the name is not found.
def create(fileName):
	f= open(fileName,'w')
	#Debugged_by_Yash: Print Statement has to be outside the loop to avoid multiple echo
	print(color.OKBLUE+"Enter Content of File , enter #exit to exit " + color.OKGREEN)
	while True:
		content = input()
		if content == '#exit':
			break
		#Debugged_by_Yash: Fwrite should add newline character for new line
		f.write(content + "\n")
	f.close()

def editFile(fileName):
	try:
		f = open(fileName,'r+')
		f.seek(0)
		#while added for multiple edits
		while(True):
			print(color.OKBLUE+'Current Cursor Position:' + color.ENDC,f.tell())
			change = int(input(color.BOLD +'\nEnter The Number of Characters You Want To Move The Cursor\n\tor\nEnter 0 to Finish\n: '+color.ENDC))
			if(change == 0):
				break
			#Debugged_by_Yash:Folowing line added to actually move the cursor
			f.seek(f.tell() + change)
			
			text = input(color.BOLD+'\nEnter new content\n: '+color.ENDC)
			#Debugged_by_Yash: no need for if and else statements
			f.write( text )
			f.clear()
			readFile(fileName)
	except:
		print(color.FAIL +"File To Be Read Not Found !" + color.ENDC)

def readFile(fileName):
	try:
		f = open(fileName,'r')
		content = f.read()
		print(color.HEADER+"-----------------"+fileName+"-----------------"+color.ENDC)
		print(color.OKGREEN + content + color.ENDC)
		print(color.HEADER+"----------------------------------------------\n"+color.ENDC)
		f.close()
	except:
		print(color.WARNING +"File Does Not Exist, Created New File" + color.ENDC)
		create(fileName)	



def main():
	splashScreen()
	fileName = sys.argv[1]
	while(True):
		os.system("clear")
		readFile(fileName)
		print(color.BOLD + color.OKBLUE+"\nPress 1 to Edit \n       or\nPress 0 to Exit"+color.ENDC)
		opt = input()
		if(opt != "0"):
			editFile(fileName)
		else:
			break	


if __name__ == '__main__':
	main()