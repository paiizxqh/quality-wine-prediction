from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import pandas as pd

# โหลดโมเดลที่ฝึกไว้
loaded_model = joblib.load(r'models\model_randomforest.joblib')

# สร้าง Flask app
app = Flask(__name__)
CORS(app)  # เปิดใช้ CORS ให้สามารถเชื่อมต่อจาก origin ต่างๆ ได้

# สร้าง API สำหรับทำนายคุณภาพไวน์
@app.route('/api/predict', methods=['POST'])
def predict():
    try:
        # รับข้อมูลจาก request body (JSON)
        data = request.get_json()

        # ตรวจสอบว่าได้รับข้อมูลครบถ้วนหรือไม่
        required_features = [
            'fixed acidity', 'volatile acidity', 'citric acid', 'residual sugar', 'chlorides',
            'free sulfur dioxide', 'total sulfur dioxide', 'density', 'pH', 'sulphates', 'alcohol'
        ]
        if not all(feature in data for feature in required_features):
            return jsonify({"error": "Missing feature(s) in input data"}), 400

        # สร้าง DataFrame จากข้อมูลที่ได้รับ
        new_data = pd.DataFrame({key: [data[key]] for key in required_features})

        # ทำการทำนาย
        prediction = loaded_model.predict(new_data)

        # ส่งผลลัพธ์กลับในรูปแบบ JSON
        response = {'predicted_quality': int(prediction[0])}
        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)