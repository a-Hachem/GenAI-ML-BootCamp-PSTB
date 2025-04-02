# import streamlit as st

# st.title("My First Streamlit App")
# st.write("Hello, Streamlit!")
#
# 
# 1.5 Utilisation des widgets
# Streamlit fournit des widgets pour interagir avec vos données.



import streamlit as st

st.title("Streamlit Widgets")

# Slider
x = st.slider("Select a value", 0, 100, 50)
st.write("Selected value:", x)

# Text input
name = st.text_input("Enter your name", "Type here...")
st.write("Hello,", name)

# Checkbox
show_data = st.checkbox("Show data")
if show_data:
    st.write("Data is being displayed.")

#Selectbox
option = st.selectbox(
    'Which number do you like best?',
     [1,2,3,4,5,6,7,8,9,10])

st.write('You selected:', option)
 
