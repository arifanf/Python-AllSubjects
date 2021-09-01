def main():
	f=0;c=0
	for x in range(0,101):
		f=(x*(9/5))+32 
		# or c==(x-32)*(5/9)
		# print("C ---> F")
		print("{} ---> {:.2f}".format(x,f))
if __name__ == '__main__':
	main()