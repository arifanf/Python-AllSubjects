def main():
	data=enumerate(range(100,0,-1),start=1)
	for x in data:
		print("i-%s dan j-%s"%(x[0],x[1]))
if __name__ == '__main__':
	main()