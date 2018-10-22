#!/usr/bin/env python3

# Working with data structures

# Making a Data Structure to hold parts of a multi-fasta file
import re

multiFasta = {}
geneInfo = {}
with open("Python_07.fasta", 'r') as fasta:
	for line in fasta:
		line = line.rstrip()
		for header in re.finditer(r'^>(\S+)\s(.+)', line):	
			ID = header.group(1)
			Descr = header.group(2)
			multiFasta[ID] = geneInfo
			geneInfo['Description'] = Descr
			geneInfo['ID'] = ID

print('Fasta contains:', multiFasta) 
