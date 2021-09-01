from sys import argv

def main():
	n=int(input())
	if((n>2) and (n<=5) or (n<=15) and (n<27)):
		benar=True
	else:
		benar=False
	print("Interval 2<={}<5 atau Interval 15<={}<27  {}\n".format(n,n,benar))

if __name__ == '__main__':
	main()