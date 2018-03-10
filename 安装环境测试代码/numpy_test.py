# encoding=utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def main():
    lst = [[1, 3, 5], [2, 4, 6]]
    print(type(lst))
    np_lst = np.array(lst)
    print(type(np_lst))
    np_lst = np.array(lst, dtype=np.float)
    # bool,int,int8,int16,int32,int64,int128,uint8,uint16,uint32,uint64,uint128,float,float16,float32,float64,
    # complex64,complex128
    print(np_lst.shape)
    print(np_lst.ndim)
    print(np_lst.dtype)
    print(np_lst.itemsize)
    print(np_lst.size)
    # Some Arrays
    print(np.zeros([2, 4]))
    print(np.ones([3, 5]))
    print("Rand:")
    print(np.random.rand(2, 4))
    print(np.random.rand())
    print("Randint:")
    print(np.random.randint(1, 10))
    print("Randn:")
    print(np.random.randn(2, 4))
    print("Choice:")
    print(np.random.choice([10, 20, 30]))


if __name__ == "__main__":
    main()
