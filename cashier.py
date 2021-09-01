kembalian=0
kurang=0
print(">>>Selamat Datang di Cafein<<<")
print("Silahkan masukkan data untuk memesan kopi")
nama=input("Masukkan Nama Anda = ")
email=input("Masukkan Email Anda = ")
print("\nMenu")
print("1. Vietnam Drip @15k")
print("2. Espresso @25k")
print("3. Caffe Latte @30k")
choice=int(input("Masukkan pilihan anda = "))

if choice==1:
	product=("Vietnam Drip")
	harga=15000
	print("\nNote")
	print("1. Y/y untuk Yes")
	print("2. N/n untuk No")
	n=input("Apakah anda yakin ingin memesan {}, dengan harga Rp.{} ??? ".format(product,harga)).upper()
	if n=="Y":
		x=int(input("Masukkan uang anda = Rp."))
		if x>=harga:
			kembalian=x-harga
			print("\t\n>>> Anda Berhasil Memesan {} dengan harga Rp.{}, kembalian anda Rp.{} <<<".format(product,harga,kembalian))
		elif x<harga:
			kurang=harga-x
			print("\n>>> Maaf uang anda kurang = Rp{} <<<".format(kurang))
	else:
		print("\t\n>>> Silahkan membeli dilain waktu~ <<<")

elif choice==2:
	product=("Espresso")
	harga=25000
	print("\nNote")
	print("1. Y/y untuk Yes")
	print("2. N/n untuk No")
	n=input("Apakah anda yakin ingin memesan {}, dengan harga Rp.{} ??? ".format(product,harga)).upper()
	if n=="Y":
		x=int(input("Masukkan uang anda = Rp."))
		if x>=harga:
			kembalian=x-harga
			print("\t\n>>> Anda Berhasil Memesan {} dengan harga Rp.{}, kembalian anda Rp.{} <<<".format(product,harga,kembalian))
		elif x<harga:
			kurang=harga-x
			print("\n>>> Maaf uang anda kurang = Rp{} <<<".format(kurang))
	else:
		print("\t\n>>> Silahkan membeli dilain waktu~ <<<")

elif choice==3:
	product=("Caffe Latte")
	harga=30000
	print("\nNote")
	print("1. Y/y untuk Yes")
	print("2. N/n untuk No")
	n=input("Apakah anda yakin ingin memesan {}, dengan harga Rp.{} ??? ".format(product,harga)).upper()
	if n=="Y":
		x=int(input("Masukkan uang anda = Rp."))
		if x>=harga:
			kembalian=x-harga
			print("\t\n>>> Anda Berhasil Memesan {} dengan harga Rp.{}, kembalian anda Rp.{} <<<".format(product,harga,kembalian))
		elif x<harga:
			kurang=harga-x
			print("\n>>> Maaf uang anda kurang = Rp{} <<<".format(kurang))
	else:
		print("\t\n>>> Silahkan membeli dilain waktu~ <<<")

print("\nNote :")
print("1. Y/y untuk Yes")
print("2. N/n untuk No")
y=input("Apakah Anda ingin Mencetak nota belanja? : ").upper()
if y=="Y":
	print("\nNama Pembeli     = {}".format(nama))
	print("Email Pembeli    = {}".format(email))
	print("Kopi yang Dibeli = {}".format(product))
	print("Harga Kopi       = {}".format(harga))
	print("Uang Pembayaran  = {}".format(x))
	print("Uang Kembalian   = {}".format(kembalian))
	print("Uang Kurang      = {}".format(kurang))
else:
	print("Terima Kasih. Silahkan Datang Kembali")
