# 02_image_classification_lab.py
import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model, load_model
import numpy as np
import matplotlib.pyplot as plt
import os

# 1. 데이터 준비 (폴더 구조 가정)
# dataset/
#   train/
#     pizza/
#     steak/
#   val/
#     pizza/
#     steak/

# 데모를 위해 가상의 경로 설정 (실행 시 에러 날 수 있음)
# 실제 데이터가 있다면 경로 수정 필요
base_dir = './dataset' 
train_dir = os.path.join(base_dir, 'train')
val_dir = os.path.join(base_dir, 'val')

# 폴더가 없으면 데모용 생성 (실행 방지)
if not os.path.exists(base_dir):
    print("데이터셋 폴더가 없습니다. 이 코드는 구조 설명용입니다.")
    # 임시 실행을 위해 cifar10 데이터로 대체하는 로직을 넣거나 종료
    # 여기서는 코드 루틴만 보여줍니다.

# 2. 제너레이터 설정
# MobileNetV2는 -1 ~ 1 사이 입력을 기대하므로 preprocess_input 함수 사용
train_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input,
    rotation_range=20,
    width_shift_range=0.2,
    horizontal_flip=True
)

val_datagen = ImageDataGenerator(
    preprocessing_function=preprocess_input
)

# 3. 데이터 흐름 생성 (flow_from_directory)
# train_generator = train_datagen.flow_from_directory(
#     train_dir,
#     target_size=(224, 224),
#     batch_size=32,
#     class_mode='categorical'
# )
# val_generator = ...

# 4. 전이 학습 모델 구축 (MobileNetV2)
base_model = MobileNetV2(weights='imagenet', include_top=False, input_shape=(224, 224, 3))
base_model.trainable = False # 동결

# 커스텀 헤드 부착
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.5)(x)
# 클래스 개수에 맞게 수정 (예: 2개)
predictions = Dense(2, activation='softmax')(x)

model = Model(inputs=base_model.input, outputs=predictions)

model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# 5. 학습
# history = model.fit(train_generator, epochs=5, validation_data=val_generator)

# 6. 미세 조정 (Fine Tuning)
print("\n미세 조정 시작...")
base_model.trainable = True
# 상위 층만 해동 (100층 이후부터 학습)
fine_tune_at = 100
for layer in base_model.layers[:fine_tune_at]:
    layer.trainable = False

# 낮은 학습률로 재컴파일
model.compile(optimizer=tf.keras.optimizers.Adam(1e-5),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# history_fine = model.fit(train_generator, epochs=5, validation_data=val_generator)

# 7. 단일 이미지 예측 함수
def predict_image(image_path, model):
    img = load_img(image_path, target_size=(224, 224))
    img_array = img_to_array(img)
    img_expanded = np.expand_dims(img_array, axis=0)
    img_preprocessed = preprocess_input(img_expanded)
    
    pred = model.predict(img_preprocessed)
    class_idx = np.argmax(pred)
    confidence = np.max(pred)
    return class_idx, confidence

# 사용 예시
# idx, conf = predict_image('test_pizza.jpg', model)
# print(f"Class: {idx}, Confidence: {conf}")
