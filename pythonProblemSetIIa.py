#!/usr/bin/env python3
import sys

user_input = sys.argv[1]
user_num = int(user_input)

if user_num < 100:
	message = 'Your number is less than 100'
	print(message)
elif user_num > 100:
	message = 'Your number is greater than 100'
	print(message)
else:
	message = 'Your number is 100 or might be utter nonsense'
	print(message)
print('now you number how your number compares to 100')
