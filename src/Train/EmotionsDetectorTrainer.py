import numpy as np
import matplotlib.pyplot as plt
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Flatten
from tensorflow.keras.layers import Conv2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.layers import MaxPooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'


# Plots accuracy and loss curves
def plot_model_history(model_history):
    """
    Plot Accuracy and Loss curves given the model_history
    """
    fig, axs = plt.subplots(1,2,figsize=(15,5))
    # summarize history for accuracy
    axs[0].plot(range(1,len(model_history.history['accuracy'])+1),model_history.history['accuracy'])
    axs[0].plot(range(1,len(model_history.history['val_accuracy'])+1),model_history.history['val_accuracy'])
    axs[0].set_title('Model Accuracy')
    axs[0].set_ylabel('Accuracy')
    axs[0].set_xlabel('Epoch')
    axs[0].set_xticks(np.arange(1,len(model_history.history['accuracy'])+1),len(model_history.history['accuracy'])/10)
    axs[0].legend(['train', 'val'], loc='best')
    # summarize history for loss
    axs[1].plot(range(1,len(model_history.history['loss'])+1),model_history.history['loss'])
    axs[1].plot(range(1,len(model_history.history['val_loss'])+1),model_history.history['val_loss'])
    axs[1].set_title('Model Loss')
    axs[1].set_ylabel('Loss')
    axs[1].set_xlabel('Epoch')
    axs[1].set_xticks(np.arange(1,len(model_history.history['loss'])+1),len(model_history.history['loss'])/10)
    axs[1].legend(['train', 'val'], loc='best')
    fig.savefig('plot.png')
    plt.show()


totalTrainingImages = 28709
totalValidationImages = 7178
batchSize = 64
epochs = 50

# Initialize image data generators with rescaling
trainingDataGenerator = ImageDataGenerator(rescale=1./255)
validationDataGenerator = ImageDataGenerator(rescale=1./255)


# Preprocess train images
trainingGenerator = trainingDataGenerator.flow_from_directory(
        '../../dataset/train', # it'll go through the train directory, fetch all the images and labeled then according to the folder name (emotions)
        target_size=(48,48), # each image will be resized to 48 by 48
        batch_size=batchSize,
        color_mode="grayscale", # images will have gray color,
        class_mode='categorical') # the categories will be the folders name (emotions)

# Preprocess test images
validationGenerator = validationDataGenerator.flow_from_directory(
        '../../dataset/test',
        target_size=(48,48),
        batch_size=batchSize,
        color_mode="grayscale",
        class_mode='categorical')


# Create the model, our Convolutional Nwural Network
model = Sequential()

model.add(Conv2D(32, kernel_size=(3, 3), activation='relu', input_shape=(48,48,1))) # Add Convolutional 2D layer with 32 size
model.add(Conv2D(64, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(128, kernel_size=(3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))

model.add(Flatten())
model.add(Dense(1024, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(7, activation='softmax')) # Last dense layer with 7 categories, the seven emotions


# Train the Neural Network Model
model.compile(loss='categorical_crossentropy',optimizer=Adam(lr=0.0001, decay=1e-6),metrics=['accuracy'])

modelInformation = model.fit_generator(
        trainingGenerator,
        steps_per_epoch=totalTrainingImages // batchSize,
        epochs=epochs,
        validation_data=validationGenerator,
        validation_steps=totalValidationImages // batchSize
)

plot_model_history(modelInformation)

# Save the models
model.save_weights('model.h5')


