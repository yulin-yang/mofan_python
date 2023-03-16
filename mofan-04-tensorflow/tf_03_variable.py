"""
    在 Tensorflow 中，定义了某字符串是变量，它才是变量，这一点是与 Python 所不同的。
    定义语法： state = tf.Variable()
"""

import tensorflow as tf
tf.compat.v1.disable_eager_execution()

# 定义变量
state = tf.Variable(0, name='counter')

# 定义常量 one
one = tf.constant(1)

# 定义加法步骤 (注: 此步并没有直接计算)
new_value = tf.add(state, one)

# 将 State 更新成 new_value
update = tf.compat.v1.assign(state, new_value)

'''
    如果你在 Tensorflow 中设定了变量，那么初始化变量是最重要的！！
    所以定义了变量以后, 一定要定义 init = tf.initialize_all_variables() .
'''

# 如果定义 Variable, 就一定要 initialize
# init = tf.initialize_all_variables() # tf 马上就要废弃这种写法
init = tf.compat.v1.global_variables_initializer()  # 替换成这样就好

# 使用 Session
with tf.compat.v1.Session() as sess:
    sess.run(init)
    for _ in range(3):
        # 执行 update 命令，将state的值加1
        sess.run(update)
        print(sess.run(state))

