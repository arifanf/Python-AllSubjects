def main():
	# input : 3 4 5
	a=0
	b=0
	c=0
	a,b,c=list(map(int, input("Masukkan 3 bilangan integer : ").split()))
	if a==b or a==c or b==c :
		print("ADA")
	else:
		print("TIDAK ADA")
if __name__ == '__main__':
	main()