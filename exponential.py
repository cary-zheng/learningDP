import numpy as np
import random
import math


def exp_mech(stat,epsilon,sensitivity):
    quality = list(stat.values())
    items = list(stat.keys())
    n = len(items)
    expo_list = []
    sum = 0.0
    sum_exp = 0.0
    j = 0

    for i in range(n):
        expo = math.exp(0.5 * quality[i] * epsilon / sensitivity)
        expo_list.append(expo)
        sum = sum + expo

    for i in range(n):
        expo_list[i] = expo_list[i] / sum
        
    r = random.random()

    while True:
        sum_exp = sum_exp + expo_list[j]
        if(sum_exp > r):
            return items[j]
        j += 1

        
if __name__ =='__main__':
    stat = {"Football":1.,"Baseball":3.,"Basketball":5.,"Tennis":7.,"Soccer":9.}
    epsilon = 1.
    sensitivity = 1.
    result = exp_mech(stat,epsilon,sensitivity)
    print('the output under the Exponential Mechnaism: ' + result)

    
        
        
