#!/usr/bin/env python3

# Practicing Regular Expressions
import re

#line_count=1
#with open('Python_07_nobody.txt','r') as nobody_file:
#	for lines in nobody_file:
#		lines = lines.rstrip()
#		Nobody = re.search(r'Nobody', lines)
	#	if Nobody:
		#	print('Found Nobody at', Nobody.start(), 'on line', line_count)
#		line_count+=1

# Writing out a file with some substitutions

Somebody = open("ScottIsSomebody.txt",'w')

with open('Python_07_nobody.txt','r') as nobody_file:
	for lines in nobody_file:
		lines = lines.rstrip()
		Nobody = re.sub(r'Nobody','Scott',lines)
		Somebody.write(Nobody + '\n')
Somebody.close()
print("Wrote a file called ScottIsSomebody.txt")


