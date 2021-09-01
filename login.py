def main():

	print("Pendaftaran")
	nama=input("Masukkan Nama = ")
	email=input("Masukkan Email Pendafaran = ")
	passwd=input("Masukkan Password Pendaftaran = ")
	print(">>>Yeeeeayy. Akun dengan nama {} berhasil didaftarkan<<<".format(nama))
	# print(">>>Yeeeeayy. Akun dengan nama %s berhasil didaftarkan<<<"%nama)

	print("\nNote :")
	print("1. Y/y untuk Yes")
	print("2. N/n untuk No")
	n=input("Apakah anda ingin Login? ").upper()
	if n=="Y":
		a=input("\nMasukkan Email = ")
		b=input("Masukkan Password = ")
		if a==email and b==passwd:
			print("\n>>>Selamat {}, Anda berhasil Login<<<".format(nama))
			# print("\n>>>Selamat %s, Anda berhasil Login<<<"%nama)	
		else:
			print("Maaf, Email Atau Password tidak sesuai")
	else:
		print("Sampai Jumpa~")
		# exit()
if __name__ == '__main__':
	main()