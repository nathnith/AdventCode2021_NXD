# clouds in lines
# 1,1 -> 1,3
# covers 1,1 1,2 & 1,2
# 9,7 -> 7,7 covers 9,7 8,7 7,7
# only horizontal and vertical lines
# x1,y1 -> x2,y2

# . no line, number = number of lines
# determine number of points with 2 or higher

import numpy as np
f = open('Input5_small.txt', 'r')
num_lines = sum(1 for line in f)
print(num_lines)

np.matlib.empty(1000,1000)