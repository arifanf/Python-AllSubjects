import os,sys,math
# Konsep dan Skema Pengulangan
# dengan bahasa python
def main():
	n=int(input('Enter data (1<n<11): '))
	print('Skema Dengan Mark')
	print('Tanpa penanganan kasus kosong')
	i=0                                #init
	while i<n:                         #not EOP
		print('{:^3}'.format(i),end='')#current elemen
		i+=1                           #next elemen
	print()                            # terminasi
	print('Skema Dengan Mark')
	print('Dengan penanganan kasus kosong')
	if n<1 and n>10:						# penanganan
		print('n diluar range !')			# kasus kosong
	else:
		i=0									#init
		while True:
			print('{:^3}'.format(i),end='') #proses current
			i+=1							# next elemen
			if i>n-1 :						#EOP
				break
		print()								#terminasi
	
	print('Skema Tanpa Mark')
	print('Pasti tidak ada kasus kosong')
	i = -1								#init
	while True:
		i+=1							#next
		print('{:^3}'.format(i),end='') #proses
		if i>=n-1:						#EOP
			break
	print()
	print('Skema Tanpa Mark')
	print('Pasti tidak ada kasus kosong')
	i=0								#init dan First elemen
	print('{:^3}'.format(i),end='') #proses
	while i<n-1:
		i+=1
		print('{:^3}'.format(i),end='') #proses
	print()

if __name__=='__main__':
	main()