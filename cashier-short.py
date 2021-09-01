print(">>>Selamat Datang di Cafein<<<")
print("Silahkan masukkan data untuk memesan kopi")
nama=input("Masukkan Nama Anda = ")
email=input("Masukkan Email Anda = ")
print("\nMenu")
print("1. Vietnam Drip @15k")
print("2. Espresso @25k")
print("3. Caffe Latte @30k")
choice=int(input("Masukkan pilihan anda = "))
print("\nNote")
	print("1. Y/y untuk Yes")
	print("2. N/n untuk No")
	n=input("Apakah anda yakin ingin memesan Vietnam Drip, dengan harga Rp.{} ??? ".format(harga)).upper()
	
if choice==1:
	product="Vietnam Drip"
	harga=15000