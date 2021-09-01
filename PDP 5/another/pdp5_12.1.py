def main():
	while True:
		print("Konversi Temperature : ")
		print("1. Celcius ke Fahrenheit : ")
		print("2. Fahrenheit ke Celcius : ")
		t=input("pilih program(1-2): ")
		if t=="1":
			for x in range(0,101):
				f=(x*(9/5))+32 
				print("{} ---> {:.2f}".format(x,f))
		elif t=="2":
			for y in range(0,101):
				c=(y-32)*(5/9)
				print("{} ---> {:.2f}".format(y,c))
		break
if __name__ == '__main__':
	main()