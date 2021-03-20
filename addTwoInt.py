#!/usr/bin/env python

def add_num(a,b):
	sum=a+b;
	return sum;
	
def main():
	import sys
	print(sys.argv)
	
	x = int (sys.argv[1])
	y = int (sys.argv[2])
	
	print(add_num(x,y))
	
main()
		
