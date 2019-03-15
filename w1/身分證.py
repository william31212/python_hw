
def main(checker):

	str = checker
	cnt = 0
	dict = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,'G': 16, 'H': 17, 'I': 34, 'J': 18, 'K': 19, 'L': 20, 'M':21, 'N': 22, 'O': 35, 'P': 23, 'Q': 24, 'R': 25, 'S': 26, 'T': 27, 'U': 28, 'V': 29, 'W': 32, 'X': 30, 'Y': 31, 'Z': 33}
	if str[0] >= 'A' and str[0] <= 'Z':
		cnt += int(dict[str[0]] / 10) * 1
		cnt += int(dict[str[0]] % 10) * 9
		for i in range (1,9):
			cnt += int(str[i]) * 9-i


		ans = cnt % 10
		checker	= int(str[9])
		ans = 10 - ans
		if ans == checker:
			print("VAILD\n")
		else:
			print("NOT VAILD\n")

	else:
		print("NOT VAILD\n")

if __name__ == "__main__":
	main("A123456789")