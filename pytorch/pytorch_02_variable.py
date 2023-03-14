import torch
from torch.autograd import Variable  # torch中Variable 模块

tensor = torch.FloatTensor([[1, 2], [3, 4]])
# 把鸡蛋放到篮子里, requires_grad是参不参与误差反向传播, 要不要计算梯度
variable = Variable(tensor, requires_grad=True)

print(tensor)
print(variable)
# 到这里还看不出什么区别

# 我们再对比一下 tensor 的计算和 variable 的计算.
t_out = torch.mean(tensor*tensor)       # x^2
v_out = torch.mean(variable*variable)   # x^2
print(t_out)
print(v_out)    # 7.5


