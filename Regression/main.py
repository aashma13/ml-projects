import pickle
file = open('salary_model.pickle', 'rb')
model = pickle.load(file)
file.close()

import streamlit as st

st.write("# Salary APP")

yoe = st.number_input("Insert Years of Experience: ")

if yoe or st.button("Predict"):
    y_pred = model.predict([[yoe]]) # X is in 2D
    st.write(y_pred)