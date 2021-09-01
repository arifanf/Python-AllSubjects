def main():
	i=0
	n=int(input("input bil : "))
	while n!= 9999:
		print(n)
		i+=n
		n=int(input("Input bil : "))
	print("Jumlah input bilangan : {}".format(i))
if __name__ == '__main__':
	main()