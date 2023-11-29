import streamlit as st
import pickle

# Load the pickled model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Create the Streamlit web app
st.header("Profit Prediction")




X_test = st.sidebar.slider("Select Sales to get Profit", 10000, 300000, 50000)

st.write("Profit:", X_test)

yhat_test = model.predict([[X_test]])


st.write("Profit is", yhat_test)

