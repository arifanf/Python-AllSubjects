from sys import argv

def main():
	n=int(input())
	if((n<5) or (n>17)):
		benar=True
	else:
		benar=False
	print("{}<5 atau {}>17 {}\n".format(n,n,benar))

if __name__ == '__main__':
	main()