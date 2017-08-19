from random import randint
import numpy as np
import tflearn
from tflearn.layers.core import input_data, dropout, fully_connected
from tflearn.layers.conv import conv_2d, max_pool_2d
from tflearn.layers.normalization import local_response_normalization
from tflearn.layers.estimator import regression



#input
t_x = [3, 8, 7, 4, 0, 7, 9, 5, 1]
#output
t_y = [9, 5, 1, 4, 7, 9, 7, 3, 6]

x = []
y = []

for i in range(1000):
  x.append(t_x)
  y.append(t_y)

#array of input values
x = np.reshape(x,(-1,3,3,1))

#array of output values
y = np.reshape(y,(-1,9))

network = input_data(shape=[None, 3, 3, 1], name='input')
network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
network = max_pool_2d(network, 2)
network = local_response_normalization(network)
network = fully_connected(network, 128, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 256, activation='tanh')
network = dropout(network, 0.8)
network = fully_connected(network, 9, activation='softmax')
network = regression(network, optimizer='adam', learning_rate=0.01,
                     loss='categorical_crossentropy', name='target')


# Training
model = tflearn.DNN(network, tensorboard_verbose=0)
model.fit({'input': x}, {'target': y}, n_epoch=20)

pred = model.predict(np.reshape(t_x,(-1,3,3,1)))
print "Prediction :", pred[0]