#!/usr/bin/env python3
import sys

# Doin things with strings
species = 'sapiens, erectus, neaderthalesis'
print(species)
speciesList = species.split(',')
print(speciesList)
speciesList.sort()
print(speciesList)

sortSpList = sorted(speciesList, key=len)
print(sortSpList)

