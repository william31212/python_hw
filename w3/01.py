import matplotlib.pyplot as pt

w = [1, 3, 4, 5, 9, 11]
x = [1, 2, 3, 4, 5, 6, 8, 10]
y = [20, 30, 14, 67, 42, 12, 40, 60]
z = [12, 33, 43, 22, 34, 20]


pt.plot(x, y, lw=2, label='Mary')
pt.plot(w, z, lw=2, label='Tom')
pt.xlabel('month')
pt.ylabel('dollars (million)')
pt.legend()
pt.title('Program 01')
pt.show()