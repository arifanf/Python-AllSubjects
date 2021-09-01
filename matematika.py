nama = input(" masukkan nama anda = ")
matkul = input(" mata kuliah anda? = ")
nilai_akhir = float(input(" nilai akhir anda = "))

if(nilai_akhir >= 70 and nilai_akhir <= 100 ):
	print(" Selamat {} ! anda lulus mata kuliah {} ".format(nama,matkul))
else :
	print(" Maaf {} Silahkan mengulagi lagi mata kuliah {}".format(nama,matkul))