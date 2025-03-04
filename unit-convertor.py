import streamlit as st

# Define conversion_factors globally
conversion_factors = {
    "Length": {
        "Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000,
        "Mile": 0.000621371, "Yard": 1.09361, "Foot": 3.28084, "Inch": 39.3701
    },
    "Weight": {
        "Kilogram": 1, "Gram": 1000, "Milligram": 1e6, "Pound": 2.20462, "Ounce": 35.274
    },
    "Temperature": {
        "Celsius": lambda x: x, "Fahrenheit": lambda x: (x * 9/5) + 32, "Kelvin": lambda x: x + 273.15
    }
}

def convert_units(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius":
            return conversion_factors[category][to_unit](value)
        elif from_unit == "Fahrenheit":
            celsius = (value - 32) * 5/9
            return conversion_factors[category][to_unit](celsius)
        elif from_unit == "Kelvin":
            celsius = value - 273.15
            return conversion_factors[category][to_unit](celsius)
    else:
        base_value = value / conversion_factors[category][from_unit]
        return base_value * conversion_factors[category][to_unit]

# Streamlit UI
st.title("Unit Converter")
st.sidebar.header("Choose Conversion Type")
category = st.sidebar.selectbox("Select a category", ["Length", "Weight", "Temperature"])

if category:
    units = list(conversion_factors[category].keys())  # Now accessible globally
    from_unit = st.selectbox("From Unit", units)
    to_unit = st.selectbox("To Unit", units)
    value = st.number_input("Enter Value", min_value=0.0, format="%.5f")
    
    if st.button("Convert"):
        result = convert_units(value, from_unit, to_unit, category)
        st.success(f"{value} {from_unit} = {result:.5f} {to_unit}")
