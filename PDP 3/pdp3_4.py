from sys import argv

def main():
	if len(argv)<3 :
		print("usage: python pdp3_4 <arg_list+>")
	else:
		data=map(float, argv[1].split())
		#(7.5 8.3)
		p=data[0]
		l=data[1]
		L=p*l
		print("Luas persegi 7.5 X 8.3 = {}".format(L))

if __name__ == '__main__':
	main()