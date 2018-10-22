#!/usr/bin/env python3

# Reading in a file of sequences in Fasta format

with open("Python_06.seq.txt","r") as Seqeunces_rev:
	for line in Seqeunces_rev:
		line = line.rstrip()
		Descriptions,Sequences = line.split()
		newDescrip = '>' + Descriptions + ' reverse complement\n' # New description
		RevSequences = Sequences[::-1] # Reversing the sequence
		lowRevSequences = RevSequences.lower()	#Make string lowercase
		switch1=lowRevSequences.replace('t','A') # Changin them nts (caps used to distinguish
		switch2=switch1.replace('a','T') 	 # changed nts from not
		switch3=switch2.replace('g','C')
		switch4=switch3.replace('c','G')
		RevComp = switch4 # Setting all these changes to RevComp
		# print(Descriptions,'looked like', Sequences[-10:], ' and is now\n',
		# newDescrip,RevComp[:10]) # Print out a sample of the data
		print(newDescrip,RevComp)
	
