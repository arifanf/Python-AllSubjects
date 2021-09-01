import math
def chFirstLast(N):
	c=math.log10(N)
	c=int(c)
	last=N%10
	first=N//10**c
	a=first*10**c
	b=N%a
	num=b//10
	hasil=(last*(10**c))+(num*10)+first
	return hasil
def swapDigital(N):
	temp=""
	hasil=""
	while True:
		temp=N%10
		N//=10
		hasil+=str(temp)
		if N==0:
			break
	return hasil
def main():
	N=int(input("Bilangan Integer : "))
	print(swapDigital(N))
	print(chFirstLast(N))
if __name__ == '__main__':
	main()