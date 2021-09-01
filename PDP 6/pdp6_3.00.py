def main():
	lagi=None
	n=int(input("Jumlah Analisa : "))
	y=0
	for i in range(1,n+1):
		print("{} + {} = ? ".format(i,i), end='')
		jawab=int(input())
		if jawab==i+i:
			print("Benar")
		else:
			print("Salah")
			print("Coba Lagi.")
			Benar=False
			while y in range(0,4) and not Benar:
				print("{} + {} = ? ".format(i,i))
				jawab=int(input())
				if jawab == i+i :
					print("Benar!")
					Benar=True
					y+=0
			if not Benar:
				print("Jawabannya adalah {}.".format(i+i))
	print("== Analisa ==  \nJumlah Analisa = {}\nAnalisa Benar = {}\nAnalisa Salah = {}".format(n,n-y,y))
if __name__ == '__main__':
	main()