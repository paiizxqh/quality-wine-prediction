import joblib
import pandas as pd

loaded_model = joblib.load(r'models\model.joblib')
####################################################
fixed_acidity = float(input("fixed_acidity : "))
volatile_acidity = float(input("volatile_acidit : "))
citric_acid = float(input("citric_acid : "))
residual_sugar = float(input("residual_sugar : "))
chlorides = float(input("chlorides : "))
free_sulfur = int(input("free_sulfur : "))
total_sulfur = int(input("total_sulfurtotal_sulfur : "))
density = float(input("density : "))
pH = float(input("pH : "))
sulphate = float(input("sulphate : "))
alc = float(input("alcohol : "))

###################################################

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
print("Prediction:",prediction)