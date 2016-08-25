__author__ = 'lixin77'

import time
import numpy as np
import random
from test_module import test

def SUM(L):
    count = 0
    for ele in L:
        count += ele
    return count

int_list = [random.randint(1, 10) for i in xrange(10000000)]
int_ndarray = np.array(int_list)

N = 20

methods = {0: SUM, 1: sum, 2: np.sum}

d = {0: int_list, 1: int_ndarray}

method_names = {0: 'self implementation', 1: 'built-in', 2: 'np.sum'}

dt_name = {0: 'list', 1: 'np.ndarray'}

test(methods=methods, method_names=method_names, data=d, data_type=dt_name, n_iter=N)




