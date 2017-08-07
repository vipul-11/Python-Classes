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


#To create a newfile and write Data to it.
#To be used when file with the name is not found.
def create(fileName):
	f= open(fileName,'w')
	#Debugged_by_Yash: Print Statement has to be outside the loop to avoid multiple echo
	print("Enter Content of File , enter #exit to exit ")
	while True:
		content = input()
		if content == '#exit':
			break
		#Debugged_by_Yash: Fwrite should add newline character for new line
		f.write(content + "\n")
	f.close()





def main():
	#Write the starter code that displays 
	#The program name and pauses for some time.
	#Then cleares the screen.


	#Now the idea is to check , whether a file 
	# with the filename as specified by user 
	# exist or not.

	try:
		
		#this edit section is not working yet !
		
		f = open(sys.argv[1],'r+')
		# Display the content available in the 
		# file currently.
		content = f.read()
		print(content)
		# As after reading the complete file
		# the file pointer has moved to the end 
		# of the file , we should set it back to 
		# starting by using seek function
		f.seek(0)
		
		currentPointer = f.tell()
		
		print('Current filepointer Position:',currentPointer)
		change = int(input('\nEnter the number of characters you want to move the pointer: '))
		
		#Debugged_by_Yash:Folowing line added to actually move the cursor
		f.seek(f.tell() + change)
		
		text = input('\nEnter the content to be replaced\n: ')
		#Debugged_by_Yash: no need for if and else statements due to line 69
		f.write( text )
	except:
		create(sys.argv[1])



if __name__ == '__main__':
	main()