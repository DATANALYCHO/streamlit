import streamlit as st
import pandas as pd
st.title("데이터 분석")
st.write("데이터에서 의미 있는 정보를 추출하고 의사 결정을 돕는 과정입니다.")

# Read the dataset
df = pd.read_csv('height_weight.csv')

# Create a scatter plot
st.scatter_chart(data=df, x='H', y='W')
