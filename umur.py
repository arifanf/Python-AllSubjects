nama = str(input(" masukkan nama = "))
usia = float(input(" masukkan usianya = "))
k=""
k1="bayi"
k2="balita"
k3="balita"
k4="anakanak"
k5="remaja"
k6="pemuda"
k7="dewasa"
k8="lansia"

if(usia>0 and usia<= 1):
	k=k1
elif(usia>1 and usia<=3):
	k=k2
elif(usia>3 and usia<=5):
	k=k3
elif(usia>5 and usia<=12):
	k=k4
elif(usia>12 and usia<=17):
	k=k5
elif(usia>17 and usia<=30):
	k=k6
elif(usia>30 and usia<=60):
	k=k7
elif(usia>60 and usia<=100):
	k=k8
else:
	k="ketuaan"
print(50*"=")
print(" usia {} sekarang {} tahun kategori {}".format(nama,usia,k))
print(50*"=")
