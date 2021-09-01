import math
def max2(a,b):
	if a>b:
		return a
	else:
		return b

def max3(a,b,c):
	if max2(a,b)>c:
		return max2(a,b)
	else:
		return c

def max4(a,b,c,d):
	if max3(a,b,c)>d:
		return max3(a,b,c)
	else:
		return d

def IsGanjil(n):
	if n%2!=0:
		return True
	else:
		return False

def IsPrima(n):
	if n>1:
		for x in range(2,n):
			if n%x==0:
				return False
				break
			else:
				return True
				break
		else:
			return True
	return

def NumOfPrima(n):
	count = 2
	text=""
	while True:
		isprime = True
		for x in range(2,int(math.sqrt(count) + 1)):
			if count%x==0:
				isprime = False
				break
		if count>=n:
			break
		if isprime:
			text=text+str(count)+" "
		count+=1
	return text

def Pangkat(basis,eksp):
	pangkat=basis**eksp 
	return pangkat

def SumOfN(N):
	sumData=0
	for i in range(0,N+1):
		sumData+=i
	return sumData

def ProductOfN (N):
	kali=1
	for num in range(1,N+1,1):
		kali = kali*num
	return kali

def AveSumOfN (N):
	sum=0
	for num in range(1,N+1,1):
		sum = sum+num
		average = sum/N
	return average

def AveProdOfN (N):
	kali=1
	for num in range(1,N+1,1):
		kali = kali*num
		average = kali/N
	return average

def FPB (x,y):
	if x > y:
		terkecil = y
	else:
		terkecil = x
	for i in range(1, terkecil+1):
		if((x % i == 0) and (y % i == 0)):
			fpb = i
	return fpb

def C2F (C):
	f=((9/5)*C)+32
	return f

def F2C (F):
	c=((5/9)*F)-32
	return c

def C2R (C):
	R=(4/5)*C
	return R

def R2C (R):
	C=(5/4)*R
	return C

def Cel2Cal(Cal):
	C=Cal+273
	return C

def Cal2Cel(C):
	Cal=C-273
	return Cal

def R2F(R):
	F=((9/4)*R)+32
	return F

def F2R(F):
	R=((4/9)*(F-32))
	return R