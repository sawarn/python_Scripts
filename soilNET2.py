import numpy
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, BatchNormalization, Activation
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.constraints import maxnorm
from keras import backend as K 
#K.set_image_dim_ordering('tf')
import pickle
from keras.models import model_from_json
from PIL import Image
from keras.utils import np_utils
import os
from imutils import paths
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from keras import backend as K
from sklearn.metrics import confusion_matrix


img_width, img_height = 150, 150

train_data = r"C:\Users\Shivam\Downloads\Soils\Train"
#validation_data = "filepath"
test_data = r"C:\Users\Shivam\Downloads\Soils\Test"

train_path = list(paths.list_images(train_data)) 
totalTrain = len(train_path)
#totalValidation =len(list(paths.list_images(validation_data)))
totalTest = len(list(paths.list_images(test_data)))         

trainLabels = [p.split(os.path.sep)[-2] for p in train_path] 
#trainLabels = to_categorical(trainLabels)
#classTotals = trainLabels.sum(axis=0)
classWeight = dict()
#print (trainLabels)

"""for i in range(0, len(classTotals)):
	classWeight[i] = classTotals.max() / classTotals[i]"""

epochs = 25
batch_size = 10

if K.image_data_format() == 'channels_first':
    input_shape = (3, img_width, img_height)
else:
    input_shape = (img_width, img_height, 3)

model = Sequential()

model.add(Conv2D(16, (3, 3), input_shape=(img_width,img_height,3), padding="valid"))
model.add(Activation('relu'))
model.add(BatchNormalization())

model.add(Conv2D(32, (3, 3), padding="same"))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())
model.add(Conv2D(32, (3, 3), padding="same"))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())



model.add(Conv2D(64, (3, 3), padding="same"))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())

model.add(Conv2D(64, (3, 3), padding="same"))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(BatchNormalization())
   
model.add(Conv2D(128, (3, 3), padding="same"))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Flatten())
    
model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.2))
model.add(BatchNormalization())

model.add(Dense(128))
model.add(Activation('relu'))
model.add(BatchNormalization())

model.add(Dense(6))  #Adding the final layer compression constant
model.add(Activation('softmax'))

train_datagen = ImageDataGenerator(
    rescale=1. / 255,
    shear_range=0.2,
    zoom_range=0.2,
    rotation_range = 40,
    width_shift_range=0.2,
    height_shift_range=0.2,
    vertical_flip= True,
    horizontal_flip=True)

test_datagen = ImageDataGenerator(rescale=1. / 255)

train_generator = train_datagen.flow_from_directory(
    train_data,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    shuffle = True,
    color_mode="rgb",
    class_mode='categorical') #depends on the number of labels

"""validation_generator = test_datagen.flow_from_directory(
    validation_data,
    target_size=(img_width, img_height),
    batch_size=batch_size,
    shuffle = True,
    color_mode="rgb",
    class_mode='categorical')"""

test_generator = test_datagen.flow_from_directory(
	test_data,
	class_mode="categorical",
	target_size=(img_width, img_height),
	color_mode="rgb",
	shuffle=False,
	batch_size = batch_size)
#model.build(img_width=150, img_height=150, depth=3,
	#classes=2)
optimizer = 'adam'
model.compile(loss='categorical_crossentropy', optimizer=optimizer, metrics=['accuracy'])

model.fit_generator(
    train_generator,
    steps_per_epoch=totalTrain // batch_size,
    epochs=epochs,
    #validation_data=validation_generator,
    #validation_steps=totalValidation // batch_size,
    class_weight = classWeight)

print("[INFO] evaluating network...")
test_generator.reset()
predIdxs = model.predict(x=test_generator, steps=(totalTest // batch_size) + 1)

#model_json = model.to_json()
#with open("model.json", "w") as json_file:
 #   json_file.write(model_json)
  #serialize weights to HDF5
  
#json_file = open('model.json', 'r')
#loaded_model_json = json_file.read()
#json_file.close()
#loaded_model = model_from_json(loaded_model_json)
#loaded_model.load_weights("weights.h5")


#model.save_weights("weights.h5")
#H=model.load_weights("weights.h5")
with open ('model_pickle','wb') as f:
    pickle.dump(model,f)
