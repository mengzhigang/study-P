#多层感知机实现异或
from and_gate import andGate
from nand_gate import nandGate
from or_gate import orGate

def xorGate(x1,x2):
    s1 = nandGate(x1, x2)
    s2 = orGate(x1, x2)
    y = andGate(s1, s2)
    return y

result = xorGate(0, 0)
print(result)
result = xorGate(0, 1)
print(result)
result = xorGate(1, 0)
print(result)
result = xorGate(1, 1)
print(result)
