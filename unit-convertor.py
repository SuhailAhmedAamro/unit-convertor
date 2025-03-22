import streamlit as st

# Function to convert length units
def convert_length(value, from_unit, to_unit):
    length_units = {
        "Meters": 1,
        "Kilometers": 0.001,
        "Centimeters": 100,
        "Millimeters": 1000,
        "Miles": 0.000621371,
        "Yards": 1.09361,
        "Feet": 3.28084,
        "Inches": 39.3701
    }
    return value * (length_units[to_unit] / length_units[from_unit])

# Function to convert weight units
def convert_weight(value, from_unit, to_unit):
    weight_units = {
        "Kilograms": 1,
        "Grams": 1000,
        "Pounds": 2.20462,
        "Ounces": 35.274
    }
    return value * (weight_units[to_unit] / weight_units[from_unit])

# Function to convert temperature units
def convert_temperature(value, from_unit, to_unit):
    if from_unit == "Celsius":
        return (value * 9/5) + 32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else ((value - 32) * 5/9) + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value

# Function to convert time units
def convert_time(value, from_unit, to_unit):
    time_units = {
        "Seconds": 1,
        "Minutes": 1/60,
        "Hours": 1/3600,
        "Days": 1/86400
    }
    return value * (time_units[to_unit] / time_units[from_unit])

# Streamlit UI
st.title("🔄 Unit Converter")

# Sidebar for category selection
category = st.sidebar.selectbox("Select Conversion Type", ["Length", "Weight", "Temperature", "Time"])

# Input for value to convert
value = st.number_input("Enter Value", min_value=0.0, format="%.4f")

if category == "Length":
    from_unit = st.selectbox("From", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    to_unit = st.selectbox("To", ["Meters", "Kilometers", "Centimeters", "Millimeters", "Miles", "Yards", "Feet", "Inches"])
    if st.button("Convert"):
        result = convert_length(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Weight":
    from_unit = st.selectbox("From", ["Kilograms", "Grams", "Pounds", "Ounces"])
    to_unit = st.selectbox("To", ["Kilograms", "Grams", "Pounds", "Ounces"])
    if st.button("Convert"):
        result = convert_weight(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")

elif category == "Temperature":
    from_unit = st.selectbox("From", ["Celsius", "Fahrenheit", "Kelvin"])
    to_unit = st.selectbox("To", ["Celsius", "Fahrenheit", "Kelvin"])
    if st.button("Convert"):
        result = convert_temperature(value, from_unit, to_unit)
        st.success(f"{value}° {from_unit} = {result:.2f}° {to_unit}")

elif category == "Time":
    from_unit = st.selectbox("From", ["Seconds", "Minutes", "Hours", "Days"])
    to_unit = st.selectbox("To", ["Seconds", "Minutes", "Hours", "Days"])
    if st.button("Convert"):
        result = convert_time(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
