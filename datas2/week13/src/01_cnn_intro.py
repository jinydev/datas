# 01_cnn_intro.py
import tensorflow as tf
from tensorflow.keras.datasets import cifar10
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout, BatchNormalization
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.applications import VGG16
from tensorflow.keras.applications.vgg16 import preprocess_input as vgg_preprocess
import matplotlib.pyplot as plt
import numpy as np

# 1. 데이터 로드 (CIFAR-10)
# 10개 클래스: airplane, automobile, bird, cat, deer, dog, frog, horse, ship, truck
print("데이터 다운로드 중...")
(X_train, y_train), (X_test, y_test) = cifar10.load_data()

# 2. 전처리
# 일반 CNN용: 0~1 정규화
X_train_norm = X_train / 255.0
X_test_norm = X_test / 255.0

# 정답 원-핫 인코딩
y_train_cat = to_categorical(y_train)
y_test_cat = to_categorical(y_test)

# 3. 직접 만드는 CNN 모델
model = Sequential([
    # Conv Layer 1
    Conv2D(32, (3, 3), padding='same', activation='relu', input_shape=(32, 32, 3)),
    BatchNormalization(),
    Conv2D(32, (3, 3), padding='same', activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.2),
    
    # Conv Layer 2
    Conv2D(64, (3, 3), padding='same', activation='relu'),
    BatchNormalization(),
    Conv2D(64, (3, 3), padding='same', activation='relu'),
    BatchNormalization(),
    MaxPooling2D((2, 2)),
    Dropout(0.3),
    
    # Flatten & Dense
    Flatten(),
    Dense(128, activation='relu'),
    BatchNormalization(),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 4. 데이터 증강 (Augmentation)
datagen = ImageDataGenerator(
    rotation_range=15,
    width_shift_range=0.1,
    height_shift_range=0.1,
    horizontal_flip=True,
)
datagen.fit(X_train_norm)

# 5. 모델 학습
print("학습 시작...")
history = model.fit(datagen.flow(X_train_norm, y_train_cat, batch_size=64),
                    epochs=10, 
                    validation_data=(X_test_norm, y_test_cat),
                    verbose=1)

# --- 전이 학습 (Transfer Learning) ---
print("\n전이 학습 데모 (VGG16)...")

# VGG16에 맞는 전처리 (0~255 유지하되 평균값 빼기 등)
# 실제로는 X_train 원본을 써야 함
X_train_vgg = vgg_preprocess(X_train.astype('float32'))
X_test_vgg = vgg_preprocess(X_test.astype('float32'))

# Pretrained Model 불러오기 (Top 제외)
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(32, 32, 3))
base_model.trainable = False # 가중치 동결 (학습 안 되게)

# 내 모델 붙이기
transfer_model = Sequential([
    base_model,
    Flatten(),
    Dense(256, activation='relu'),
    Dropout(0.5),
    Dense(10, activation='softmax')
])

# 학습 (짧게)
transfer_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])
transfer_model.fit(X_train_vgg, y_train_cat, batch_size=64, epochs=3, validation_data=(X_test_vgg, y_test_cat))

print("전이 학습 완료.")
