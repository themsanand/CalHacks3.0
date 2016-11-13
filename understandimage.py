from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Activation, Flatten, Input
from keras.layers import Convolution2D, MaxPooling2D, merge
from keras.optimizers import SGD
import numpy


first_img = numpy.array([numpy.ones((n, m, 3)), numpy.ones((n, m, 3))])
second_img = numpy.array([numpy.ones((n, m, 3)), numpy.ones((n, m, 3))])
same_or_not_labels = numpy.array([1, 1])
time_separation_labels = numpy.array([5, 20])

def check_model(n, m, first_img, second_img, same_or_not_labels, time_separation_labels):
	#First pooling
	pic_1 = Input(shape=(n, m, 3), name='I1')
	pic_2 = Input(shape=(n, m, 3), name='I2')
	conv1a0 = Convolution2D(32, 3, 3, border_mode='same')(pic_1)
	conv2a0 = Convolution2D(32, 3, 3, border_mode='same')(pic_2)
	rl1a0 = Activation('relu')(conv1a0)
	rl2a0 = Activation('relu')(conv2a0)
	conv1a1 = Convolution2D(32, 3, 3, border_mode='same')(rl1a0)
	conv2a1 = Convolution2D(32, 3, 3, border_mode='same')(rl2a0)
	rl1a1 = Activation('relu')(conv1a1)
	rl2a1 = Activation('relu')(conv2a1)
	mp1a = MaxPooling2D(pool_size=(2, 2))(rl1a1)
	mp2a = MaxPooling2D(pool_size=(2, 2))(rl2a1)


	#Second pooling
	conv1b0 = Convolution2D(32, 3, 3, border_mode='valid')(mp1a)
	conv2b0 = Convolution2D(32, 3, 3, border_mode='valid')(mp2a)
	rl1b0 = Activation('relu')(conv1b0)
	rl2b0 = Activation('relu')(conv2b0)
	conv1b1 = Convolution2D(32, 3, 3, border_mode='valid')(rl1b0)
	conv2b1 = Convolution2D(32, 3, 3, border_mode='valid')(rl2b0)
	rl1b1 = Activation('relu')(conv1b1)
	rl2b1 = Activation('relu')(conv2b1)
	mp1b = MaxPooling2D(pool_size=(2, 2))(rl1b1)
	mp2b = MaxPooling2D(pool_size=(2, 2))(rl2b1)

	#Flatten everything
	mp1bf = Flatten()(mp1b)
	mp2bf = Flatten()(mp2b)
	mp1af = Flatten()(mp1a)
	mp2af = Flatten()(mp2a)
	pic_1f = Flatten()(pic_1)def fit

	pic_2f = Flatten()(pic_2)

	#Merge and then create outputs
	merged_layer = merge([mp1bf, mp2bf, mp1af, mp2af], mode='concat')
	dense_layer = Dense(500, activation='relu')(merged_layer)
	is_same_output = Dense(1, activation='sigmoid', name="O1")(dense_layer)
	time_diff_output = Dense(1, activation='tanh', name="O2")(dense_layer)
	model = Model(input=[pic_1, pic_2], output=[is_same_output, time_diff_output])
	model.compile(optimizer= 'sgd', loss={'O1': 'binary_crossentropy', 'O2': 'mean_squared_error'}, metrics={'O1': 'binary_crossentropy', 'O2': 'mean_squared_error'})
	return model
	
def check_fit(model):
	model.fit({'I1': first_img, 'I2': second_img},
          {'O1': same_or_not_labels, 'O2': time_separation_labels},
          nb_epoch=1, batch_size=1)
	return model

def check_test(model):
	model.test_on_batch({'I1':first_img, 'I2':second_img}, {'O1':same_or_not_labels, 'O2':time_separation_labels})

modl = check_model(n, m, first_img, second_img, same_or_not_labels, time_separation_labels)
check_fit(modl)
check_test(modl)

"""
model = Sequential()
# input: 100x100 images with 3 channels -> (3, 100, 100) tensors.
# this applies 32 convolution filters of size 3x3 each.
model.add(Convolution2D(32, 3, 3, border_mode='valid', input_shape=(3, 100, 100)))
model.add(Activation('relu'))
model.add(Convolution2D(32, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Convolution2D(64, 3, 3, border_mode='valid'))
model.add(Activation('relu'))
model.add(Convolution2D(64, 3, 3))
model.add(Activation('relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
# Note: Keras does automatic shape inference.
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(10))
model.add(Activation('softmax'))

sgd = SGD(lr=0.1, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(X_train, Y_train, batch_size=32, nb_epoch=1)"""