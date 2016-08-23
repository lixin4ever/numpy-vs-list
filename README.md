## Numpy-vs-list
Some scripts to compare time cost of basic operation on python built-in list and that on numpy.ndarray. 

## Interpreter
Python 2.7.12 (64 bits)

## Operationg system and cpu information
* OS X 10.10: Intel Core I5-4260U (1.4 GHz)
* Windows 7: Intel Core I5-4570 (3.2 GHz) 
* Red Hat 6.4: Intel Xeon E5-2650 (2.6 GHz)

## Experiment results

### SUM operation on one-dimensional array (list)
OS | `SELF+list` | `SELF+np.ndarray` | `built-in+list` | `built-in+np.ndarray` | `np+list` | `np+np.ndarray`
--- | --- | --- | --- | --- | --- | ---
OS X | 1.867 | 2.844 | 0.079 | 1.148 | 0.560 | 0.037

Note: `A+B` in the above form means applying methods `A` on the data structure `B`


