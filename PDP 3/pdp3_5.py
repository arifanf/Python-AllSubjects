from sys import argv

def main():
	if len(argv)<3 :
		print("usage: python pdp3_5 <arg_list+>")
	else:
		data=map(float, argv[1].split())
		#(5.5 2.3)
		r1=data[0]
		PI=3.14
		L1=PI*r1*r1
		r2=data[1]
		PI=3.14
		L2=PI*r2*r2
		L3=L1-L2
		print("Luas L1, r=5.5 : {:.4f}".format(L1))
		print("Luas L2, r=2.3 : {:.4f}".format(L2))
		print("Selisih L1-L2 : {:.4f}".format(L3))
if __name__ == '__main__':
	main()