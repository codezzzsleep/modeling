import keras
from keras.datasets import mnist
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import RMSprop
from keras.utils import to_categorical

# 加载 MNIST 数据集
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 将数据折叠到1维结构，即 (num_samples, 784)
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# 标准化输入数据（0-255 的整数值转换为 0-1 的浮点值）
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# 将类别向量（类别标签）转换为二进制类矩阵（即 one-hot 编码）
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

# 创建一个顺序模型（sequential model），然后添加层次
model = Sequential()
model.add(Dense(512, activation='relu', input_shape=(784,)))
model.add(Dense(256, activation='relu'))
model.add(Dense(128, activation='relu'))
model.add(Dense(10, activation='softmax'))

# 编译模型
model.compile(loss='categorical_crossentropy', optimizer=RMSprop(), metrics=['accuracy'])

# 拟合（训练）模型训练集；设置批处理大小和迭代轮数
model.fit(x_train, y_train, batch_size=128, epochs=10, verbose=1, validation_split=0.2)

# 评估模型
score = model.evaluate(x_test, y_test, verbose=0)
print('Test loss:', score[0])
print('Test accuracy:', score[1])
