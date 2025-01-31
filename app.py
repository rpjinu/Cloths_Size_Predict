import streamlit as st
import joblib
import pandas as pd

# Load the pre-trained model
model = joblib.load(r'C:\Users\Ranjan kumar pradhan\.vscode\mlp_model.pkl')

# Streamlit app
st.title("Size Prediction API")
st.write("Enter the following details to predict the size:")

# Input fields
age = st.number_input("Age", min_value=1, max_value=100, value=25)
weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=65)
height = st.number_input("Height (cm)", min_value=100, max_value=250, value=170)

# Preprocess the input data
def preprocess_input(age, weight, height):
    # Calculate BMI (as per your preprocessing step)
    bmi = height / weight
    
    # Create a DataFrame with the input data
    input_data = pd.DataFrame({
        'weight': [weight],
        'age': [age],
        'height': [height],
        'bmi': [bmi]
    })
    
    return input_data

# Predict the size
if st.button("Predict Size"):
    input_data = preprocess_input(age, weight, height)
    prediction = model.predict(input_data)
    
    # Map the predicted size back to the original labels
    size_mapping = {1: 'XXS', 2: 'S', 3: 'M', 4: 'L', 5: 'XL', 6: 'XXL', 7: 'XXXL'}
    predicted_size = size_mapping.get(prediction[0], 'Unknown')
    
    st.write(f"Predicted Size: {predicted_size}")