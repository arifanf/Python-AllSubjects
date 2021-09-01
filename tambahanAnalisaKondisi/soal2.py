def main():
	n=list(map(int, input().split(',')))
	if n[0]==n[1]==n[2]:
		print("0")
	elif n[0]==n[1]:
		print(n[2])
	elif n[0]==n[2]:
		print(n[1])
	elif n[1]==n[2]:
		print(n[0])
	else:
		print(n[0]+n[1]+n[2])
if __name__ == '__main__':
	main()
