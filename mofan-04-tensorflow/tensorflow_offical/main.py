'''
    tensorflow官网教程
'''

import tensorflow as tf

'''加载数据集'''
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0

''' 构建机器学习模型 '''
# 通过堆叠层来构建 tf.keras.Sequential 模型。
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])

# 对于每个样本，模型都会返回一个包含 logits 或 log-odds 分数的向量，每个类一个。
predictions = model(x_train[:1]).numpy()
print(predictions)

# tf.nn.softmax 函数将这些 logits 转换为每个类的概率：
tf.nn.softmax(predictions).numpy()

# 使用 losses.SparseCategoricalCrossentropy 为训练定义损失函数，它会接受 logits 向量和 True 索引，并为每个样本返回一个标量损失。
loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)

# 这个未经训练的模型给出的概率接近随机（每个类为 1/10），因此初始损失应该接近 -tf.math.log(1/10) ~= 2.3。
loss_fn(y_train[:1], predictions).numpy()

# 在开始训练之前，使用 Keras Model.compile 配置和编译模型。
# 将 optimizer 类设置为 adam，将 loss 设置为您之前定义的 loss_fn 函数，并通过将 metrics 参数设置为 accuracy 来指定要为模型评估的指标。
model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])
'''训练并评估模型'''
# 使用 Model.fit 方法调整您的模型参数并最小化损失：
model.fit(x_train, y_train, epochs=5)

# Model.evaluate 方法通常在 "Validation-set" 或 "Test-set" 上检查模型性能。
model.evaluate(x_test,  y_test, verbose=2)



