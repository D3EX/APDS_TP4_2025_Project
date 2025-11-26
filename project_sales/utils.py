# utils.py
import numpy as np

def generate_random_sales(min_val: int, max_val: int, size: int, seed: int = None) -> np.ndarray:
    if seed is not None:
        np.random.seed(seed)
    # numpy.randint upper bound exclusive -> +1
    return np.random.randint(min_val, max_val + 1, size=size)
