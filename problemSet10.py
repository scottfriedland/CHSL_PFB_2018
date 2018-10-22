#!/usr/bin/env python3


# Keepin' it 'Classy'


class DNAsequence(object): #Making the class DNAsequence
	def __init__ (self, sequence, seq_id, organism): # Defining some attribute 'init'
		self.sequence = sequence
		self.seq_id = seq_id
		self.organism = organism
	
	def seqLen(self):
		length = len(self.sequence)
		return length
	
	def ntComp(self):
		A = 0
		T = 0
		C = 0
		G = 0
		self.sequence = self.sequence.upper()
		for nt in self.sequence:
			if nt == 'A':
				A += 1
			if nt == 'T':
				T += 1
			if nt == 'G':
				G += 1
			if nt == 'A':
				C += 1
		ntComp = {'A':A, 'T':T, 'C':C, 'G':G}
		return ntComp
							
# Setting those atrributes outside of the class

dna_seq_obj1 = DNAsequence('ACTGTCGTATGCTACGATTCGTACGATCGT','Fakegene1','Unicorns')
dna_seq_obj2 = DNAsequence('CGTGTACTGTACAGTAGCTAGCTGAT', 'Fakegene2', 'Werewolf')

# Looping through objs and printing them out
for dna_obj in [dna_seq_obj1 , dna_seq_obj2]:
	print(
	'{} from {}:\n {}\n Length is {} \n Nucleotide Composition:\n {}'
	.format(
	dna_obj.seq_id,
	dna_obj.organism,
	dna_obj.sequence,
	dna_obj.seqLen(),
	dna_obj.ntComp()
	))

# Take some of the info in the class and return other info
# Takes sequence attribute and prints sequence


