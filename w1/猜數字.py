import random

minnum = 0
maxnum = 99
target = random.randint(0, 100)
print(target)

cnt = 0
while True:
	cnt += 1
	num = int(input("輸入"+ str(minnum) +"~" + str(maxnum) + '\n'))

	if num > target:
		maxnum  = num-1
		print("輸入小一點")
	elif num < target:
		minnum  = num-1
		print("輸入大一點")
	else:
		print("猜中了耶耶耶~~~~~~ ，你輸入了" + str(cnt) + "次")
		break

