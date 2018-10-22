#!/usr/bin/env python3

import re
import sys

# Fasta reformatter

Fasta_fileName = sys.argv[1]
line_length = sys.argv[2]

def SequenceFormatter(sequence, length):
	form_sequence = re.findall(r'(\w{1,'+length+'})',sequence)
	form_sequence = '\n'.join(form_sequence)
	return form_sequence
	

header = ''
sequence = ''
with open(Fasta_fileName, 'r') as fileObject:
	for line in fileObject:
		line = line.rstrip()
		if line.startswith('>'):
			if len(sequence) > 0:
				print(header+'\n'+SequenceFormatter(sequence, line_length))
			header = line
			sequence = ''
		else:
			sequence += line	
	print( header+'\n'+SequenceFormatter(sequence, line_length))

