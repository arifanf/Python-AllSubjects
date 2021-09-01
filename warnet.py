while True:# a=0
	print("Pilih Menu")
	print("1. Member")
	print("2. Reguler")
	pilih=int(input("Masukkan pilihan anda : "))

	while True:
		if pilih==1:
			x=input("Apakah anda punya voucher (Yy/Nn)? ").upper()
			if x=="Y":
				v=input("Masukkan kode voucher anda : ").upper()
				if v=='PALUGADA':
					harga1=3000
					harga2=2000
					n=int(input("Berapa jam anda menggunakan billing? "))
					if n==1:
						dis=(10/100)*n
						bayar=n-dis
						print("Anda harus membayar = Rp{:.0f}".format(bayar))
					elif n>1:
						a=n-1
						b=(a*harga2)+harga1
						dis=(10/100)*b
						bayar=b-dis
						print("Anda harus membayar = Rp{:.0f}".format(bayar))
				else:
					print("Kode Voucher anda salah")
			else:
				harga1=3000
				harga2=2000
				n=int(input("Berapa jam anda menggunakan billing? "))
				if n==1:
					dis=(10/100)*n
					print("Anda harus membayar = Rp{:.0f}".format(dis))
				elif n>1:
					a=n-1
					b=(a*harga2)+harga1
					print("Anda harus membayar = Rp{:.0f}\n".format(b))
					break

		elif pilih==2:
			harga1=5000
			harga2=4000
			n=int(input("Berapa jam anda menggunakan billing? "))
			if n==1:
				print("Anda harus membayar = Rp{}".format(harga1))
			elif n>1:
				a=n-1; 
				b=(a*harga2)+harga1
				print("Anda harus membayar = Rp{}".format(b))

		else:
			exit()
