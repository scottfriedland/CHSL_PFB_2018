#!/usr/bin/env python3


# Making a simple alligner 

sequence1 = 'agtctgtca'
sequence2 = 'gatctctgc'
scoreValue = 1
# Function for reverse complementing dna
def revComp(dna):
	newSequence = ''
	for nt in dna:
		if nt == 'a':
			nt = 'T'
		if nt == 't':
			nt = 'A'
		if nt == 'c':
			nt = 'G'
		if nt == 'g':
			nt = 'C'
	newSequence += nt
	newRevSeq = newSequence[::-1]
	newRevSeq = newRevSeq.lower()
	return newRevSeq

# Alignment Scorer
def ScoreAlign(dna1, dna2, scoreValue):
	score = 0
	if len(dna1) == len(dna2):
		for nt in dna1:
			count = 0
			if dna1[count] == dna2[count]:
				score += scoreValue
			if dna1[count] != dna2[count]:
				score -= scoreValue
			count += 1
	else: print("No can do")
	return score

# Gathering reverse complements
RevCSeq1 = revComp(sequence1)
RevCSeq2 = revComp(sequence2)

# Scores
StdScore = ScoreAlign(sequence1, sequence2, scoreValue)
Rev1Score = ScoreAlign(RevCSeq1, sequence2, scoreValue)
Rev2Score = ScoreAlign(sequence1, RevCSeq2, scoreValue)
RevBothScore = ScoreAlign(RevCSeq1, RevCSeq2, scoreValue)

# Getting the highest score and its alignment
maxScore = max(StdScore, Rev1Score, Rev2Score, RevBothScore)
if maxScore == StdScore:
	BestAlign = sequence1+'\n'+sequence2
if maxScore == Rev1Score:
	BestAlign = RevCSeq1+'\n'+sequence2
if maxScore == Rev2Score:
	BestAlign = sequence2+'\n'+RevCSeq2
if maxScore == RevBothScore:
	BestAlign = RevCSeq1+'\n'+RevCSeq2

# Printing
print('The best score is {}\nThe best alignment is\n {}'.format(maxScore, BestAlign))
 
