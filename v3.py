import pandas as pd
import streamlit as st
st.title("Slider")
uploaded_file = st.file_uploader("choose a file")
if uploaded_file is not None:
	df = pd.read_csv(uploaded_file)
	st.write(df)
    st.slider(label="range", min_value= df['A'],max_value= df['C'])