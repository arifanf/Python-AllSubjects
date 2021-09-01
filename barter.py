x=int(input("Masukkan Harga Barang Bila = "))
a=int(input("Masukkan Harga Barang Indah = "))

print(">>>KESIMPULAN<<<")
print("Harga Barang Dian = {} poin".format(x))
print("Harga Barang Dian = {} poin".format(a))
if x<a:
	print("Tukarlah Barang Bila dengan Barang Indah, Karena Bila akan mengalami keuntungan sebesar {} poin".format(a-x))
	#swipe di PYTHON : replace
	# x=a
	# a=b
	# b=x
	# print(x)
	# print(a)
	# print(b)
else:
	print("carilah Barang Lain saja untuk ditukar, Karena Bila akan mengalami kerugian sebesar {} poin".format(x-a))