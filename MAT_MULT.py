__author__ = 'lixin77'

import random
import math
import numpy as np
import time

int_list_2d_A = [[random.randint(1, 10) for j in xrange(1000)] for i in xrange(1000)]
int_list_2d_B = [[random.randint(1, 10) for j in xrange(1000)] for i in xrange(1000)]

int_ndarray_2d_A = np.array(int_list_2d_A)
int_ndarray_2d_B = np.array(int_list_2d_B)

def MAT_MULT(MAT_A, MAT_B):
    p, q, n = len(MAT_A), len(MAT_B[0]), len(MAT_B)
    res = []
    for i in xrange(p):
        tmp = []
        for j in xrange(q):
            c = 0
            for k in xrange(n):
                c += MAT_A[i][k] * MAT_B[k][j]
            tmp.append(c)
        res.append(tmp)
    return res

def validate(LIST, NDARRAY):
    res = True
    height, width = NDARRAY.shape
    for i in xrange(height):
        for j in xrange(width):
            if LIST[i][j] != NDARRAY[i][j]:
                res = False
                break
        if not res:
            break
    return res

print 'begin testing...'

assert validate(LIST=MAT_MULT(MAT_A=int_list_2d_A, MAT_B=int_list_2d_B), NDARRAY=np.dot(int_ndarray_2d_A, int_ndarray_2d_B))

print 'pass the result validation!'

methods = {0: MAT_MULT, 1: np.dot}

ds = {0: (int_list_2d_A, int_list_2d_B), 1: (int_ndarray_2d_A, int_ndarray_2d_B)}

method_name = {0: 'built-in', 1: 'np'}

d_name = {0: 'list', 1: 'np.ndarray'}

N = 20

time_cost = np.zeros((len(method_name), len(d_name)))

for i in xrange(20):
    for j in xrange(len(methods)):
        f = methods[j]
        for k in xrange(len(ds)):
            A, B = ds[k]
            beg = time.time()
            res = f(A, B)
            cost = time.time() - beg
            time_cost[j][k] += cost

for j in xrange(len(methods)):
    m_name = method_name[j]
    for k in xrange(len(ds)):
        name = d_name[k]
        print '%s+%s: %s seconds' % (m_name, name, time_cost[j][k] / N)