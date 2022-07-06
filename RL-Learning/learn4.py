#coding=utf-8
#蒙特卡罗方法计算圆周率
import random,math,time
start_time = time.perf_counter()
s = 1000*1000
hits = 0
for i in range(s):
    x = random.random()
    y = random.random()
    z = math.sqrt(x**2+y**2)
    if z<=1:
        hits +=1

PI = 4*(hits/s)
print(PI)
end_time = time.perf_counter()
print("{:.2f}S".format(end_time-start_time))
