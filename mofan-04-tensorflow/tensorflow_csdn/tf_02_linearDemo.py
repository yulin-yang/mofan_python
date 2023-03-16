import tensorflow as tf
tf.compat.v1.disable_eager_execution()  # 保证sess.run()能够正常运行

# 使用tf.Variable()可以创建一个变量 Tensor
# 创建变量 W 和 b 节点，分别为0.1 和 -0.1
W = tf.Variable([.1], dtype=tf.float32)
b = tf.Variable([-.1], dtype=tf.float32)

# 创建 x 节点，用来输入实验中的输入数据
x = tf.compat.v1.placeholder(tf.float32)
# 创建线性模型
linear_model = W*x + b

# 创建 y 节点，用来输入实验中得到的输出数据，用于损失模型计算
y = tf.compat.v1.placeholder(tf.float32)
# 创建损失模型
loss = tf.reduce_sum(tf.square(linear_model - y))

# 创建 Session 用来计算模型
sess = tf.compat.v1.Session()

""""
    通过tf.Variable()创建变量 Tensor 时需要设置一个初始值，但这个初始值并不能立即使用，
    例如我们如果在这里print(sess.run(W))尝试打印W的值会得到提示未初始化的异常
    变量 Tensor 需要经过下面的 init 过程后才能使用：
"""

# 初始化变量
init = tf.compat.v1.global_variables_initializer()
sess.run(init)

print(sess.run(W))
print(sess.run(linear_model, {x: [1, 2, 3, 6, 8]}))
print(sess.run(loss, {x: [1, 2, 3, 6, 8], y: [4.8, 8.5, 10.4, 21.0, 25.3]}))

"""
    TensorFlow 提供了很多优化算法来帮助我们训练模型。最简单的优化算法是梯度下降(Gradient Descent)算法，
    它通过不断的改变模型中变量的值，来找到最小损失值。如下的代码就是使用梯度下降优化算法帮助我们训练模型：
"""

# 创建一个梯度下降优化器，学习率为0.001
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.001)
train = optimizer.minimize(loss)

# 用两个数组保存训练数据
x_train = [1, 2, 3, 6, 8]
y_train = [4.8, 8.5, 10.4, 21.0, 25.3]

# 训练10000次
for i in range(10000):
    sess.run(train, {x: x_train, y: y_train})

# 打印一下训练后的结果
print('W: %s b: %s loss: %s' % (sess.run(W), sess.run(b), sess.run(loss, {x: x_train , y: y_train})))