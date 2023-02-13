import multiprocessing as mp
import numpy as np
import time


def model():
    return sum([((np.random.random(1000) * np.random.random(1000)).sum())**(1/2) for x in range(10000)])

if __name__ == '__main__':
    workers = 8
    t = time.time()

    with mp.Pool(workers) as pool:
        results = [pool.apply_async(model, ()) for i in range(100)]
        results_sum = sum([r.get() for r in results])

    print(f'workers: {workers}, time: {time.time() - t}')