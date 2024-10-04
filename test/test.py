import keras
from keras.models import load_model
import numpy as np
x_new = np.array([[7.9,1.04,0.05,2.2,0.084,13,29,0.9959,3.22,0.55,9.9]])  # ปรับให้ตรงกับจำนวนฟีเจอร์ที่ใช้ในการฝึก
# โหลดโมเดลจากไฟล์ .keras
loaded_model = load_model('my_model.keras')
predictions = loaded_model.predict(x_new)

# แสดงผลลัพธ์
print(predictions)