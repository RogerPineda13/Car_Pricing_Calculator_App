import streamlit as st
import pandas as pd
import numpy as np
import pickle


cars_df = pickle.load(open('cars.pkl', 'rb'))
X_test = cars_df.drop(['price','model'],axis=1)
test =pickle.load(open('car_price_predictor_model.sav', 'rb'))
st.write("Car Price Predictor")




year = st.number_input(
    label = "What is the year of your car?",
    min_value=2003,
    max_value=2022,
    step =1
)
year = (year-2012.4205045603987)/4.4768709628937495

odometer = st.number_input(
    label = "How many miles is your odometer say?(round to the nearest thousand)",
    min_value=0,
    max_value=500000,
    step =1000

)
odometer = (odometer-102836.53701866485)/57728.5872305997

maker =st.selectbox(label = "Pick a manufacturer",options=list(X_test.columns.values[2:43]))
condition =st.selectbox(label = "What type of condition is your car in?", options = list(X_test.columns.values[44:49]))
cylinders =st.selectbox(label = "How many cylinders does your engine have?", options = list(X_test.columns.values[49:57]))
fuel =st.selectbox(label = "Fuel?", options=list(X_test.columns.values[57:62]))
title =st.selectbox(label = "Title status of the vehicle", options=list(X_test.columns.values[62:68]))
transmission =st.selectbox(label = "Transmission?", options=list(X_test.columns.values[68:71]))
drivetrain=st.selectbox(label = "Drivetrain?", options=list(X_test.columns.values[71:74]))
size=st.selectbox(label = "Size?", options=list(X_test.columns.values[74:78]))
type=st.selectbox(label = "Type", options=list(X_test.columns.values[78:91]))
color=st.selectbox(label = "Color of the vehicle", options=list(X_test.columns.values[91:103]))
state=st.selectbox(label = "State where your car is?", options=list(X_test.columns.values[103:]))



inputss = {'year': year, 'odometer':odometer, maker:[1], condition:[1], cylinders:[1], fuel:[1], title:[1], transmission:[1], drivetrain:[1], size:[1], type:[1], color:[1], state:[1]}
df = pd.DataFrame(inputss)

run = st.button("Click here to get your prediction")
if run:
    input_data = pd.DataFrame(columns=X_test.columns)
    input_data = input_data.append(df, ignore_index=True)
    input_data = input_data.fillna(0)
    st.write("The car is worth:")
    st.write(np.exp(test.predict(input_data)))
    





