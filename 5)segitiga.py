# 5) SEGITIGA
def nama():
    print(31*'~')
    print("| Nama  : Arifa Nurul Fadlila |")
    print("| NIM   : A11.2019.12160      |")
    print("| Kelas : A11.4113            |")
    print(31*'~')

def segitiga():
	print("VALIDASI KETEPATAN SISI SUATU SEGITIGA")
	a=0;b=0;c=0
	print("\nFormat Sisi Segitiga : a,b,c")
	print("dengan syarat bilangan yang dimasukkan : a<b<c")
	print("Example : 3,4,5")
	a,b,c=list(map(int, input("\nMasukkan bilangan riil : ").split(',')))
	if ((a+b>c) and (a+c>b) and (b+c>a)):
		print(" MUNGKIN DAPAT MEMBENTUK SEGITIGA")
		if a**2+b**2==c**2:
			print(20*'-')
			print("| TERMASUK SEGITIGA SIKU-SIKU |")
			print(20*'-')
		elif a**2+b**2>c**2:
			print(20*'-')
			print("| TERMASUK SEGITIGA LANCIP |")
			print(20*'-')
		elif a**2+b**2<c**2:
			print(20*'=')
			print("TERMASUK SEGITIGA TUMPUL")
			print(20*'=')
	else:
		print(31*'-')
		print(" TIDAK MUNGKIN DAPAT MEMBENTUK SEGITIGA ")
		print(31*'-')

def main():
	nama()
	i = 1
	while i < 3:
		print(30*'=')
		print("Daftar pilihan : ")
		print("1. Validasi Segitiga Berdasarkan Sisi-sisinya ")
		print("2. Exit")
		a = input("\nPilih Program(1-2) : ")
		if a == "1":
			segitiga()
		elif a == "2":
			exit()
if __name__ == '__main__':
	main()