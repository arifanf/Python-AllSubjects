def lndata(data):
	cnt=0
	if data==None:
		return cnt
	else:
		for x in data:
			cnt+=1
	return cnt

def nMutlak(n):
	if n<0:
		n*=-1
	else:
		n*=1
	return n

def moveN(A,n):
	valuelist=list()
	if n<=0:
		for y in range(n,lndata(A)+n):
			if nMutlak(n)<=lndata(A):
				valuelist.append(A[y])
			else:
				print("n melebihi jumlah indeks")
				break
		teks="ke kiri"
		if n==0:
			teks="(tetap)"
	else:
		for y in range(n,lndata(A)):
			if nMutlak(n)<lndata(A):
				valuelist.append(A[y])
			else:
				print("n melebihi jumlah indeks")
				break
		for y in range(0,n):
			if nMutlak(n)<lndata(A):
				valuelist.append(A[y])
			else:
				print("n melebihi jumlah indeks")
				break
		teks="ke kanan"
	return valuelist,n,teks

def main():
	A=list(map(int, input("Masukkan bilangan integer => ").split(",")))
	n=int(input("Bilangan digeser sebanyak => "))
	Atempo=A
	A,n,teks=moveN(A,n)
	print("Array A => {}\nDigeser sebanyak => {} {} \nHasil Array => {}".format(Atempo,nMutlak(n),teks,A))
if __name__ == '__main__':
	main()