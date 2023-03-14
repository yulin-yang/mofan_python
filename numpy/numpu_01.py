import numpy as np

# 实现矩阵相乘的两种方式
a = np.array([[1, 2], [3, 4]])
b = np.array([[1, 2], [3, 4]])

print(np.dot(a, b))
print(a.dot(b))

# 最大最小值，累加，累乘，总数
students = np.array([168, 156, 176])
print('\n最大值:', np.max(students))
print('\n最小值:', students.min())
print('\n总和:', students.sum())
print('\n累乘:', students.prod())
print('\n总个数:', students.size)
print('\n均值:', students.mean())
print('\n中位数:', np.median(students))
print('\n标准差:', np.std(students))


