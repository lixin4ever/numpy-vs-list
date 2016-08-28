__author__ = 'lixin77'

import random
import math
import numpy as np
from test_module import test

int_list_2d_A = [[random.randint(1, 10) for j in xrange(400)] for i in xrange(400)]
int_list_2d_B = [[random.randint(1, 10) for j in xrange(400)] for i in xrange(400)]

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

def MAT_MULT_ELEMENTWISE(MAT_A, MAT_B):
    p, q = len(MAT_A), len(MAT_B)
    res = []
    for i in xrange(p):
        tmp = []
        for j in xrange(q):
            tmp.append(MAT_A[i][j] * MAT_B[i][j])
        res.append(tmp)
    return res

def MAT_MULT_ELEMENTWISE_NP(MAT_A, MAT_B):
    if type(MAT_A) is list:
        MAT_A = np.array(MAT_A)
        MAT_B = np.array(MAT_B)
    return MAT_A * MAT_B

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

assert validate(LIST=MAT_MULT_ELEMENTWISE(MAT_A=int_list_2d_A, MAT_B=int_list_2d_B),
                NDARRAY=MAT_MULT_ELEMENTWISE_NP(MAT_A=int_ndarray_2d_A, MAT_B=int_ndarray_2d_B))

print 'pass the result validation!'

methods = {0: MAT_MULT_ELEMENTWISE, 1: MAT_MULT_ELEMENTWISE_NP}

data = {0: (int_list_2d_A, int_list_2d_B), 1: (int_ndarray_2d_A, int_ndarray_2d_B)}

method_names = {0: 'SELF', 1: 'np'}

dt_name = {0: 'list', 1: 'np.ndarray'}

N = 20

test(methods=methods, method_names=method_names, data=data, data_type=dt_name, n_iter=N)