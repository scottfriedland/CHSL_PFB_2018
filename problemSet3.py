#!/usr/bin/env python3
import sys

#Program to do stuff to strings

DNA = sys.argv[1] #take in a string from stdin

#Return the length of the string
length_of_DNA = len(DNA)
print("Your DNA is", length_of_DNA, "nucelotides long!")

#counting the number of each nucelotide
numberAs = DNA.count('A') + DNA.count('a')
numberTs = DNA.count('T') + DNA.count('t')
numberGs = DNA.count('G') + DNA.count('g')
numberCs = DNA.count('C') + DNA.count('c')

print("Your DNA has,", numberAs, "As", numberTs, "Ts", numberGs, "Gs and", numberCs, "Cs\n...\n")

#converting DNA to RNA
RNA = DNA.replace('T','U')
RNAlowCase = RNA.replace('t','u')
print("Your RNA sequence is", RNAlowCase, "\n...\n")

#counting the number of each nucelotide
RnumberAs = RNAlowCase.count('A') + RNAlowCase.count('a')
RnumberTs = RNAlowCase.count('T') + RNAlowCase.count('t')
RnumberGs = RNAlowCase.count('G') + RNAlowCase.count('g')
RnumberCs = RNAlowCase.count('C') + RNAlowCase.count('c')
RnumberUs = RNAlowCase.count('U') + RNAlowCase.count('u')

print("Your RNA has,", RnumberAs, "As", RnumberTs, "Ts", RnumberGs, "Gs", RnumberUs, "Us and", numberCs, "Cs\n...\n")

#Calculating AT content
AT_total = numberAs + numberTs
AT_content = AT_total / length_of_DNA
GC_content = 1-AT_content
print("Your AT content is", AT_content, "and your GC content is", GC_content, "\n..\n")

#Extracting a substring
start_slice = int( sys.argv[2] ) #Get user start cut
start_slice_act = start_slice -  1 # Subtract 1 to match python indices
end_slice = int( sys.argv[3] ) # Get user end cut
end_slice_act = end_slice - 1 # Subtract 1 to match python indices
print("Slicing your DNA from", start_slice, "to", end_slice) # Tell user how you're slicing their DNA

sub_DNA = DNA[start_slice_act:end_slice_act] # Make substring of DNA, based on specified slices
print("Your new slice of DNA is:", sub_DNA, "\n...\n") 

# Gettin dem G's
subNumberGs = sub_DNA.count('G') + sub_DNA.count('g')
print("Your slice of DNA has", subNumberGs, "Gs")

#Reverse complementing e..g you're ugly

