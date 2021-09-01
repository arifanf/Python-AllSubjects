def satu(n):
	nNext=n
	while True:
		n=nNext%10
		if n==1:
			return True
		nNext=nNext//10
		if nNext<1:
			return False

def faktor(n):
	nNext=n
	while True:
		num=nNext%10
		if num==0:
			return False
		elif n%num=0:
			return False
		nNext//=10
		if nNext<1:
			return True

def akhir1(a,b):
	a%=10
	b%=10
	if a==b:
		return True
	else:
		return False

def akhir2(a,b,p):
	n=10**p
	a%=n
	b%=n
	if a==b:
		return True
	else:
		return False