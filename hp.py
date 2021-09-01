namahp = str(input(" masukkan nama HP = "))
harga  = int(input(" masukkan harganya = "))

if(harga>5000000):
 	print("hp spek high-end")
elif(harga>=2000000 and harga<=4000000):
	print("hp spek high-mid")
elif(harga<1000000):
	print("hp spek low-end")
else:
	print(" tidak terdefinisi")