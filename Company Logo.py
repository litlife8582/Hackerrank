import math
import os
import random
import re
import sys
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    # Using list comprehension to generate the required coordinates
    coordinates = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if (i + j + k) != n]

    print(coordinates)