import streamlit as st
import pandas as pd

st.title("🏗️ Construction Project Monitor")
st.write("This is a web app running via Streamlit!")

# Create a simple table
data = pd.DataFrame({
    'Project': ['Bridge A', 'Site B', 'Mall C'],
    'Status': ['On Track', 'Delayed', 'On Track']
})

st.table(data)

if st.button('Click for Site Alert'):
    st.warning("Weather delay predicted for Site B!")
