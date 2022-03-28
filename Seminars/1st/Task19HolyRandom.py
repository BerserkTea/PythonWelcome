# 19.Реализовать алгоритм задания случайных чисел. Без использования встроенного генератора псевдослучайных чисел

from io import SEEK_CUR
from random import shuffle
import time

def holy_random (start, stop):
    sequence = [items for items in range(start, stop + 1)]
    seconds = str(time.time())
    print(seconds)
    print(len(seconds))
    print(int(seconds[len(seconds)-(len(str(stop))-1): ]))
    index = int(seconds[len(seconds)-(len(str(stop))-1): ])
    # print(seconds[len(seconds)])
    print (sequence)
    shuffle (sequence)
    print (sequence)
    return sequence[index]


print (holy_random(1, 1000))