def main():
	mini=None
	maxi=None
	n=None
	while True:
		n=[int(x) for x in input("Masukkan nilai : ").split()]
		if n[0]==-99:
			break
		else:
			if maxi is None or maxi<n:
				maxi = n
			if mini is None or mini>n:
				mini = n
			print("---> {}".format(n))
	print("Max: {}".format(maxi))
	print("Min: {}".format(mini))
if __name__ == '__main__':
	main()