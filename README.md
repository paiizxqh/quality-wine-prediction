### Wine Quality Prediction

```markdown
# Wine Quality Prediction

## Overview
The **Wine Quality Prediction** project is a web application that predicts the quality of wine based on its physicochemical properties. The prediction model uses a **Random Forest Classifier** trained on the wine dataset. This project aims to provide an interactive and easy-to-use interface for predicting wine quality, using **React** on the frontend and **Flask** for the backend API.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [API Documentation](#api-documentation)
- [License](#license)

## Features
- Predict the quality of wine based on various physicochemical properties such as acidity, sugar content, and alcohol levels.
- Uses **Random Forest Classifier** to provide accurate predictions.
- User-friendly interface created with **React** and **Ant Design**.
- Parallax effects and vintage theme for an engaging user experience.

## Technologies Used
- **Frontend**: React, TypeScript, Ant Design
- **Backend**: Flask, Python, Joblib for model serialization
- **Machine Learning Model**: Random Forest Classifier from `scikit-learn`
- **Styling**: CSS, Vintage-themed decorations, Parallax effect

## Setup and Installation

### Prerequisites
- Node.js and npm
- Python 3 and pip
- Flask

### Frontend Setup
1. Navigate to the `frontend` directory.
   ```bash
   cd frontend
   ```
2. Install dependencies.
   ```bash
   npm install
   ```
3. Start the development server.
   ```bash
   npm start
   ```

### Backend Setup
1. Navigate to the `backend` directory.
   ```bash
   cd backend
   ```
2. Create a virtual environment.
   ```bash
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On MacOS/Linux:
     ```bash
     source venv/bin/activate
     ```
4. Install dependencies.
   ```bash
   pip install -r requirements.txt
   ```
5. Start the Flask server.
   ```bash
   flask run
   ```

## Usage
1. Open your browser and navigate to `http://localhost:3000`.
2. Fill in the input fields with the physicochemical properties of the wine (e.g., acidity, sugar content).
3. Click on **Predict Quality**.
4. The predicted wine quality will be displayed along with a notification.

## Project Structure
```
wine-quality-prediction/
│
├── backend/
│   ├── models/
│   │   └── model_randomforest.joblib   # Trained Random Forest model
│   ├── app.py                          # Flask API to handle predictions
│   └── requirements.txt                # Python dependencies
│
├── frontend/
│   ├── public/
│   │   └── index.html                  # HTML entry point
│   ├── src/
│   │   ├── components/
│   │   │   └── Prediction.tsx          # Prediction form component
│   │   ├── assets/
│   │   │   └── images/                 # Images used in the frontend
│   │   ├── css/
│   │   │   └── style.css               # Styling for the application
│   │   └── App.tsx                     # Main app file
│   └── package.json                    # Frontend dependencies
│
└── README.md                           # Project documentation
```

## API Documentation

### `/api/predict`
- **Method**: POST
- **Description**: Predicts the wine quality based on physicochemical properties.
- **Request Body**: JSON object containing:
  - `fixed acidity`
  - `volatile acidity`
  - `citric acid`
  - `residual sugar`
  - `chlorides`
  - `free sulfur dioxide`
  - `total sulfur dioxide`
  - `density`
  - `pH`
  - `sulphates`
  - `alcohol`
- **Response**: JSON object with the predicted quality.
  
  Example:
  ```json
  {
    "predicted_quality": 6
  }
  ```

## License
This project is licensed under the MIT License. Feel free to use, modify, and distribute this software as needed.

---

### Notes:
- Make sure the Flask backend is running before interacting with the React frontend.
- You may need to adjust the API URL in `Prediction.tsx` if you deploy the backend to a different server.

Happy coding! 🍷✨
```
