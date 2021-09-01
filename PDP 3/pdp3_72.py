from sys import argv

def main():
	n=int(input())
	if((n>=5) and (n<=6) or (n>=10)):
		benar=True
	else:
		benar=False
	print("5<={}<6 atau {}>=10 {}\n".format(n,n,benar))

if __name__ == '__main__':
	main()