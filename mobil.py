nama= input("masukkan nama pembeli = ")
alamat= input(" masukkan nama alamat = ")
notelp= int(input(" masukkan notelp = "))

print("\n jenis mobil yang ingin dibeli")
print("\t1. DAIHATSU")
print("\t2. HONDA")
print("\t3. TOYOTA")
pilihan =input (" pilih program (1-3) = ")
if pilihan =="1":
	print("a. Grand New Xenia")
	print("b. All New Terios")
	print("c. New Ayla")
	pilihan1=input("mana yang anda pilih??")
	if pilihan1=="a":
		print(" harga mobil Grand New Xenia adalah 183 juta")
	elif pilihan1=="b":
		print(" harga mobil All New Terios adalah 215 juta")
	elif pilihan1=="c":
		print(" harga mobil New Ayla adalah 110 juta")
	else:
		print(" eror ")
elif pilihan=="2":
	print("a. Honda Brio Satya")
	print("b. Honda Jazz")
	print("c. Honda Brio")
	pilihan2=input("mana yang anda pilih??")
	if pilihan2=="a":
		print(" harga mobil Honda Brio Satya adalah 131 juta")
	elif pilihan2=="b":
		print(" harga mobil Honda Jazz adalah 232 juta")
	elif pilihan2=="c":
		print(" harga mobil Honda Brio adalah 189 juta")
	else:
		print(" eror ")
elif pilihan=="3":
	print("a. Alphard")
	print("b. Camry")
	print("c. Fortuner")
	pilihan3=input("mana yang anda pilih??")
	if pilihan3=="a":
		print(" harga mobil Alphard adalah 870 juta")
	elif pilihan3=="b":
		print(" harga mobil Camry adalah 560 juta")
	elif pilihan3=="c":
		print(" harga mobil Fortuner adalah 492 juta")
	else:
		print(" eror ")
		

