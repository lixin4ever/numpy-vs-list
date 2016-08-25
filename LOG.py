__author__ = 'lixin77'

import numpy as np
import random
import math
from test_module import test

def LOG(L):
    return [math.log(ele) for ele in L]

int_list = [random.randint(1, 10) for i in xrange(10000000)]

int_ndarray = np.array(int_list)


N = 20

methods = {0: LOG, 1: np.log}

data = {0: int_list, 1: int_ndarray}

method_names = {0: 'built-in', 1: 'np.log'}

dt_name = {0: 'list', 1: 'np.ndarray'}

test(methods=methods, method_names=method_names, data=data, data_type=dt_name, n_iter=N)



