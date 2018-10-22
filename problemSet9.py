#!/usr/bin/env python3
import sys

#Makign f(x)s

DNA_input = sys.argv[1].rstrip()
print_length = sys.argv[2]

#def DNAchoppa(dna, width):	
#	dna = dna.rstrip()
#	newDNA = ''
#	for nt in dna:
#		newDNA = newDNA+nt
#		if len(newDNA) % width == 0:
#			newDNA = newDNA	+ '\n'
#	return newDNA 
#print(DNAchoppa(DNA_input,print_length))

# Second try
import re
	
def DNAprint(dna, width):
	regex_maker = r'(\w{1,' + width + '})'
	chunk = re.findall(regex_maker,dna)
	newline = '\n'
	newDNA = newline.join(chunk)
	return newDNA

print(DNAprint(DNA_input,print_length))



