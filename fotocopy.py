print("\tFotocopy Sultan LC")
print("\nList Harga")
while True:
	print("1) Kertas A4 70g : 200\n2) Kertas F4 70g : 220\n3) Kertas Burem  : 120 ")
	while True:
		pilih=int(input("Masukkan pilihan anda (1-3) : "))
		if pilih==1:
			harga1=200
			order=int(input("Masukkan berapa lembar = "))
			total1=order*harga1
			print("Total harga anda = {} ".format(total1))
			x=input("Apakah anda ingin menambah pesanan anda (y/n) ? ").upper()
			if x=="Y":
				break

		elif pilih==2:
			harga2=220
			order=int(input("Masukkan berapa lembar : "))
			total2=order*harga2
			print("Total harga anda = {} ".format(total2))
			x=input("Apakah anda ingin menambah pesanan anda (y/n) ? ").upper()
			if x=="Y":
				break

		elif pilih==3:
			harga3=120
			order=int(input("Masukkan berapa lembar = "))
			total3=order*harga3
			print("Total harga anda = {} ".format(total3))
			x=input("Apakah anda ingin menambah pesanan anda (y/n) ? ").upper()
			if x=="YA":
				break


		
