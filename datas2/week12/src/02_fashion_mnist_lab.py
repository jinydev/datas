# 02_fashion_mnist_lab.py
import tensorflow as tf
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.callbacks import ModelCheckpoint, EarlyStopping
from tensorflow.keras.datasets import fashion_mnist
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from sklearn.metrics import confusion_matrix

# 1. 데이터 준비
(X_train, y_train), (X_test, y_test) = fashion_mnist.load_data()
X_train, X_test = X_train / 255.0, X_test / 255.0

class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 2. 모델 설게 (Deep + Batch Normalization)
model = Sequential([
    Flatten(input_shape=(28, 28)),
    
    Dense(256),
    BatchNormalization(), # 배치 정규화
    tf.keras.layers.Activation('relu'),
    Dropout(0.3),
    
    Dense(128),
    BatchNormalization(),
    tf.keras.layers.Activation('relu'),
    Dropout(0.3),
    
    Dense(64, activation='relu'),
    
    Dense(10, activation='softmax')
])

model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# 3. 콜백 정의 (조기 종료 및 자동 저장)
checkpoint = ModelCheckpoint('best_fashion_model.h5', 
                             monitor='val_accuracy', 
                             save_best_only=True, 
                             verbose=1)
early_stopping = EarlyStopping(monitor='val_loss', 
                               patience=5, # 5번 참음 
                               restore_best_weights=True)

# 4. 학습
print("학습 시작 (Early Stopping 적용)...")
history = model.fit(X_train, y_train, 
                    epochs=30, # 넉넉하게 주지만 조기 종료될 것임
                    validation_split=0.2, 
                    callbacks=[checkpoint, early_stopping])

# 5. 베스트 모델 로드 및 평가
best_model = load_model('best_fashion_model.h5')
test_loss, test_acc = best_model.evaluate(X_test, y_test, verbose=0)
print(f"\n최적 모델 테스트 정확도: {test_acc:.4f}")

# 6. 혼동 행렬 시각화
y_pred_probs = best_model.predict(X_test)
y_pred = np.argmax(y_pred_probs, axis=1)

cm = confusion_matrix(y_test, y_pred)
plt.figure(figsize=(10, 8))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=class_names, yticklabels=class_names)
plt.title('Confusion Matrix (Fashion MNIST)')
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.show()

# 7. 잘못 예측한 샘플 확인
miss_indices = np.where(y_pred != y_test)[0]
sample_idx = miss_indices[0]

plt.figure(figsize=(4, 4))
plt.imshow(X_test[sample_idx], cmap='gray')
plt.title(f"True: {class_names[y_test[sample_idx]]}, Pred: {class_names[y_pred[sample_idx]]}")
plt.axis('off')
plt.show()
