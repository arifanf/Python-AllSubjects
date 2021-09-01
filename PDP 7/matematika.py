import math
def Max2(a,b):
	if a>b:
		print("Max ---> {} dan {} : {}".format(a,b,a))
	elif a<b:
		print("Max ---> {} dan {} : {}".format(a,b,b))
	return ""

def Max3(a,b,c):
	if a>b and a>c:
		print("Max ---> {}, {} dan {} : {}".format(a,b,c,a))
	elif a<b and b>c:
		print("Max ---> {}, {} dan {} : {}".format(a,b,c,b))
	elif a<c and b<c:
		print("Max ---> {}, {} dan {} : {}".format(a,b,c,c))
	return ""

def Max4(a,b,c,d):
	if a>b and a>c and a>d:
		print("Max ---> {}, {} , {}, dan {} : {}".format(a,b,c,d,a))
	if b>a and b>c and b>d:
		print("Max ---> {}, {} , {} ,dan {} : {}".format(a,b,c,d,b))
	if c>a and c>b and c>d:
		print("Max ---> {}, {} , {} ,dan {} : {}".format(a,b,c,d,c))
	if d>a and d>b and d>c:
		print("Max ---> {}, {} , {} ,dan {} : {}".format(a,b,c,d,d))
	return ""

def IsGanjil(n):
	if n%2!=0:
		print("IsGanjil {} : True".format(n))
	else:
		print("IsGanjil {} : False".format(n))
	return ""

def IsPrima(n):
	if n>1:
		for x in range(2,n):
			if n%x==0:
				print("IsPrima {} : False".format(n))
				break
			else:
				print("IsPrima {} : True".format(n))
				break
		else:
			print("IsPrima {} : True".format(n))
	return ""

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

def function():
	print("hello")

def Pangkat(basis,eksp):
	pangkat=basis**eksp 
	return pangkat,basis,eksp

def SumOfN(N):
	sumData=0
	for i in range(0,N+1):
		sumData+=i
	return sumData
