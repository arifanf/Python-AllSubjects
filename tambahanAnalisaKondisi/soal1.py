def main():
	n=list(map(int, input().split(',')))
	if n[0]==13:
		print("0")
	elif n[1]==13:
		print(n[0])
	elif n[2]==13:
		print(n[0]+n[1])
	else:
		print(n[0]+n[1]+n[2])
if __name__ == '__main__':
	main()