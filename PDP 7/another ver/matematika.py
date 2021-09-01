import math
def Max2(a,b):
	if a>b:
		print("Max2 --> {} dan {}	= {}".format(a,b,a))
	elif a<b:
		print("Max2 --> {} dan {}	= {}".format(a,b,b))

def Max3(a,b,c):
	if a>b and a>c:
		print("Max3 --> {}, {}, dan {}	= {}".format(a,b,c,a))
	elif b>a and b>c: 
		print("Max3 --> {}, {}, dan {}	= {}".format(a,b,c,b))
	elif c>a and c>b:
		print("Max3 --> {}, {}, dan {}	= {}".format(a,b,c,c))

def Max4(a,b,c,d):
	if a>b and a>c and a>d:
		print("Max3 --> {}, {}, {}, {}	= {}".format(a,b,c,d,a))
	elif b>a and b>c and b>d: 
		print("Max3 --> {}, {}, {}, {}	= {}".format(a,b,c,d,b))
	elif c>a and c>b and c>d:
		print("Max3 --> {}, {}, {}, {}	= {}".format(a,b,c,d,c))
	elif d>a and d>b and d>c:
		print("Max3 --> {}, {}, {}, {}	= {}".format(a,b,c,d,d))

def IsGanjil(n):
	if n%2!=0:
		print("IsGanjil {}		= True".format(n))
	else:
		print("IsGanjil {}		= False".format(n))

def IsPrima(a):
	if a>1:
		for x in range(2,a):
			if a%x==0:
				print("IsPrima {}		= Bukan Prima".format(a))
				break
			else:
				print("IsPrima {}		= Prima".format(a))
				break
		else:
			print("IsPrima {}		= Prima".format(a))

def NumOfPrima (b):
	lower=2
	while True:
		isprima = True
		for x in range(2, int(math.sqrt(lower)+1)):
			if lower%x==0:
				isprima=False
				break
		if lower>b:
			break
		if isprima:
			print(lower,end=" ")
		lower+=1

def Pangkat (basis,eksp):
	c=basis**eksp
	print("\nPangkat ({},{})		= {}".format(basis,eksp,c))

def SumOfN (N):
	sum=0
	for num in range(0,N+1,1):
		sum = sum+num
	print("SumOfN ({})		= {}".format(N,sum))

def ProductOfN (N):
	kali=1
	for num in range(1,N+1,1):
		kali = kali*num
	print("ProductOfN ({})		= {}".format(N,kali))

def AveSumOfN (N):
	sum=0
	for num in range(1,N+1,1):
		sum = sum+num
		average = sum/N
	print("AveSumOfN ({})		= {}".format(N,average))

def AveProdOfN (N):
	kali=1
	for num in range(1,N+1,1):
		kali = kali*num
		average = kali/N
	print("AveProdOfN ({})		= {}".format(N,average))

def FPB (x,y):
	if x > y:
		smaller = y
	else:
		smaller = x
	for i in range(1, smaller+1):
		if((x % i == 0) and (y % i == 0)):
			fpb = i
	print("FPB ({},{})		= {}".format(x,y,fpb))

def C2F (C):
	f=((9/5)*C)+32
	print("{} C adalah {} F".format(C,f))

def F2C (F):
	c=((5/9)*F)-32
	print("{} F adalah {} C".format(F,c))

def C2R (C):
	R=(4/5)*C
	print("{} C adalah {} R".format(C,R))

def R2C (R):
	C=(5/4)*R
	print("{} R adalah {} C".format(R,C))

def Cel2Cal(Cal):
	C=Cal+273
	print("{} C adalah {} R".format(Cal,C))

def Cal2Cel(C):
	Cal=C-273
	print("{} C adalah {} R".format(C,Cal))

def R2F(R):
	F=((9/4)*R)+32
	print("{} R adalah {} F".format(R,F))

def F2R(F):
	R=((4/9)*F)-32
	print("{} R adalah {} F".format(F,R))