import matplotlib.pyplot as pt
import numpy as np

# 開關檔案
with open('popu.txt', 'r') as fp:
	populations = fp.readlines()

# print(populations)

city = list()
popu = list()

## first
for p in populations:
	# rstrip(右邊換行去掉)
	cc, pp = p.rstrip('\n').split(',')
	city.append(cc)
	popu.append(int(pp))

ind = np.arange(len(city))


# bar 直方圖
# barh 橫方圖


pt.bar(ind, popu)

# 單位
pt.xticks(ind, city)
pt.title('Program 02')
pt.show()

