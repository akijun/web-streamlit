import streamlit as st
import pandas as pd
import numpy as np


st.title("テスト")
st.header("ヘッダー")
st.subheader("サブヘッダー")
st.text("テキスト")


"""
テスト画面
"""

df=pd.DataFrame(
    {"1列目":[1,2,3],
    "2列目":[4,5,6]}
)

expander=st.expander("石油情報")
expander.table(df)

#expander.write(df)

option_button=st.button("ボタン")

num=st.number_input("数字を入力してください")
st.text(str(num*10))


option_radio=st.sidebar.radio(
  "目次",('BPD等','水素重量')
)


left_column,right_column=st.columns(2)
left_column.title("左")
right_column.title("右")
