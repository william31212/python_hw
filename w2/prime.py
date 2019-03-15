import time


def main():

	print("顯示a~b所有質數")
	a = int(input("請輸入a:"))
	b = int(input("請輸入b:"))
	print("建表O(nlog(n)):")


	if a > b:
		a,b = b,a



	t0 = time.clock()
	build(int(b+5),a,b)
	print("花費時間:"  + str(time.clock() - t0))

	print("建表O(n):")
	t0 = time.clock()
	linear(int(b+5),a,b)
	print("花費時間:"  + str(time.clock() - t0))

	print("建表O(n^2):")
	t0 = time.clock()
	basic(a,b)
	print("花費時間:"  + str(time.clock() - t0))

def build(n,a,b):
	table = [True] * (n+1)
	table[1] = False
	for i in range(2,int(n),1):
		if table[i]:
			for j in range(i*i,n,i):
				table[j] = False

	for x in range(2,int(n)+1,1):
		if x >= int(a) and x <= int(b):
			if table[x]:
				print("{}到{}之間的質數有{}".format(a,b,x))

def linear(n,a,b):

	table = [False] * (n+1)
	check = []

	table[0] = table[1] = True

	for i in range(2,int(n)):
		if table[i] == False:
			check.append(i)
		for j in check:
			if (i * j >= int(n)):
				break
			table[i * j] = True
			if (i % j == 0):
				break

	for x in range(a,b):
		if table[x] == False:
			print("{}到{}之間的質數有{}".format(a,b,x))

def basic(a,b):

	ans = []
	for i in range(int(a),int(b)):
		flag = 0
		if i == 0 or i == 1:
			continue
		for j in range(2,i-1):
			if i % j == 0:
				flag = 1
				break
		if flag == 0:
			ans.append(i)

	for j in ans:
		print("{}到{}之間的質數有{}".format(a,b,j))


if __name__ == "__main__":
	main()


