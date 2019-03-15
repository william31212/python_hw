import time

def fib(n):
	if (n == 0 or n == 1):
		return n
	else:
		return fib(n-1) + fib(n-2)
def dp(n):
	check = [0 , 1]
	for i in range (2,n+1):
		check.append(check[i-1] + check[i-2])
	return check[n]


def main():

	n = int(input("n="))
	t0 = time.time( )
	ans = dp(n)
	print("Fib({}) = {}".format(n,ans))
	print("花費時間:"  + str(time.time( ) - t0))

	t0 = time.time( )
	ans = fib(n)
	print("花費時間:"  + str(time.time( ) - t0))
	print("Fib({}) = {}".format(n,ans))


if __name__ == "__main__":
	main()