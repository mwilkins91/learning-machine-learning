import tensorflow as tf
import numpy as np
from tensorflow import keras

model = tf.keras.Sequential([keras.layers.Dense(units=1, input_shape=[1])])

# optimizer is a function/algorythm that adjusts the computer's "guess" each run
# loss is a function /algorythm that judges how wrong the last guess was
# sgd is the name of some algorythm, mean_squared_error is the same
model.compile(optimizer='sgd', loss='mean_squared_error')

# The relationship is y=3x+1, so where x = -1, y=-2 etc. etc
xs = np.array([-1.0, 0.0, 1.0, 2.0, 3.0, 4.0], dtype=float)
ys = np.array([-2.0, 1.0, 4.0, 7.0, 10.0, 13.0], dtype=float)

# Train the model, run 10000 simulations...
model.fit(xs, ys, epochs=10000)


print('\n\n\n ---------- \n\n\n')

# Predict what y would equal for 10 (31 would be correct...)
print('Prediction for 10: ', model.predict([10.0]))
