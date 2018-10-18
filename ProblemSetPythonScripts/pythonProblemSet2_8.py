#!/usr/bin/env python3
import sys

#Script that tells one if an number is positive or negative

#Get a number from the user and coerce to int
user_input = sys.argv[1]
user_num = int(user_input)

#Compares user input to 0 and returns pos, neg or other
if user_num >= 0 and user_num != 0:
	print('positive')
elif user_num <0:
	print('negative')
elif user_num == 0:
	print('Your number is 0, silly')

print('Now you know if your number is positive or negative')
