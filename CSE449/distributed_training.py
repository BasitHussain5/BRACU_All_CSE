# -*- coding: utf-8 -*-
"""Distributed Training

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1cRwy9084j69FM_gj9gFw7HH7IAnFLY8r
"""

from tensorflow.keras.preprocessing.image import ImageDataGenerator

# Define paths to the train and validation datasets on both laptops
train_dir = '/path/to/dataset/train'
val_dir = '/path/to/dataset/validation'

# Data augmentation for training
train_datagen = ImageDataGenerator(
    rescale=1./255,  # Normalize pixel values to [0, 1]
    rotation_range=20,
    width_shift_range=0.2,
    height_shift_range=0.2,
    shear_range=0.2,
    zoom_range=0.2,
    horizontal_flip=True,
    fill_mode='nearest'
)

# Validation data will only be rescaled (no augmentation)
val_datagen = ImageDataGenerator(rescale=1./255)

# Create data generators for training and validation sets
train_generator = train_datagen.flow_from_directory(
    train_dir,
    target_size=(224, 224),  # Resize images to (224, 224) for EfficientNet
    batch_size=32,  # Number of samples per batch
    class_mode='categorical'  # Multi-class classification
)

val_generator = val_datagen.flow_from_directory(
    val_dir,
    target_size=(224, 224),
    batch_size=32,
    class_mode='categorical'
)

