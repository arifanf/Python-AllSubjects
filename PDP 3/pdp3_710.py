from sys import argv

def main():
	n=int(input())
	if((n<8) or (9<n<=15) or (21<=n<30) or (n>34)):
		benar=True
	else:
		benar=False
	print("{}<8 atau interval 9<{}<=15 atau interval 21<={}<30 atau n>34 {}\n".format(n,n,n,benar))

if __name__ == '__main__':
	main()