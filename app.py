import streamlit as st

# Set up the Streamlit interface
st.title("Simple Calculator")

# Operation options
st.write("Select an operation:")
operation = st.selectbox("Operation", ("Addition", "Subtraction", "Multiplication", "Division"))

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Perform the calculation based on the selected operation
if st.button("Calculate"):
    if operation == "Addition":
        result = num1 + num2
        st.write(f"The result is: {result}")
    elif operation == "Subtraction":
        result = num1 - num2
        st.write(f"The result is: {result}")
    elif operation == "Multiplication":
        result = num1 * num2
        st.write(f"The result is: {result}")
    elif operation == "Division":
        if num2 != 0:
            result = num1 / num2
            st.write(f"The result is: {result}")
        else:
            st.write("Error: Division by zero is not allowed.")
