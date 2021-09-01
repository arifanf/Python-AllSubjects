from sys import argv

def main():
	if len(argv)<2 :
		print("usage: python pdp3_2 <arg_list+>")
	else:
		data=map(float, argv[1].split())
		#(23.5)
		r=23.5
		PI=3.14
		L=PI*r**2
		print("Luas Lingkaran jari-jari 23.5 adalah : {}".format(L))

if __name__ == '__main__':
	main()