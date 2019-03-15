def main():
	strr = 'The International Conference on Digital Information Processing, Data Mining, and Wireless Communications'
	strr = strr.lower()
	arr = list(strr)
	had = []


	for i in arr:
		if i not in had:
			had.append(i)

	print("有{}種不同字母".format(len(had)))

	for j in had:
		print("{}有{}個".format(j,arr.count(j)))


if __name__ == "__main__":
	main()