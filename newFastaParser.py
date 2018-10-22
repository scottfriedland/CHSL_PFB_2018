#!/usr/bin/env python3
from Bio import SeqIO
from Bio import Seq

GCcontTable = []
idTable = []
GeneTable = [[idTable],[GCcontTable]]
for secrec in SeqIO.parse('./human_cds.fasta', 'fasta'):
	sequence = str(secrec.seq)
	seqID = secrec.id
	secLen = len(sequence)
	sequence = sequence.upper()
	A = 0
	T = 0
	C = 0
	G = 0
	for nt in sequence:
		if nt == 'A':
			A += 1	
		if nt == 'T':
			T += 1	
		if nt == 'G':
			G += 1	
		if nt == 'C':
			C += 1
	ntComp = {'A':A,'T':T,'C':C,'G':G}
	GCcont = (G+C)/secLen	
	idTable.append(seqID)
	GCcontTable.append(GCcont)
	#print(seqID,':',ntComp,'\nGC Content is:',GCcont)
print(GeneTable)
	
