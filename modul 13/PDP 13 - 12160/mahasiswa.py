from math import *

class Mahasiswa():
	"""docstring for Mahasiswa"""
	def __init__(self, nim=None, nama=None, ipk=0.0):
		self.nim = nim
		self.nama = nama
		self.ipk = ipk

def panjang(m):
	cnt=0
	for i in m:
		cnt=cnt+1
	return cnt

def isEmpty(m):
	if m==None or (nim==None and nama==None and ipk==0.0):
		return True

def setNim(m,newnim):
	Mhs=Mahasiswa()
	Mhs.nim=newnim

def setNama(m,newnama):
	Mhs=Mahasiswa()
	Mhs.nim=newnama

def setIpk(m,newipk):
	Mhs=Mahasiswa()
	Mhs.nim=newipk

def getNim(m):
	return m.nim

def getNama(m):
	return m.nama

def getIpk(m):
	return m.ipk

def BacaData():
	m=Mahasiswa
	nama,nim,ipk=[str(x) for x in input().split('')]
	Mhs.nim=nim
	Mhs.nama=nama
	Mhs.ipk=ipk
	return Mhs.nim,Mhs.nama,Mhs.ipk

def TulisData(m):
	if m!=None:
		Mhs=Mahasiswa()
		Mhs.nim=m.nim
		Mhs.nama=m.nama
		Mhs.ipk=m.ipk
		print(Mhs.nim,Mhs.nama,Mhs.ipk)
	else:
		print("Tidak Ada")

def printList(data):
	for elmn in data:
		TulisData(elmn)

def Sorting(m,idx):
	if idx==0:
		for i in range(panjang(m)-1):
			minim=i
			for j in range(i+1,panjang(m)):
				if m[j].nim<m[minim].nim:
					minim=j
			temp=m[i]
			m[i]=m[minim]
			m[minim]=temp
		for a in range(panjang(m)):
			print(m[a].nim,m[a].nama,m[a].ipk)

	elif idx==1:
		for i in range(panjang(m)-1):
			minim=i
			for j in range(i+1,panjang(m)):
				if m[j].nama<m[minim].nama:
					minim=j
			temp=m[i]
			m[i]=m[minim]
			m[minim]=temp
		for a in range(panjang(m)):
			print(m[a].nama,m[a].nim,m[a].ipk)

	elif idx==2:
		for i in range(panjang(m)-1):
			minim=i
			for j in range(i+1,panjang(m)):
				if m[j].ipk<m[minim].ipk:
					minim=j
			temp=m[i]
			m[i]=m[minim]
			m[minim]=temp
		for a in range(panjang(m)):
			print(m[a].ipk,m[a].nim,m[a].nama)
	else:
		print("Index Tidak Terdaftar (0/1/2)")

def Searching1(listm,nim_find):
	# found= m for m in listm
	# 	if m.nim==nim_find
	# return found

	idx=-1
	for i in range(panjang(listm)):
		if listm[i].nim==nim_find:
			idx=1
			break
	if idx<0:
		return None
	else:
		return listm[idx]

def Searching2(listm,nim):
	idx=-1
	for i in range(panjang(listm)):
		if listm[i].nim==nim:
			idx=1
			break
	return idx