import matplotlib.pyplot as pt
import numpy as np

# import matplotlib
# print(matplotlib.__file__)

pt.rcParams['font.sans-serif']=['SimHei']
pt.rcParams['axes.unicode_minus']=False

data = []
temprature = []
month = ["JAN","FEB","MAR","APR","MAY","JUN","JUL","AUG","SEP","OCT","NOV","DEC"]

def main():

	target_file = 'climate.txt'
	with open(target_file, 'r', encoding='utf-8') as fp:
		raw_data = fp.readlines()

	for p in raw_data:
		data.append(p.rstrip('\n').split('\t'))


def menu():

	cnt = 1
	for a in data:
		if cnt % 5 == 0:
			print("{:>2}:{:<6}\t".format(cnt,a[0]),end="")
			cnt += 1
			print()
		else:
			print("{:>2}:{:<6}\t".format(cnt,a[0]),end="")
			cnt += 1
	print("------------------------------------------------------------")


def input_it():


	while True:
		menu()
		task = int(input('請輸入地區編號一至十二，輸入0即可結束\n'))

		if task == 0:
			print("再會")
			break

		ans = 0
		for i in range(1,13):
			print("{}: 第{}月均溫:{:>6s}度".format(data[task-1][0],i,data[task-1][i]) )
			ans = ans + float(data[task-1][i])
			temprature.append(float(data[task-1][i]))


		print("{}: 本年度年均溫為{}度".format(data[task-1][0],ans/12))

		ind = np.arange(12)
		pt.subplot(111)
		pt.barh(ind, temprature)
		pt.yticks(ind, month)
		pt.title(data[task-1][0])
		pt.show()
		temprature.clear()


if __name__=='__main__':
	main()
	input_it()

