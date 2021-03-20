#!/usr/bin/env python

def mul_num(a,b):
	product=a*b;
	return product;
	
def main():
	import sys
	print(sys.argv)
	i=(len(sys.argv)-1)
	print(i)
	
	if (i==2):
		x = int(sys.argv[1])
		y = int(sys.argv[2])
		print (mul_num(x,y))
	else :
		print("error : only two argumentsare allowed")
	
main()
