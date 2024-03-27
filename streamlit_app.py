
import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

x=st.slider{"selct"}
st.write(x,'is a square',x*x)

st.title("this the app")
st.header("this is the markdown")
st.markdown("this is header")
st.subheader("this is subheader")
st.caption("this the caption")
st.code("x=2021")
st.latex(r'''a+a r^1+a r^2+a r^3 ''')