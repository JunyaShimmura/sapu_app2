import streamlit as st
from PIL import Image
st.title('サンプルアプリ')
st.caption('これはサンプル用のアプリです')

Image = Image.open('./data/samplePng.png')
st.image(Image, width=200)

#PS C:\Users\PC\Desktop\sample\sapu_app> streamlit run main_app.py      実行