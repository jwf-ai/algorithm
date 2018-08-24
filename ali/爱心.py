# encoding: utf-8

import random

mu1 = 0
sigma1 = 0

mu2 = 0
sigma2 = 1

count = 0

def f(x, y):
    return (x+y-1)**3 - x**2*y**3 <= 0

s = 1000000
for i in range(s):
    x = random.normalvariate(mu1,sigma1)
    y = random.normalvariate(mu2,sigma2)

    if f(x,y) == True:
        count += 1

print(round(count/s,1))

