import streamlit as st

# Set up the title and description
st.title("🧮 Interactive Calculator")
st.write("A simple, interactive calculator for basic operations.")

# Sidebar for operation selection
st.sidebar.title("Choose Operation")
operation = st.sidebar.radio(
    "Select an operation:",
    ("Addition (+)", "Subtraction (-)", "Multiplication (×)", "Division (÷)")
)

# Main panel for inputs and results
st.write("### Enter your numbers:")

# Input fields for numbers
num1 = st.number_input("Enter the first number", value=0.0, format="%.2f")
num2 = st.number_input("Enter the second number", value=0.0, format="%.2f")

# Function to perform the calculation based on the selected operation
def calculate(num1, num2, operation):
    if operation == "Addition (+)":
        return num1 + num2
    elif operation == "Subtraction (-)":
        return num1 - num2
    elif operation == "Multiplication (×)":
        return num1 * num2
    elif operation == "Division (÷)":
        if num2 != 0:
            return num1 / num2
        else:
            return "Error: Division by zero is not allowed."

# Displaying the selected operation for clarity
st.write(f"### Operation: {operation}")

# Calculate result when any input changes
result = calculate(num1, num2, operation)

# Display the result
if isinstance(result, str):
    # If result is an error message
    st.error(result)
else:
    st.success(f"The result is: {result}")

# Additional options to reset values
if st.button("Reset"):
    st.experimental_rerun()
