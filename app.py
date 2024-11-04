import streamlit as st
import numpy as np

# Set up the Streamlit interface
st.title("🧮 Scientific Calculator")
st.write("Perform basic and scientific calculations with ease.")

# Sidebar for choosing between simple and scientific modes
mode = st.sidebar.selectbox("Choose Calculator Mode", ["Simple", "Scientific"])

# Sidebar for selecting the operation
if mode == "Simple":
    operation = st.sidebar.radio("Select an operation", ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)"))
else:
    operation = st.sidebar.radio(
        "Select a scientific operation",
        ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)",
         "Power (x^y)", "Square Root (√x)", "Logarithm (log10(x))", "Sine (sin(x))",
         "Cosine (cos(x))", "Tangent (tan(x))", "Exponential (e^x)")
    )

# Input fields based on the operation selected
st.write("### Enter your numbers:")

# If operation requires two inputs, display two input fields
if operation in ["Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)", "Power (x^y)"]:
    num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
    num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")
else:
    num1 = st.number_input("Enter the number", value=0.0, format="%.2f")
    num2 = None

# Function to perform the calculation based on the selected operation
def calculate(num1, num2, operation):
    if operation == "Addition (+)":
        return num1 + num2
    elif operation == "Subtraction (-)":
        return num1 - num2
    elif operation == "Multiplication (×)":
        return num1 * num2
    elif operation == "Division (÷)":
        return "Error: Division by zero is not allowed." if num2 == 0 else num1 / num2
    elif operation == "Power (x^y)":
        return num1 ** num2
    elif operation == "Square Root (√x)":
        return np.sqrt(num1) if num1 >= 0 else "Error: Square root of negative number is not allowed."
    elif operation == "Logarithm (log10(x))":
        return np.log10(num1) if num1 > 0 else "Error: Logarithm of zero or negative number is not allowed."
    elif operation == "Sine (sin(x))":
        return np.sin(np.radians(num1))
    elif operation == "Cosine (cos(x))":
        return np.cos(np.radians(num1))
    elif operation == "Tangent (tan(x))":
        return np.tan(np.radians(num1))
    elif operation == "Exponential (e^x)":
        return np.exp(num1)

# Perform the calculation and display the result
if st.button("Calculate"):
    result = calculate(num1, num2, operation)
    if isinstance(result, str):
        st.error(result)
    else:
        st.success(f"The result is: {result}")

# Option to reset values
if st.button("Reset"):
    st.experimental_rerun()
