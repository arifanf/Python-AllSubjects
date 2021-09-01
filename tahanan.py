
def nama():
    print(31*'~')
    print("| Nama  : Arifa Nurul Fadlila |")
    print("| NIM   : A11.2019.12160      |")
    print("| Kelas : A11.4113            |")
    print(31*'~')

resistor=0;r=00
def seri():
	print("\nRangkaian Seri")
	print("Format : x,y,z")
	print("Example : 1,2,3")
	r1=list(map(float,  input("Masukkan muatan resistor : ").split(',')))
	if r1[0]<0 or r1[1]<0 or r1[2]<0:
		print("Error : Cannot defined negative")
	else:
		print("\nDiketahui r1 = {}".format(r1[0]))
		print("          r2 = {}".format(r1[1]))
		print("          r3= {}".format(r1[2]))

		seri=r1[0]+r1[1]+r1[2]
		print("Hasil muatan yang diperoleh adalah {} Ω".format(seri))

def paralel():
	print("\nRangkaian Paralel")
	print("Format : x,y,z")
	print("Example : 1,2,3")
	r2=list(map(float,  input("Masukkan muatan resistor : ").split(',')))
	if r2[0]<=0 or r2[1]<=0 or r2[2]<=0:
		print("Error : Cannot defined zero and negative")
	else:
		print("\nDiketahui r1 = {}".format(r2[0]))
		print("          r2 = {}".format(r2[1]))
		print("          r3 = {}".format(r2[2]))

		paralel=(r2[0]*r2[1]*r2[2])/((r2[1]*r2[2])+(r2[0]*r2[2])+(r2[0]*r2[1]))
		print("Hasil muatan yang diperoleh adalah {} Ω".format(paralel))

def main():
	nama()
	while True:
		print("Kalkulator Resistor")
		print("1. Seri")
		print("2. Paralel")
		print("3  Exit")
		resistor=input("Pilih program (1-3) : ")
		if resistor=="1":
			seri()
		elif resistor=="2":
			paralel()
		elif resistor=="3":
			exit()
		else:
			print("Error : Input Invalid")

if __name__ == '__main__':
	main()