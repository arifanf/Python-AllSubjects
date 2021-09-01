from math import *

def panjang(data):
	count=0
	if data==None:
		return count
	else:
		for i in data:
			count+=1
		return count

def BacaTabelInt():
	d=[0]*int(input("Panjang Tabel Integer : "))
	if panjang(d)>20:
		d=d[:20]
	return d

def BacaTabelFloat():
	flt=[0.0]*int(input("Panjang Tabel Float : "))
	if panjang()>20:
		flt=flt[:20]
	return flt

def BacaTabelChar():
	ch=["0"]*int(input("Panjang Tabel Integer : "))
	if panjang(ch)>20:
		ch=ch[:20]
	return ch

def TulisTabelData(data):
	ln=panjang(data)
	if ln<1:
		print('{}')
	else:
		print('{',end="")
		for i in data:
			if 0<ln-1 :
				print(i,",",end="")
			else:
				print(i,end="")
			ln-=1
		print("}")

def CariElm(data,elm):
	found=None
	for e in data:
		if e == elm:
			found=e
			break
	return found

def CariIdx(data,elm):
	found=None
	for i in range(panjang(data)):
		if data[i] == elm:
			found=i
			break
	return found

def CariBool(data,elm):
	found=False
	for i in range(panjang(data)):
		if data[i] == elm:
			found=True
			break
	return found
