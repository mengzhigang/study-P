import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread

#生成数据
#x = np.arange(0, 6, 0.1)
#y1 = np.sin(x)
#y2 = np.cos(x)
#plt.plot(x, y1)
#plt.plot(x, y2)
#plt.xlabel("x")
#plt.ylabel("y")
#plt.title("sin & cos")
#plt.legend()
#plt.show()

img = imread("D:/test_image/image_new1.png")
plt.imshow(img)

plt.show()





