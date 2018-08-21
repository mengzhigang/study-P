##与非门
import numpy as np

def nandGate(x1,x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7
    y = np.sum(x*w) + b
    if y <= 0:
        return 1
    else:
        return 0

# result = nandGate(0, 0)
# print(result)
# result = nandGate(0, 1)
# print(result)
# result = nandGate(1, 0)
# print(result)
# result = nandGate(1, 1)
# print(result)

