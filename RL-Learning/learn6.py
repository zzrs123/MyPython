#coding=utf-8
import numpy as np


def buffon(a, l, n):
    xl = np.pi * np.random.random(n)
    yl = 0.5 * a * np.random.random(n)
    m = 0
    for x, y in zip(xl, yl):
        if y < 0.5 * l * np.sin(x):
            m += 1
    result = 2 * l / a * n / m
    print(f'pi的估计值是{result}')


buffon(2, 1, 100000)
