#!/usr/bin/env python3

import re

#Fishin for fasta

with open('Python_07.fasta','r') as Fasta:
	for line in Fasta: 
		if re.search(r'>',line):
			print(line)


with open('Python_07.fasta','r') as Fasta:
	for line in Fasta: 
		found = re.search(r'>(*+)|',line)
		fast_id = found.group(1)
		print(fast_id)

