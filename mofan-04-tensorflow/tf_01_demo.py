import tensorflow_csdn as tf
import numpy as np
tf.compat.v1.disable_eager_execution()

# create data
x_data = np.random.rand(100).astype(np.float32)
y_data = x_data*0.1 + 0.3

Weights = tf.Variable(tf.random.uniform([1], -1.0, 1.0))
biases = tf.Variable(tf.zeros([1]))

y = Weights*x_data + biases

# 计算误差
loss = tf.reduce_mean(tf.square(y-y_data))

# 传播误差
optimizer = tf.compat.v1.train.GradientDescentOptimizer(0.5)

train = optimizer.minimize(loss)

init = tf.compat.v1.global_variables_initializer()  # 替换成这样就好

sess = tf.compat.v1.Session()
sess.run(init)

for step in range(201):
    sess.run(train)
    if step % 20 == 0:
        print(step, sess.run(Weights), sess.run(biases))

sess.close()