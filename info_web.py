import streamlit as st
import pandas as pd
import numpy as np

def page1():
    left_column,right_column=st.columns(2)

    left_column.title("原油　入力")
    in_radio=left_column.radio(
         "単位",('BPD','kL/年','t/年')
        )
    num=left_column.number_input(in_radio)

    if in_radio=='BPD':
        num=num
    elif in_radio=='kL/年':
        num=num*6.2898/340
    elif in_radio=='t/年':
        num=num*6.2898/340*0.8

    right_column.title("原油　出力")
    out_radio=right_column.radio(
        "単位",('BPD','KL/年','t/年')
    )
    right_column.text(out_radio)

    if out_radio=='BPD':
        num=num
    elif out_radio=='KL/年':
        num=num*340/6.2898
    elif out_radio=='t/年':
        num=num*340/6.2898/0.8

    right_column.subheader(num)

    return


def page2():
     left_column,right_column=st.columns(2)
     return

def page3():
    left_column,right_column=st.columns(2)
    return

side_radio=st.sidebar.radio(
    "目次",('原油','水素','電力')
    )
if side_radio=='原油':
    page1()
elif side_radio=='水素':
    page2()
elif side_radio=='電力':
    page3()
