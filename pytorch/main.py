import torch
import numpy as np

np_data = np.arange(6).reshape((2, 3))
# 将numpy数据转化为torch数据
torch_data = torch.from_numpy(np_data)
# 将torch数据转化为numpy数据
tensor2array = torch_data.numpy()

print(
    '\n数据转换:\n',
    '\nnumpy array:\n', np_data,          # [[0 1 2], [3 4 5]]
    '\ntorch tensor:\n', torch_data,      # 0  1  2 \n 3  4  5    [torch.LongTensor of size 2x3]
    '\ntensor to array:\n', tensor2array, # [[0 1 2], [3 4 5]]
)

# 演示矩阵相乘
data = [[1, 2], [3, 4]]
tensor = torch.FloatTensor(data)  # 将data转换成32位浮点数tensor
# data = np.array(data)

print(
    '\nmatrix multiplication (matmul):',
    '\nnumpy: \n', np.matmul(data, data),     # [[7, 10], [15, 22]]
    '\ntorch: \n', torch.mm(tensor, tensor)   # [[7, 10], [15, 22]]
)
