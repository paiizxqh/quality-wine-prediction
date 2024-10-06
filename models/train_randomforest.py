import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree
import matplotlib.pyplot as plt
import graphviz
from sklearn.tree import export_graphviz
import joblib
from sklearn.metrics import f1_score
from sklearn.metrics import recall_score
from sklearn.metrics import confusion_matrix

# โหลดข้อมูล
data = pd.read_csv(r'data\winequality-red.csv', sep=";")

# แยกฟีเจอร์และเป้าหมาย
X = data.drop('quality', axis=1)  # ฟีเจอร์
y = data['quality']  # ค่าที่ต้องการทำนาย

# แบ่งข้อมูลเป็นชุดเทรนและทดสอบ
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=50)
# สร้างโมเดล Random Forest
model = RandomForestClassifier(n_estimators=300, random_state=10,min_samples_split=2,max_depth=20,class_weight='balanced')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

# ประเมินผลด้วย Accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy}")

#tree_in_forest = model.estimators_[0]  # เลือกต้นไม้ต้นแรกจาก Random Forest
"""
plt.figure(figsize=(260, 200))
tree.plot_tree(tree_in_forest, filled=True, feature_names=X.columns, rounded=True)
plt.title("Decision Tree from Random Forest (Tree 0)")
plt.show()
"""
"""กราฟความสำคัญของ parameter เเต่ละตัว
importances = model.feature_importances_
feature_names = X.columns
# พล็อตกราฟแสดงความสำคัญของฟีเจอร์
indices = np.argsort(importances)[::-1]  # เรียงลำดับความสำคัญจากมากไปน้อย
plt.figure(figsize=(10, 6))
plt.title("Feature Importances")
plt.bar(range(X.shape[1]), importances[indices], align="center")
plt.xticks(range(X.shape[1]), feature_names[indices], rotation=90)
plt.tight_layout()
plt.show()
"""
"""
plt.figure(figsize=(50, 50))
tree.plot_tree(tree_in_forest, filled=True, feature_names=X.columns, rounded=True)
plt.title("Decision Tree from Random Forest (Tree 0)")
plt.savefig("tree_plot.png", bbox_inches='tight')
plt.show()
"""
"""

dot_data = export_graphviz(tree_in_forest, out_file=None, feature_names=X.columns,    filled=True, rounded=True,  special_characters=True)  
graph = graphviz.Source(dot_data)  
graph.render("tree",format='svg')  # บันทึกเป็นไฟล์ tree.pdf
#graph.view()  # แสดงไฟล์
"""

# ทำนายคุณภาพจากข้อมูลใหม่
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
})

prediction = model.predict(new_data)
print(f"Predicted Quality: {prediction[0]}")
#joblib.dump(model, 'model_randomforest.joblib')