def main():
	sums=0
	n=int(input("Berapa jumlah list? "))
	for a in range(0,n):
		sum=0
		plus=0
		print("Daftar ke-{}".format(a+1))
		m=int(input("Berapa jumlah item? "))
		for y in range(0,m):
			z=int(input("x ? "))
			sum=sum+z
			plus+=1
		sum=sum/plus
		sums=sums+sum
		print("Rata-rata = {}".format(sum))
	print("Total rata = {}".format(sums))
if __name__ == '__main__':
	main()