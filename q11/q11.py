#!/usr/bin/env python

arr = [61,61,61,80,66,64,64,76,75,120,77,102,107,100,70,112,75,108,68,108,108,97,122]
string = ""
for i in range(1,20):
	for ch in arr:
		string += chr(ch+i)
	print(string)
	string = ""
	for ch in arr:
		string += chr(ch-i)
	print(string)
	string = ""