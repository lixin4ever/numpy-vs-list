__author__ = 'lixin77'

import numpy as np
import random
import math
import time

def LOG(L):
    return [math.log(ele) for ele in L]

int_list = [random.randint(1, 10) for i in xrange(10000000)]
int_ndarray = np.array(int_list)


N = 20

methods = {0: LOG, 1: np.log}

data = {0: int_list, 1: int_ndarray}

method_name = {0: 'built-in', 1: 'np.ndarray'}

ds_name = {0: 'list', 1: 'np.ndarray'}

time_cost = np.zeros((len(method_name), len(ds_name)))

for i in xrange(N):
    for j in xrange(len(method_name)):
        f = methods[j]
        for k in xrange(len(ds_name)):
            d = data[k]
            start_time = time.time()
            res = f(d)
            t_cost = time.time() - start_time
            time_cost[j][k] += t_cost

for j in xrange(len(method_name)):
    m_name = method_name[j]
    for k in xrange(len(ds_name)):
        ds = ds_name[k]
        print '%s+%s: %s seconds' % (m_name, ds, time_cost[j][k] / N)

