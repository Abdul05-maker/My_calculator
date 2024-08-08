import streamlit as st

# Title of the web app
st.title("Simple Calculator")

# Input fields for the numbers
number1 = st.number_input("Enter the first number", format="%f")
number2 = st.number_input("Enter the second number", format="%f")

# Dropdown for selecting the operation
operation = st.selectbox("Select operation", ("Add", "Subtract", "Multiply", "Divide"))

# Perform calculation based on selected operation
if operation == "Add":
    result = number1 + number2
elif operation == "Subtract":
    result = number1 - number2
elif operation == "Multiply":
    result = number1 * number2
elif operation == "Divide":
    if number2 != 0:
        result = number1 / number2
    else:
        result = "Error! Division by zero."

# Display the result
st.write("The result is:", result)