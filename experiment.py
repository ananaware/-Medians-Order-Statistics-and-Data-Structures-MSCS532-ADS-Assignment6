import random
import time
from selection_algorithms import randomized_quickselect, deterministic_select


def run_experiment(size):

    arr = [random.randint(1, 100000) for _ in range(size)]
    k = size // 2

    arr_copy1 = arr.copy()
    arr_copy2 = arr.copy()

    start = time.time()
    randomized_quickselect(arr_copy1, k)
    random_time = time.time() - start

    start = time.time()
    deterministic_select(arr_copy2, k)
    deterministic_time = time.time() - start

    return random_time, deterministic_time


if __name__ == "__main__":

    sizes = [100, 1000, 5000, 10000]

    print("Size | Randomized Quickselect | Deterministic Select")
    print("------------------------------------------------------")

    for s in sizes:
        r, d = run_experiment(s)
        print(f"{s} | {r:.6f} seconds | {d:.6f} seconds")