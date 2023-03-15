import pandas as pd

a = [1, 2, 3, 'name', True]
b = {'name': 'yyl', 'age': 23}

s_a1 = pd.Series(a)
# 自定义 index 索引
s_a2 = pd.Series(a, index=['x', 'y', 'z', 'm', 'n'], name='s_a2')
s_b1 = pd.Series(b)

if __name__ == '__main__':
    print(s_a2)
    # 根据索引值输出
    print(s_a2['y'])
    print(s_b1)
