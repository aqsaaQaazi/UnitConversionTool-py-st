import streamlit as st
# -----------LOGIC-------------
# UI: select category => select unit => enter number => get results

st.set_page_config(
    layout="centered",
    page_icon="⤴",
    page_title="Unito | Aqsaa Qaazi"
)

st.markdown("# |Unito")
st.markdown("#### One tool for all your unit needs. Because no one likes math.\n ##### just select, enter, and click! \n \n")


# ---------------VARIABLES________________-


category = st.selectbox("Select Category", ["Length", "Weight", "Time", "Temperature"])

# dictionary
conversions = {
    "Length": {
        "kilometers to miles": 0.621371,
        "miles to kilometers": 1 / 0.621371,
    },
    "Weight": {
        "kilograms to pounds": 2.20462,
        "pounds to kilograms": 1 / 2.20462,
    },
    "Time": {
        "seconds to minutes": 1 / 60,
        "minutes to seconds": 60,
        "minutes to hours": 1 / 60,
        "hours to minutes": 60,
    }, 
    "Temperature": {
        "celsius to fahrenheit" : lambda x: (x * 9/5) + 32,
        "fahrenheit to celsius": lambda x: (x - 32) * 5/9,
    }
}

# Main Function
def convert_units(category, value, units):
    try:
        
        # this try is writen by ai.
        if category in conversions:
            # Get the conversion function or rate
            conversion = conversions[category].get(units)
            if conversion:
                if callable(conversion):  # If it's a function (for Temperature)
                    return conversion(value)
                else:  # If it's a number (for Length, Weight, Time)
                    return value * conversion
            else:
                st.error("Invalid conversion type selected")
                return None
        else:
            st.error("Invalid category selected")
            return None
    except KeyError:
        st.error("Invalid type selected")
        return None

# UNit dropdownas
if category == "Length":
    units = st.selectbox("Select Conversion", 
                        [
                        "kilometers to miles", 
                        "miles to kilometers",
                        ])

elif category == "Weight":
    units = st.selectbox("Select Conversion", 
                        [
                        "kilograms to pounds", 
                        "pounds to kilograms",
                        ])

elif category == "Time":
    units = st.selectbox("Select Conversion", 
                        [
                        "seconds to minutes", 
                        "minutes to seconds", 
                        "minutes to hours", 
                        "hours to minutes",
                        ])

elif category == "Temperature":
    units = st.selectbox("Select Conversion",
                        [
                        "celsius to fahrenheit",
                        "fahrenheit to celsius",
                        ])

value = st.number_input("Enter the value", min_value=0.0)

if st.button("Convert"):
    if value > 0:
        result = convert_units(category, value, units)
        if result is not None:
            from_unit, to_unit = (
            units.split(" to ") if " to " in units else units.split(" into ")
        )
            st.success(f"Conversion complete: {value} {from_unit} → {round(result, 2)} {to_unit}.")


        else:
            st.error("Please enter a valid positive number.")
