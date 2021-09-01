def main():
	#masukkan Nilai : 84
	print("Konversi Nilai")
	nilai=int(input("masukan Nilai Angka Bulat : "))
	if nilai>80:
		nhuruf="A"
	elif nilai>=61 and nilai<=80:
		nhuruf="B"
	elif nilai>=41 and nilai<=60:
		nhuruf="C"
	elif nilai>=21 and nilai<=40:
		nhuruf="D"
	elif nilai>=0 and nilai<=20:
		nhuruf="E"
	else:
		print("Nilai Tidak Memenuhi")
	print("Nilai: {}, Nilai Huruf: {}".format(nilai,nhuruf))
if __name__ == '__main__':
		main()