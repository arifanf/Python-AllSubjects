def main():
	n=list(map(int, input().split(',')))
	if (n[1] or n[2])<=1:
		if abs(n[2]==n[0]-n[1] or n[1]==n[0]-n[2]):
			print("True")
		else:
			print("False")
	elif (abs(n[1]-n[2] or n[0]-n[2] or n[0]-n[1] or n[2]-n[1]))>=2:
		print("True")
	else:
		print("False")
if __name__ == '__main__':
	main()