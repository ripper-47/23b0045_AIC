import tensorflow as tf
from tensorflow.keras import Sequential
from tensorflow.keras.layers import (Dense,Conv2D,BatchNormalization,LeakyReLU,Flatten,Dropout,
                                     Reshape,Dense,Input) 

# base_model = keras.applications.VGG16(
#     weights='imagenet',
#     input_shape=(224,224,3),
#     include_top=False,
# )
# base_model.trainable=False
# model=Sequential([    
# #   base_model,
#   keras.layers.Input(shape=(226,226,3)),  
#   Conv2D(512,(3,3), padding = 'same',kernel_initializer='he_normal',),
#   BatchNormalization(),
#   LeakyReLU(alpha=0.1),
  
#   Conv2D(512,(3,3),padding = 'same',kernel_initializer='he_normal',),
#   BatchNormalization(),
#   LeakyReLU(alpha=0.1),
  
#   Conv2D(512,(3,3),padding = 'same',kernel_initializer='he_normal',),
#   LeakyReLU(alpha=0.1),

#   Flatten(),
  
#   Dense(512,kernel_initializer='he_normal',),
#   BatchNormalization(),
#   LeakyReLU(alpha=0.1),
  
#   Dropout(0.5),
  
#   Dense(7*7*30,activation='sigmoid'),
  
#   Reshape((7,7,30)),
# ])
# model2 = Sequential([
#     keras.applications.VGG16(
#     weights='imagenet',
#     input_shape=(224,224,3),
#     include_top=False),

#     # Input(shape=(226,226,3)),
#     Dense(512, activation="relu"),
#     Dense(1, activation="softmax"),
# ])
# # print(model.summary())
# print(model2.summary())
# print(1)
# Load the VGG model without the top classification layers
vgg_model = tf.keras.applications.VGG16(weights='imagenet', include_top=False, input_shape=(224, 224, 3))

# Freeze the weights of the VGG model
vgg_model.trainable = False

# Create a Sequential model
model = tf.keras.Sequential()

# Add the VGG model as the first layer
model.add(vgg_model)

# Add additional layers to the Sequential model
model.add(tf.keras.layers.Flatten())
model.add(tf.keras.layers.Dense(256, activation='relu'))
model.add(tf.keras.layers.Dropout(0.5))
model.add(tf.keras.layers.Dense(10, activation='softmax'))  # Example output layer with 10 classes

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# Create dummy input data (you can replace this with your actual input data)
dummy_input = tf.random.normal((1, 224, 224, 3))

# Pass the dummy input through the model to build it
_ = model(dummy_input)

# Print the model summary
model.summary()
