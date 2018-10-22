#!usr/bin/env python3
import sys
import re

#Fasta parser ... again

FastaFileName = sys.argv[1]

FastaFileObject = open(FastaFileName)

fastaDict = {}
sequence = ''
for line in FastaFileObject:
	line = line.rstrip()
	if line.startswith('>'):
		if len(sequence)  0:	
			key = line
		else:
			fastaDict[key] = sequence
	else:
		sequence += line
