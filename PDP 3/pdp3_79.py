from sys import argv

def main():
	n=int(input())
	if((n<8) or (9<n<=15) or (21<=n<33)):
		benar=True
	else:
		benar=False
	print("{}<8 atau interval 9<{}<=15 atau interval 21<={}<33 {}\n".format(n,n,n,benar))

if __name__ == '__main__':
	main()