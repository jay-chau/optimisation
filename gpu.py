from numba import njit
import numpy as np
import time

def model():
    number = 0.0
    for i in range(2500):
        number += np.sqrt((np.random.random(1000)* np.random.random(1000)).sum())
    return number

@njit()
def modelJit():
    number = 0.0
    for i in range(2500):
        number += np.sqrt((np.random.random(1000)* np.random.random(1000)).sum())
    return number

if __name__ == '__main__':
    for m in [model, modelJit]:
        t = time.time()
        results = [m() for i in range(1000)]
        print(f'{m.__name__}, time: {time.time() - t}')

## To consider:
    # Eager Compilation, specifying types in function
    # Compilation time when running functions on the same dataset.
    # Vectorising
    # Parallel & "fastmath", nogil, caching