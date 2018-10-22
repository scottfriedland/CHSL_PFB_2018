#!/usr/bin/env python3

line_count = 0
char_count = 0
ave_lineLen = 0
with open('Python_06.fastq','r') as file_object:
	for line in file_object:
		line = line.rstrip()
		line_count += 1
		char_count += len(line)
		ave_lineLen = (char_count/line_count)
print('Line count is:', line_count)
print('Total character count is:', char_count)
print('Average line length is:', ave_lineLen)

