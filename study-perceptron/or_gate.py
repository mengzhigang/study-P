#与门
import numpy as np

def orGate(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.3
    y =  np.sum(x*w) + b
    if y > 0:
        return 1
    else:
        return 0

# result = orGate(0, 0)
# print(result)
# result = orGate(0, 1)
# print(result)
# result = orGate(1, 0)
# print(result)
# result = orGate(1, 1)
# print(result)

