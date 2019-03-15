def main():
	for i in range(1,10,1):
		for j in range(1,10,1):
			print("{:d} * {:d} = {:2d}".format(i,j,i*j))

def version2():
	for i in range(1,10,1):
		for j in range(1,10,1):
			print("{:d} * {:d} = {:2d}".format(i,j,i*j),end=" ")
			# print(str(i) + " * " + str(j) + " = " + str(i*j), end=" ")
		print()

def version3():
	for k in range(1,10,3):
		for i in range(1,10,1):
			for j in range(k,k+3,1):
				print("{:d} * {:d} = {:2d}".format(i,j,i*j),end=" ")
			print()
		print()

def interval():
	print()
	print("++++++++++++++++++++++++++++++++")
	print()


if __name__ == "__main__":
	main()
	interval()
	version2()
	interval()
	version3()
