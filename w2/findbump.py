
def main():

	fp = open("bump.txt","r")
	ans = open("clock_90.txt","w")
	ans2 = open("counter_clock_90.txt","w")

	lines = fp.readlines()
	col = len(lines)
	row = len(lines[0])
	for i in range(row):
		for j in range(col-1,-1,-1):
			if lines[j][i] != '\n':
				ans.write(lines[j][i])
		ans.write('\n')
	ans.close()

	col = len(lines)
	row = len(lines[0])

	for i in range(row-1,-1,-1):
		for j in range(col):
			if lines[j][i] == '\n':
				ans2.write(" ")
			else:
				ans2.write(lines[j][i])
		ans2.write('\n')
	ans2.close()


if __name__ == "__main__":
	main()
