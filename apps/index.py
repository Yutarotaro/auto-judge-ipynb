import streamlit as st
from apps import config
import pprint

def app(date):
    st.title('数理演習2C')
    st.write(f'## {date}')


