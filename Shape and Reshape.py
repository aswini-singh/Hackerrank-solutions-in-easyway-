
import numpy as np


array = np.array(list(map(int, input().split())))
print(array.reshape(3, 3))

       # (or)

import numpy
ar = list(map(int,input().split()))
np_ar = numpy.array(ar)
print(numpy.reshape(np_ar,(3,3)))