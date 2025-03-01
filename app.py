import streamlit as st

# Custom CSS for Stylish Design
st.markdown(
    """
    <style>
        /* Full Page Background Gradient */
        body {
            background: linear-gradient(135deg, #FFDD00, #00FF88);
            font-family: 'Arial', sans-serif;
        }

        /* Main Title with Gradient Text */
        .main-title {
            font-family: 'Poppins', sans-serif;
            font-size: 52px;
            font-weight: bold;
            background: linear-gradient(to right, #FF5733, #32CD32);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            text-align: center;
            text-shadow: 2px 2px 6px rgba(0,0,0,0.3);
            margin-bottom: 5px;
        }

        /* Subtitle Style */
        .subtitle {
            font-family: 'Poppins', sans-serif;
            font-size: 20px;
            color: #004d00;
            text-align: center;
            margin-bottom: 30px;
        }

        /* Custom Button */
        div.stButton > button:first-child {
            background: linear-gradient(to right, #FF5733, #FFC300);
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 16px;
            font-weight: bold;
            border-radius: 25px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            transition: transform 0.3s, background 0.3s;
        }

        div.stButton > button:first-child:hover {
            background: linear-gradient(to right, #FFC300, #FF5733);
            transform: scale(1.08);
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Subtitle
st.markdown("<h1 class='main-title'>🌐 Unit Converter 🌐</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>Convert values between various units with ease!</p>", unsafe_allow_html=True)

# Conversion Functions
def length_converter(value, from_unit, to_unit):
    factors = {"Meters": 1, "Kilometers": 0.001, "Centimeters": 100, "Millimeters": 1000, "Inches": 39.3701, "Feet": 3.28084}
    return value / factors[from_unit] * factors[to_unit]

def weight_converter(value, from_unit, to_unit):
    factors = {"Kilograms": 1, "Grams": 1000, "Pounds": 2.20462, "Ounces": 35.274}
    return value / factors[from_unit] * factors[to_unit]

def temperature_converter(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius":
        return (value * 9/5 + 32) if to_unit == "Fahrenheit" else value + 273.15
    if from_unit == "Fahrenheit":
        return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    if from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32

def speed_converter(value, from_unit, to_unit):
    factors = {"Meters per second": 1, "Kilometers per hour": 3.6, "Miles per hour": 2.23694, "Feet per second": 3.28084}
    return value / factors[from_unit] * factors[to_unit]

def time_converter(value, from_unit, to_unit):
    factors = {"Seconds": 1, "Minutes": 1/60, "Hours": 1/3600, "Days": 1/86400}
    return value / factors[from_unit] * factors[to_unit]

# Layout - Two Columns
col1, col2 = st.columns(2)

# Left Column - Length, Weight, Temperature
with col1:
    st.subheader("📏 General Unit \n Converter")
    category = st.selectbox("Select Unit Category", ["Length", "Weight", "Temperature"], key="general_category")
    value = st.number_input("Enter Value:", min_value=0.0, key="general_value")

    if category == "Length":
        units = ["Meters", "Kilometers", "Centimeters", "Millimeters", "Inches", "Feet"]
        from_unit = st.selectbox("From Unit", units, key="length_from")
        to_unit = st.selectbox("To Unit", units, key="length_to")
        if st.button("Convert", key="length_convert"):
            st.success(f"{value} {from_unit} = {length_converter(value, from_unit, to_unit):.4f} {to_unit}")

    elif category == "Weight":
        units = ["Kilograms", "Grams", "Pounds", "Ounces"]
        from_unit = st.selectbox("From Unit", units, key="weight_from")
        to_unit = st.selectbox("To Unit", units, key="weight_to")
        if st.button("Convert", key="weight_convert"):
            st.success(f"{value} {from_unit} = {weight_converter(value, from_unit, to_unit):.4f} {to_unit}")

    elif category == "Temperature":
        units = ["Celsius", "Fahrenheit", "Kelvin"]
        from_unit = st.selectbox("From Unit", units, key="temp_from")
        to_unit = st.selectbox("To Unit", units, key="temp_to")
        if st.button("Convert", key="temp_convert"):
            st.success(f"{value} {from_unit} = {temperature_converter(value, from_unit, to_unit):.2f} {to_unit}")

# Right Column - Speed, Time
with col2:
    st.subheader("⏱️ Speed & Time \n Converter")
    category2 = st.selectbox("Select Unit Category", ["Speed", "Time"], key="special_category")
    value2 = st.number_input("Enter Value:", min_value=0.0, key="special_value")

    if category2 == "Speed":
        units = ["Meters per second", "Kilometers per hour", "Miles per hour", "Feet per second"]
        from_unit = st.selectbox("From Unit", units, key="speed_from")
        to_unit = st.selectbox("To Unit", units, key="speed_to")
        if st.button("Convert", key="speed_convert"):
            st.success(f"{value2} {from_unit} = {speed_converter(value2, from_unit, to_unit):.4f} {to_unit}")

    elif category2 == "Time":
        units = ["Seconds", "Minutes", "Hours", "Days"]
        from_unit = st.selectbox("From Unit", units, key="time_from")
        to_unit = st.selectbox("To Unit", units, key="time_to")
        if st.button("Convert", key="time_convert"):
            st.success(f"{value2} {from_unit} = {time_converter(value2, from_unit, to_unit):.4f} {to_unit}")
