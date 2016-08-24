__author__ = 'lixin77'

import random
import numpy as np
import time

def INNER_PRODUCT(L_A, L_B):
    return sum([L_A[i] * L_B[i] for i in xrange(len(L_A))])


int_list_A = [random.randint(1, 10) for i in xrange(10000000)]
int_list_B = [random.randint(1, 10) for i in xrange(10000000)]

int_ndarray_A = np.array(int_list_A)
int_ndarray_B = np.array(int_list_B)

N = 20

methods = {0: INNER_PRODUCT, 1: np.dot}

data = {0: (int_list_A, int_list_B), 1: (int_ndarray_A, int_ndarray_B)}

method_name = {0: 'built-in', 1: 'np.dot'}

ds_name = {0: 'list', 1: 'np.ndarray'}

time_cost = np.zeros((len(methods), len(data)))

assert INNER_PRODUCT(int_list_A, int_list_B) == np.dot(int_ndarray_A, int_ndarray_B)

for i in xrange(N):
    for j in xrange(len(methods)):
        f = methods[j]
        for k in xrange(len(data)):
            (A, B) = data[k]
            start_time = time.time()
            res = f(A, B)
            cost = time.time() - start_time
            time_cost[j][k] += cost

for j in xrange(len(methods)):
    m_name = method_name[j]
    for k in xrange(len(data)):
        d_name = ds_name[k]
        print "%s+%s: %s seconds" % (m_name, d_name, time_cost[j][k] / N)


