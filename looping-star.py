# n=int(input("Masukkan Batas = "))
# for x in range(1,n+1):
# 	for y in range(1,x+1):
# 		print("*",end="")
# 	print()

# n=int(input("Masukkan batas : "))
# for x in range(n+1):
# 	print("*"*1)

for row in range(6):
	for col in range(7):
		if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row+col==8):
			print("*",end="")
		else:
			print(" ",end="")
	print()
