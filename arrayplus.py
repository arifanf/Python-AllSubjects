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
	reverse=list()
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

	for x in range(1,len(valuelist)+1):
		reverse.append(valuelist[-x])
	return valuelist,n,teks,reverse



def main():
	A=4,5,6,7,8,9
	n=-2
	Atempo=A
	A,n,teks,reverse=moveN(A,n)
	print("Array A => {}\nDigeser sebanyak => {} {} \nHasil Array => {}".format(Atempo,nMutlak(n),teks,A))
	print(reverse)
if __name__ == '__main__':
	main()