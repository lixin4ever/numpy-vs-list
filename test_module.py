__author__ = 'lixin77'

import time
import numpy as np
import random
import math

def test(methods, method_names, data, data_type, n_iter):
    """
    function to test time costs of basic operation
    :param methods: methods in the test
    :param method_names: name of the function
    :param data: data structure used in the test
    :param data_type: name of data structure
    :param n_iter: number of iterations to get the average results
    """
    time_cost = np.zeros((len(methods), len(data)))
    for i in xrange(n_iter):
        for j in xrange(len(methods)):
            f = methods[j]
            for k in xrange(len(data)):
                if type(data[k]) is tuple:
                    # binary operation
                    (A, B) = data[k]
                    start_time = time.time()
                    res = f(A, B)
                    cost = time.time() - start_time
                    time_cost[j][k] += cost
                else:
                    # unary operation
                    A = data[k]
                    start_time = time.time()
                    res = f(A)
                    #print 'result is', res
                    cost = time.time() - start_time
                    time_cost[j][k] += cost
    for j in xrange(len(methods)):
        m_name = method_names[j]
        for k in xrange(len(data)):
            d_name = data_type[k]
            print "%s+%s: %s seconds" % (m_name, d_name, time_cost[j][k] / n_iter)




