def main():
	#multiple input
	#print("m.V : ", end="")
	# massa = [int(a) for a in input().split()]
	# kecepatan = [int(a) for a in input().split()]
	#m=100kg
	#V=(15i+60j-2k)m/s
	m=int(input('m = '))
	V=input('V = ')

	m=100
	V=(15+60-2)
	P=m*V
	print("Momentum = {}".format(P))
	#print("i+j-k")
if __name__ == '__main__':
	main()