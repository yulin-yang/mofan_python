# 引入 tensorflow_csdn 模块
import tensorflow as tf
tf.compat.v1.disable_eager_execution()  # 保证sess.run()能够正常运行

'''
    TensorFlow 内部的计算都是基于张量的，因此我们有必要先对张量有个认识。
    张量是在我们熟悉的标量、向量之上定义的，详细的定义比较复杂，我们可以先简单的将它理解为一个多维数组：
    3                                       # 这个 0 阶张量就是标量，shape=[]
    [1., 2., 3.]                            # 这个 1 阶张量就是向量，shape=[3]
    [[1., 2., 3.], [4., 5., 6.]]            # 这个 2 阶张量就是二维数组，shape=[2, 3]
    [[[1., 2., 3.]], [[7., 8., 9.]]]        # 这个 3 阶张量就是三维数组，shape=[2, 1, 3]
    
    TensorFlow 内部使用tf.Tensor类的实例来表示张量，每个 tf.Tensor有两个属性:
        dtype : Tensor存储的数据的类型，可以为tf.float32、tf.int32、tf.string…
        shape : Tensor存储的多维数组中每个维度的数组中元素的个数，如上面例子中的shape
]
'''
# 创建一个整型常量，即 0 阶 Tensor
t0 = tf.constant(3, dtype=tf.int32)

# 创建一个浮点数的一维数组，即 1 阶 Tensor
t1 = tf.constant([3., 4.1, 5.2], dtype=tf.float32)

# 创建一个字符串的2x2数组，即 2 阶 Tensor
t2 = tf.constant([['Apple', 'Orange'], ['Potato', 'Tomato']], dtype=tf.string)

# 创建一个 2x3x1 数组，即 3 阶张量，数据类型默认为整型
t3 = tf.constant([[[5], [6], [7]], [[4], [3], [2]]])

if __name__ == '__main__':
    # 打印上面创建的几个 Tensor
    print(t0)
    print(t1)
    print(t2)
    print(t3)

    # print 一个 Tensor 只能打印出它的属性定义，并不能打印出它的值，要想查看一个 Tensor 中的值还需要经过Session 运行一下：
    sess = tf.compat.v1.Session()
    print('t0:', sess.run(t0))
    print('t1:', sess.run(t1))



