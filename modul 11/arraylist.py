
def panjang(data):
	count=0
	if data==None:
		return count
	else:
		# for i in range(0,len(data),1):
		for i in data:
			count+=1
		return count

def BacaTabelInt():
	pass
def BacaTabelFloat():
	pass
def BacaTabelChar():
	pass
def TulisTabelData(data): #string

	panjang(data)=l
	if l<1:
		print('{}')
	else:
		print('{}')
		for i in data

	
def CariElm(data,elm): #elemen(int,float,char,obj)
	found=None
	for e in range (panjang(data))
		if e==elm:
			found=e
	return found

def CariIdx(data,elm): #integer
	found=None
	for i in range (panjang(data))
		if data[i]==elm:
			found=i
	return found

def CariBool(data,elm): #boolean
	found=False
	for i in range (panjang(data))
		if data[i]==elm:
			found=True
			break
	return found