__author__ = 'lixin77'

import time
import numpy as np
import random

def SUM(L):
    count = 0
    for ele in L:
        count += ele
    return count

int_list = [random.randint(1, 10) for i in xrange(10000000)]
int_ndarray = np.array(int_list)

N = 20

methods = {0: SUM, 1: sum, 2: np.array}

d = {0: int_list, 1: int_ndarray}

methods_name = {0: 'self implementation', 1: 'built-in', 2: 'np.array'}

ds_name = {0: 'list', 1: 'np.ndarray'}

cost = np.zeros((len(methods), len(d)))

for i in xrange(N):
    for j in xrange(len(methods)):
        f = methods[j]
        for k in xrange(len(d)):
            data = d[k]
            start_time = time.time()
            res = f(data)
            t_cost = time.time() - start_time
            cost[j][k] += t_cost

print "Average time cost after 20 iterations:"
for j in xrange(len(methods)):
    method_name = methods_name[j]
    for k in xrange(len(ds_name)):
        print "%s+%s: %s seconds" % (method_name, ds_name[k], cost[j][k] / N)




