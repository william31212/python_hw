import matplotlib.pyplot as pt
import numpy as np

with open('popu.txt', 'r') as fp:
	populations = fp.readlines()

print(populations)

city = list()
popu = list()

for p in populations:
	cc, pp = p.rstrip('\n').split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city)//4)
# print(ind)

lenCity1= int(len(city)/4)
lenCity2= lenCity1 * 2
lenCity3= lenCity1 * 3


popu1=[]
city1=[]
for i in range(lenCity1):
	popu1.append(popu[i])
	city1.append(city[i])

popu2=[]
city2=[]
for i in range(lenCity1):
	popu2.append(popu[lenCity1+i])
	city2.append(city[lenCity1+i])

popu3=[]
city3=[]
for i in range(lenCity1):
	popu3.append(popu[lenCity2+i])
	city3.append(city[lenCity2+i])

popu4=[]
city4=[]
for i in range(lenCity1):
	popu4.append(popu[lenCity3+i])
	city4.append(city[lenCity3+i])

print(popu4)
print(popu3)
print(popu2)
print(popu1)
pt.subplot(112)
pt.bar(ind, popu1)
pt.xticks(ind, city1)
pt.title('city1')

pt.subplot(212)
pt.bar(ind, popu2)
pt.xticks(ind, city2)
pt.title('city2')

pt.subplot(122)
pt.bar(ind, popu3)
pt.xticks(ind, city3)
pt.title('city3')

pt.subplot(221)
pt.bar(ind, popu4)
pt.xticks(ind, city4)
pt.title('city4')

pt.show()
