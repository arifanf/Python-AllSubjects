def main():
	lagi=None
	for i in range(1,12):
		print("{} + {} = ? ". format(i,i), end='')
		jawab=int(input())
		if jawab==i+i:
			print("Benar")
		else:
			print("Salah")
			print("Coba Lagi.")
			Benar=False
			while lagi in range(1,4) and not Benar:
				print("{} + {} = ? ".format(i,i))
				jawab=int(input())
				if jawab==i+i:
					print("Benar!")
					Benar=True
				lagi+=1
			if not Benar:
				print("Jawabannya adalah {}".format(i+i))
if __name__ == '__main__':
	main()