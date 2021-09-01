from sys import argv

def main():
	n=int(input())
	if((n>3) and (n<=15) or (n>22) and (n<32)):
		benar=True
	else:
		benar=False
	print("Interval 3<{}<=15 atau Interval 22<{}<32 {}\n".format(n,n,benar))

if __name__ == '__main__':
	main()