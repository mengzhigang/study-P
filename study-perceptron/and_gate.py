##简单的逻辑电路--与门
import numpy

def andGate(x1,x2):
    x = numpy.array([x1, x2])
    w = numpy.array([0.5,0.5])
    b = -0.7
    y = numpy.sum(x*w) + b
    if y < 0:
        return 0
    else:
        return 1

# result =andGate(1,1)
# print(result)
