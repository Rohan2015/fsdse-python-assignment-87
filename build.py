import pandas as pd
from random import randint


def solution(array):
    print pd.Series(data=array)
    return pd.Series(data=array)

num1 = randint(0, 100)
array = [num1]
solution(array)
