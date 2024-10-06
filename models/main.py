from sklearn.metrics import accuracy_score
import joblib
import pandas as pd

loaded_model = joblib.load(r'models\model_randomforest.joblib')
fixed_acidity = 0
volatile_acidity = 0
citric_acid = 0
residual_sugar = 0
chlorides = 0
free_sulfur = 0
total_sulfur = 0
density = 0
pH = 0
sulphate = 0
alc = 0

new_data = pd.DataFrame({
    'fixed acidity': [fixed_acidity],
    'volatile acidity': [volatile_acidity],
    'citric acid': [citric_acid],
    'residual sugar': [residual_sugar],
    'chlorides': [chlorides],
    'free sulfur dioxide': [free_sulfur],
    'total sulfur dioxide': [total_sulfur],
    'density': [density],
    'pH': [pH],
    'sulphates': [sulphate],
    'alcohol': [alc],
})

prediction = loaded_model.predict(new_data)
print(prediction)