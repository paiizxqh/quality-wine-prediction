import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
import joblib

data = pd.read_csv(r'data\winequality-red.csv',sep=";")

X = data.drop('quality', axis=1)  # ฟีเจอร์
y = data['quality']  # ค่าที่ต้องการทำนาย

# แบ่งข้อมูลเป็นชุดเทรนและชุดทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeClassifier()

model.fit(X_train,y_train)
y_pred = model.predict(X_test)

# ประเมินผลโมเดลด้วยค่า Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

###################################################################################################
model = DecisionTreeClassifier(max_depth=5, min_samples_split=4)
model.fit(X_train, y_train)

# ทำนายและประเมินอีกครั้ง
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy after tuning: {accuracy}")

joblib.dump(model, 'model.joblib')
plt.figure(figsize=(65,200))
tree.plot_tree(model, filled=True, feature_names=X.columns, class_names=True)
plt.show()
new_data = pd.DataFrame({
    'fixed acidity': [7.4],
    'volatile acidity': [0.7],
    'citric acid': [0],
    'residual sugar': [1.9],
    'chlorides': [0.076],
    'free sulfur dioxide': [11],
    'total sulfur dioxide': [34],
    'density': [0.9978],
    'pH': [3.51],
    'sulphates': [0.56],
    'alcohol': [9.4],
    # เพิ่มฟีเจอร์ตามที่โมเดลใช้ในการฝึก
})

# ใช้โมเดลที่ฝึกไว้แล้วในการทำนาย
prediction = model.predict(new_data)
# แสดงผลการทำนาย
print(f"Prediction: {prediction}")