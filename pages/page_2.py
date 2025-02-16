import streamlit as st
import pandas as pd

df = pd.read_csv('./data/tmp.csv',index_col='月')
st.line_chart(df)
st.bar_chart(df['2023年'])
