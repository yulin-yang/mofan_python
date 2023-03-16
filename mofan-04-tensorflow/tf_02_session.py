"""
    Session 是 Tensorflow 为了控制,和输出文件的执行的语句.
    运行 session.run() 可以获得你要得知的运算结果, 或者是你所要运算的部分.
"""
import tensorflow_csdn as tf
tf.compat.v1.disable_eager_execution()

# create two matrixes
'''
[3 3] *[2 2]T
1x2 * 2x1
'''
matrix1 = tf.constant([[3, 3]])
matrix2 = tf.constant([[2], [2]])

matrix3 = tf.constant([[1, 2, 3], [4, 5, 6]])
matrix4 = tf.constant([[1, 2], [3, 4], [5, 6]])

product1 = tf.matmul(matrix1, matrix2)
product2 = tf.matmul(matrix3, matrix4)
# [12]

sess = tf.compat.v1.Session()
print(sess.run(product2))
