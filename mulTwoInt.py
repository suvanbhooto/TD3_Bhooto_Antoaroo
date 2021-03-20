#!/usr/bin/env python

def mul_num(a,b):
	mul=a*b;
	return mul
	
def main():
	import sys
	print(sys.argv)
	
	x = int(sys.argv[1])
	y = int(sys.argv[2])
	
	print (mul_num(x,y))
main()
