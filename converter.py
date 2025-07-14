import streamlit as st

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

#--Streamlit UI--
st.title("Temperature Converter")
st.write("Convert between Celsius and Fahrenheit")

col1, col2 = st.columns(2)
with col1:
    temperature = st.number_input("Enter temperature:",value=0.0)

with col2:
    unit = st.radio("Select unit",["Celsius","Fahrenheit"])

#--Conversion logic--
if unit in ["Celsius"]:
    result = celsius_to_fahrenheit(temperature)
    st.success(f"The temperature is: {result} F")

else:
    result = fahrenheit_to_celsius(temperature)
    st.success(f"The temperature is: {result} C")