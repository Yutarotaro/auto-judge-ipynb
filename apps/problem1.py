import streamlit as st

def app():
    st.title('数理演習2C ')

    option = st.selectbox(
     '今日の日付を選択してください',
     ('6/24', '7/1', '7/8'))

    st.write('You selected:', option)

    title = st.text_input('提出ファイルの共有リンクをペースト', placeholder = 'google.com')
    st.write('Your link:', title)

