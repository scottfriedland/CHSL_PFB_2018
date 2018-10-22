#!/usr/bin/env Python

dict1 = {}
dict1['key1'] = 'val1'
print(dict1)


dict2 = {}
key = 0
val = 0
for i in range(10):
	dict2['key'+str(key)]='val'+str(val)
	key += 1
	val += 1
print(dict2)

