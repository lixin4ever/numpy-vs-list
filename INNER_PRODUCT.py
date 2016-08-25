__author__ = 'lixin77'

import random
import numpy as np
from test_module import test

def INNER_PRODUCT(L_A, L_B):
    return sum([L_A[i] * L_B[i] for i in xrange(len(L_A))])


int_list_A = [random.randint(1, 10) for i in xrange(10000000)]
int_list_B = [random.randint(1, 10) for i in xrange(10000000)]

int_ndarray_A = np.array(int_list_A)
int_ndarray_B = np.array(int_list_B)

N = 20

methods = {0: INNER_PRODUCT, 1: np.dot}

data = {0: (int_list_A, int_list_B), 1: (int_ndarray_A, int_ndarray_B)}

method_names = {0: 'built-in', 1: 'np.dot'}

dt_name = {0: 'list', 1: 'np.ndarray'}

time_cost = np.zeros((len(methods), len(data)))

assert INNER_PRODUCT(int_list_A, int_list_B) == np.dot(int_ndarray_A, int_ndarray_B)

test(methods=methods, method_names=method_names, data=data, data_type=dt_name, n_iter=N)



