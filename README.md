## Numpy-vs-list
Some scripts to compare time cost of basic operation on python built-in list and that on numpy.ndarray. 

## Settings
* Interpreter: Python 2.7.12 (64 bits)
* Data: 10 million integers ranging from 1 to 10 (1-d list / array) and 400 x 400 integers ranging from 1 to 10 (2-d list / array, i.e, matrix), where elements in them are all generated randomly. 
* Results: operation is peroformed `N` times and results is the average time cost of the `N` executions. 

## Operationg system and cpu information
* OS X 10.10: Intel Core I5-4260U (1.4 GHz)
* Windows 7: Intel Core I5-4570 (3.2 GHz) 
* Red Hat 6.4: Intel Xeon E5-2650 (2.6 GHz)

## Time costs

#### SUM operation on 1-d array / list 
OS | `SELF+list` | `SELF+np.ndarray` | `built-in+list` | `built-in+np.ndarray` | `np+list` | `np+np.ndarray`
--- | --- | --- | --- | --- | --- | ---
OS X | 2.002 | 3.059 | 0.079 | 1.225 | 0.606 | **0.008**
Windows | 0.279 | 0.982 | 0.046 | 0.759 | 0.392 | **0.005**
Red Hat | 0.297 | 1.415 | 0.056 | 1.004 | 0.497 | **0.007**

#### LOG operation on 1-d array / list
OS | `built-in+list` | `built-in+np.ndarray` | `np+list` | `np+np.ndarray`
--- | --- | --- | --- | ---
OS X | 3.730 | 4.775 | 0.841 | **0.137**
Windows | 1.674 | 2.143 | 0.566 | **0.118**
Red Hat | 2.935 | 3.431 | 1.115 | **0.460**

#### INNER PRODUCT operation on 1-d array / list
OS | `built-in+list` | `built-in+np.ndarray` | `np+list` | `np+np.ndarray`
--- | --- | --- | --- | ---
OS X | 3.167 | 6.027 | 1.187 | **0.013**
Windows | 0.881 | 2.800 | 0.806 | **0.009**
Red Hat | 1.101 | 3.941 | 1.211 | **0.017**

#### MATRIX MULTIPLICATION operation on 2-d list / ndarray
OS | `SELF+list` | `SELF+np.ndarray` | `np+list` | `np+np.ndarray`
--- | --- | --- | --- | ---
OS X | 32.753 | 69.669 | 0.114 | **0.095**
Windows | 5.935 | 31.011 | 0.057 | **0.045**
Red Hat | 10.877 | 42.495 | 0.0117 | **0.093**

#### MATRIX MULTIPLICATION (elmentwise) operation on 2-d list / ndarray
OS | `SELF+list` | `SELF+np.ndarray` | `np+list` | `np+np.ndarray`
--- | --- | --- | --- | ---
OS X | 0.094 | 0.197 | 0.020 | **0.0004**
Windows | 5.935 | 31.011 | 0.057 | **0.045**
Red Hat | 10.877 | 42.495 | 0.0117 | **0.093**

Note: `A+B` in the above form means applying methods `A` on the data structure `B`; unit in the form is second


