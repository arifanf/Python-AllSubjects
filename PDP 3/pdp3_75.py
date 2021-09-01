from sys import argv

def main():
	n=int(input())
	if((n>=5) and (n<25)):
		benar=True
	else:
		benar=False
	print("Interval 5<={}<25 {}\n".format(n,benar))

if __name__ == '__main__':
	main()