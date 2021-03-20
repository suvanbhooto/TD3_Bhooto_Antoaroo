#!/usr/bin/env python

def mul_num(a,b):
	product=a*b;
	return product;
	
def main():
	import sys
	print(sys.argv)
	i=(len(sys.argv)-1)
	print(i)
	
	if (i==0):
		n1=int(input("inserer le premier argument : "))
		n2=int(input("inserer le deuxieme argument : "))
		x = int (n1)
		y = int (n2)
		print(mul_num(x,y))
	elif (i==1):
		n1=int(input("inserer le deuxieme argument : "))
		x = int (sys.argv[1])
		y = int (n1)
		print(mul_num(x,y))
	elif (i==2):
		x = int (sys.argv[1])
		y = int (sys.argv[2])
		print(mul_num(x,y))
	else:
		print("erreur : veuillez insererque deux arguements")
main()
		
		

