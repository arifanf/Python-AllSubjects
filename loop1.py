import os,sys,math
# implementasi 5 konsep pengulangan
# dengan bahasa python
def main():
	n=int(input('Enter data : '))
	print('loop berdasarkan JUMLAH pengulangan')
	for i in range(n):# pengulangan diulang sebanyak n kali
		print('{:^3}'.format(i),end='')
	print()

	print('loop berdasarkan KONDISI BERHENTI')
	i=0
	while True:
		print('{:^3}'.format(i),end='')
		i+=1
		if i==n: #kondisi berhenti
			break
	print()
	print('loop berdasarkan KONDISI PENGULANGAN')
	i=0
	while i<n: #kondisi pengulangan
		print('{:^3}'.format(i),end='')
		i+=1
	print()
	print('loop berdasarkan ANALISA 2 AKSI')
	i=0
	while True: # analisa 2 kasus
		print('{:^3}'.format(i),end='') # kasus 1
		if i==n-1 :						# kondisi berhenti
			break
		else:
			i+=1						# kasus 2
	print()
	print('loop berdasarkan ITERASI/PENCACAH')
	i=0;
	for i in range(0,n): # i melakukan traversal sepanjang 0..n
		print('{:^3}'.format(i),end='')
	print()
if __name__=='__main__':
	main()