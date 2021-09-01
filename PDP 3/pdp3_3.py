from sys import argv

def main():
	if len(argv)<3 :
		print("usage: python pdp3_3 <arg_list+>")
	else:
		data=map(float, argv[1].split())
		#(2.5 5)
		a=2.5
		t=2.5
		L=1/2*a*t
		print("Luas Segitiga alas 2.5 dan tinggi 2.5 = {}".format(L))

if __name__ == '__main__':
	main()