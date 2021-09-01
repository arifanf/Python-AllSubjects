#input
x=3
y=3.5
nama="DOSCOM"

#output
 #type
print(x)
print(y)
print(nama)
print("Nilai x = {}".format(x))
print("Nilai x = ",str(x))
print("Nilai y = "+str(y))
print("Starting %s"%(nama))
    #%s : Untuk type string
    #%f : Untuk type float
    #%i : Untuk type integer
print("Hello",nama)

 #operator
print("Nilai x = {0}, Nilai y = {1}, Nilai x + y = {2}".format(x,y,x+y))
 
  #luas segitiga
alas=5
tinggi=6
luas=(alas*tinggi)/2
print("Luas Segitiga dengan Alas {0} dan Tinggi {1} adalah {2}". format(alas,tinggi,luas))
 
  #luas lingkaran
pi=3.14
r=7
luas=pi*r*r
print("Luas Lingkaran dengan Pi {0} dan Jari-Jari {1} adalah {2}".format(pi,r,luas))

#input-output
nama=input("Masukkan Nama : ")
print("ID Name : {}".format(nama))

a=input("Masukkan Nilai a = ")
b=input("Masukkan Nilai b = ")
print("Nilai a = {}".format(a))
print("Nilai b = {}".format(b))

#type data casting
 #before
a=(input("Masukkan Nilai a (Bulat) = "))
b=(input("Masukkan Nilai b (Desimal) = "))
print("Nilai a = {0}, Nilai b = {1}, dan Nilai a + b = {2}".format(a,b,a+b))
 #after
a=int(input("Masukkan Nilai a (Bulat) = "))
b=float(input("Masukkan Nilai b (Desimal) = "))
    #Integer(int) = Integral Data Type
    #Float(float) = Decimal Data Type
print("Nilai a = {0}, Nilai b = {1}, dan Nilai a + b = {2}".format(a,b,a+b))

#multiple input
name1,name2=input("Masukkan Nama: ").split()
print("ID Name : {}".format(name1))
print("Nickname : {}".format(name2))

 #soal
name=(input("Masukkan Nama : "))
nim=(input("Masukkan NIM : "))
t=(input("Masukkan Tempat Lahir: "))
tl=(input("Masukkan Tanggal Lahir : "))
tugas=float(input("Masukkan Nilai Tugas : "))
uts=float(input("Masukkan Nilai UTS : "))
uas=float(input("Masukkan Nilai UAS : "))
akhir=float((0.4*tugas)+(0.3*uts)+(0.3*uas))
print("Nama             : {}".format(name))
print("NIM              : {}".format(nim))
print("Tempat Lahir     : {}".format(t))
print("Tanggal Lahir    : {}".format(tl))
print("Nilai Tugas      : {}".format(tugas))
print("Nilai UTS        : {}".format(uts))
print("Nilai UAS        : {}".format(uas))
print("Nilai Akhir      : {}".format(akhir))
 #soal
if akhir<=100 and akhir>=85:
    print("Grade A")
elif akhir>=75 and akhir<=84:
    print("Grade B")
elif akhir==65 and akhir<=74:
    print("Grade C")
elif akhir<=64:
    print("Grade D")
else:
    print("Nilai tidak memenuhi standar")

#boolean type data
nilai1=5<6
nilai2=5>6
nama="DOSCOM"=="doscom"
print(nilai1)
print(nilai2)
print(nama)

#if-else condition
i=5
j=3
print("Nilai i = {0} dan Nilai j = {1}".format(i,j))
if i<j:
    print("Nilai i kurang dari j")
elif i>j:
    print("Nilai i lebih dari j")
else:
    print("Nilai i sama dengan j")
i=3
j=5
print("Nilai i = {0} dan Nilai j = {1}".format(i,j))
if i<j:
    print("Nilai i kurang dari j")
elif i>j:
    print("Nilai i lebih dari j")
else:
    print("Nilai i sama dengan j")
i=5
j=5
print("Nilai i = {0} dan Nilai j = {1}".format(i,j))
if i<j:
    print("Nilai i kurang dari j")
elif i>j:
    print("Nilai i lebih dari j")
else:
    print("Nilai i sama dengan j")

