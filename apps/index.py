import streamlit as st
import config
import pprint

def app(date):
    st.title('数理演習2C')
    st.write(f'## {date}')

    tmp()

    title = st.text_input('提出ファイルの共有リンクをペースト', placeholder = 'google.com')
    st.write('Your link:', title)

def tmp():
    st.write('tmp')

