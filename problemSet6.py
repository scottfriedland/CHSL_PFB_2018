#!/usr/bin/env python3

# Opening the file Python_06.txt and doing things to it
# Then writing output to new file
Python_06_uc = open("Python_06_uc.txt","w")

with open("Python_06.txt","r") as file_object: #read in the file in a covenient way
	for line in file_object: # read through line by line
		line = line.rstrip() # remove new lines
		upperLine = line.upper() # make all lines upper case
		print(upperLine) # print to stdout
		Python_06_uc.write(upperLine +"\n") #write line by line to a file 

Python_06_uc.close()  # close that file
print("\n Made a file called Python_06_uc.txt") # let folks know ya done did it

		
