# 01_deeplearning_intro.py
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout
from tensorflow.keras.datasets import mnist
import matplotlib.pyplot as plt
import numpy as np

# 1. 데이터 로드 (MNIST)
print("Downloading MNIST data...")
(X_train, y_train), (X_test, y_test) = mnist.load_data()

# 2. 데이터 탐색
print(f"학습 데이터 형태: {X_train.shape}") # (60000, 28, 28)
print(f"레이블 예시: {y_train[:5]}")

plt.figure(figsize=(10, 2))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.imshow(X_train[i], cmap='gray')
    plt.title(f"Label: {y_train[i]}")
    plt.axis('off')
plt.show()

# 3. 전처리 (정규화)
# 0~255 픽셀값을 0~1 사이로 변환 (학습 안정성)
X_train, X_test = X_train / 255.0, X_test / 255.0

# 4. 모델 설계
model = Sequential([
    Flatten(input_shape=(28, 28)),          # 28x28 2차원을 784 1차원으로 폅니다.
    Dense(128, activation='relu'),          # 은닉층 1 (128개 뉴런)
    Dropout(0.2),                           # 과대적합 방지 (20% 뉴런 끔)
    Dense(64, activation='relu'),           # 은닉층 2 (64개 뉴런)
    Dense(10, activation='softmax')         # 출력층 (0~9 숫자 10개 분류)
])

# 5. 모델 컴파일
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy', # 정수 레이블(0,1,2..)일 때 sparse 사용
              metrics=['accuracy'])

# 6. 모델 요약
model.summary()

# 7. 학습
print("\n모델 학습 시작...")
history = model.fit(X_train, y_train, epochs=5, validation_data=(X_test, y_test))

# 8. 학습 결과 시각화
plt.figure(figsize=(12, 4))

plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.title('Loss Curve')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(history.history['accuracy'], label='Train Acc')
plt.plot(history.history['val_accuracy'], label='Val Acc')
plt.title('Accuracy Curve')
plt.legend()

plt.show()

# 9. 평가
test_loss, test_acc = model.evaluate(X_test, y_test, verbose=2)
print(f"\n테스트 정확도: {test_acc:.4f}")

# 10. 실제 예측 확인
predictions = model.predict(X_test[:1])
print(f"\n첫 번째 테스트 이미지 예측 확률: {np.round(predictions, 2)}")
print(f"예측값: {np.argmax(predictions)} (정답: {y_test[0]})")
