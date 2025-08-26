import streamlit as st
st.title("🧮 Simple Calculator")
st.subheader("🧾 Menu :")
st.write("1️⃣ : Add")
st.write("2️⃣ : Subtract")
st.write("3️⃣ : Multiply")
st.write("4️⃣ : Divide")


a = st.number_input("Enter first number : ",value=None,placeholder="Enter number")
if a is not None : st.write(f"You chose number : {a}")
b = st.number_input("Enter second number : ",value=None,placeholder="Enter number")
if b is not None : st.write(f"You chose number : {b}")

option = st.selectbox("Choose the operation : ",
                    (1,2,3,4),
                    index=None,
                    placeholder="Select operation method...",
)

st.write(f"You chose operation number : {option}")
left, middle, right = st.columns([1,6,1])

result = None
with middle : 
    m = st.button("Calculate",use_container_width=True)
    if m :
        match option:
          case 1:
           result = a + b
          case 2:
           result = a - b
          case 3:
           result = a * b
          case 4:
           if b!=0:
            result = a / b  
           else:
            st.error("❌ Error: Cannot divide by zero")


if result is not None:
    st.success(f"Result: {result:.2f}")
