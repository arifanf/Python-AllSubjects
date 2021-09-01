from math import *
def panjang(data):#integer
	count=0
	if data == None:
		return count
	else:
		for i in data:
			count+=1
		return count
def BacaTabelInt():#data
	data=[0]*int(input("Panjang Tabel Int :"))
	if panjang(data)>20:
		data=data[:20]
	return data
def BacaTabelFloat():
	data=[0.0]*int(input("Panjang Tabel Float :"))
	if panjang(data)>20:
		data=data[:20]
	return data
def BacaTabelChar():
	data=["0"]*int(input("Panjang Tabel Int :"))
	if panjang(data)>20:
		data=data[:20]
	return data
def TulisTabelData(data):#string
	pass
	#jika data kosong outputnya {}
	#jika data isi format outputnya ={x1......}
	l=panjang(data)
	if l<1:
		print('{}')
	else:
		print('{',end="")
		for i in data:
			if 0<l-1 :
				print(i,",",end="")
			else:
				print(i,end="")
			l-=1
		print("}")
def CariElm(data,elm):#elemen
	found=None
	for e in data:
		if e == elm:
			found=e
			break
	return found

def CariIdx(data,elm):#integer
	found=None
	for i in range(panjang(data)):
		if data[i] == elm:
			found=i
			break
	return found

def CariBool(data,elm):#boolean
	found=False
	for i in range(panjang(data)):
		if data[i] == elm:
			found=True
			break
	return found
