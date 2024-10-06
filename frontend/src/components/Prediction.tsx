import React, { useState } from "react";
import { Form, Input, Button, Card, notification } from "antd";
import axios from "axios";

const Prediction: React.FC = () => {
  const [loading, setLoading] = useState<boolean>(false);

  const onFinish = async (values: any) => {
    console.log("Form values before conversion:", values); // Log ค่าที่กรอกในฟอร์ม

    const numericValues = Object.keys(values).reduce((acc, key) => {
      acc[key] = parseFloat(values[key]);
      return acc;
    }, {} as Record<string, number>);

    console.log("Converted numeric values:", numericValues); // Log ค่าที่แปลงแล้ว

    setLoading(true);
    try {
      console.log("Sending data to API..."); // Log ก่อนส่งข้อมูล
      const response = await axios.post<{ predicted_quality: number }>(
        "http://localhost:5000/api/predict",
        numericValues
      );

      console.log("API Response:", response.data); // Log ข้อมูลที่ตอบกลับจาก API

      notification.success({
        message: "Prediction Result",
        description: `Predicted Wine Quality: ${response.data.predicted_quality}`,
        className: 'vintage-notification'
      });

      // รีเฟรชหน้าหลังจาก 15 วินาที
      setTimeout(() => {
        window.location.reload(); // ใช้ window.location.reload() เพื่อรีเฟรชหน้า
      }, 10000); // 15,000 มิลลิวินาที = 15 วินาที
    } catch (error) {
      console.error("Error while predicting wine quality:", error); // Log ข้อผิดพลาด
      notification.error({
        message: "Prediction Failed",
        description: "There was an error predicting the wine quality.",
        className: 'vintage-notification'
      });
    } finally {
      console.log("Loading state set to false."); // Log ขณะที่ทำการตั้งค่า loading
      setLoading(false);
    }
  };

  const validateNumber = (_: any, value: string) => {
    const regex = /^\d*\.?\d*$/;
    if (!value) {
      console.log("Validation failed: This field is required"); // Log เมื่อไม่กรอกข้อมูล
      return Promise.reject("This field is required");
    }
    if (!regex.test(value) || parseFloat(value) < 0) {
      console.log("Validation failed: Invalid positive number"); // Log เมื่อกรอกข้อมูลไม่ถูกต้อง
      return Promise.reject("Please enter a valid positive number");
    }
    return Promise.resolve();
  };

  return (
    <Card className="vintage-card">
      <div className="vintage-card-title">
        <h2>Predict Your Wine's Quality</h2>
        <div className="vintage-divider"></div>
      </div>
      <Form layout="vertical" onFinish={onFinish} className="vintage-form">
        {[
          { label: "Fixed Acidity", name: "fixed acidity" },
          { label: "Volatile Acidity", name: "volatile acidity" },
          { label: "Citric Acid", name: "citric acid" },
          { label: "Residual Sugar", name: "residual sugar" },
          { label: "Chlorides", name: "chlorides" },
          { label: "Free Sulfur Dioxide", name: "free sulfur dioxide" },
          { label: "Total Sulfur Dioxide", name: "total sulfur dioxide" },
          { label: "Density", name: "density" },
          { label: "pH", name: "pH" },
          { label: "Sulphates", name: "sulphates" },
          { label: "Alcohol", name: "alcohol" }
        ].map((field) => (
          <Form.Item
            key={field.name}
            label={field.label}
            name={field.name}
            rules={[{ required: true, validator: validateNumber }]}
          >
            <Input className="vintage-input" />
          </Form.Item>
        ))}
        <Form.Item>
          <Button
            type="primary"
            htmlType="submit"
            loading={loading}
            className="vintage-button"
          >
            Predict Quality
          </Button>
        </Form.Item>
      </Form>
    </Card>
  );
};

export default Prediction;