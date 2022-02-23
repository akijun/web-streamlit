import streamlit as st

def page1():
    left_column,right_column=st.columns(2)

    #原油入力
    left_column.title("原油　入力")
    in_radio=left_column.radio(
         "入力単位",('BPD','kL/年','t/年')
        )
    num=left_column.number_input(in_radio,0)

    ##単位をBPDに合わせる
    if in_radio=='BPD':
        num=num
    elif in_radio=='kL/年':
        num=num*6.2898/340
    elif in_radio=='t/年':
        num=num*6.2898/340*0.8

    #原油出力
    right_column.title("原油　出力")
    out_radio=right_column.radio(
        "出力単位",('BPD','kL/年','t/年')
    )
    right_column.text(out_radio)

    if out_radio=='BPD':
        num=num
    elif out_radio=='kL/年':
        num=num*340/6.2898
    elif out_radio=='t/年':
        num=num*340/6.2898/0.8

    right_column.subheader(num)

    return


def page2():
     left_column,right_column=st.columns(2)

    #水素入力
     left_column.title("水素　入力")
     in_radio=left_column.radio(
         "入力単位",('kg','Nm3','kWh @5kWh/Nm3')
     )
     num2=left_column.number_input(in_radio,0)
     
     ##単位をkgにあわせる
     if in_radio=="kg":
         num2=num2
     elif in_radio=="Nm3":
         num2=num2/11.2
     elif in_radio=="kWh @5kWh/Nm3":
         num2=num2/5/11.2
    
    #水素出力
     right_column.title("水素　出力")
     out_radio=right_column.radio(
         "出力単位",('kg','Nm3','kWh @5kWh/Nm3')
     )

     if out_radio=="kg":
         num2=num2
     elif out_radio=="Nm3":
         num2=num2*11.2
     elif out_radio=="kWh @5kWh/Nm3":
         num2=num2*5*11.2

     right_column.text(out_radio)
     right_column.subheader(num2)
     return

def page3():
    left_column,right_column=st.columns(2)
    left_column.title('電力　入力')
    in_radio=left_column.radio(
        "入力単位",('GW','MW','億kW','万kW')
    )
    num3=left_column.number_input(in_radio,0)
    if in_radio=="GW":
        num3=num3
    elif in_radio=="MW":
        num3=num3/1000
    elif in_radio=="億kW":
        num3=num3*100
    elif in_radio=="万kW":
        num3=num3*100/1000

    right_column.title('電力　出力')
    out_radio=right_column.radio(
        "出力単位",('GW','MW','億kW','万kW')
    )
    if out_radio=="GW":
        num3=num3
    elif out_radio=='MW':
        num3=num3*1000
    elif out_radio=="億kW":
        num3=num3/100
    elif out_radio=="万kW":
        num3=num3/100*1000
    right_column.text(out_radio)
    right_column.subheader(num3)
    return

def page4():
    left_column,right_column=st.columns(2)
    left_column.title('e-fuel　入力')
    in_radio=left_column.radio(
        "入力単位",('BPD','電力 MW','H2 t/d','CO2 t/d')
    )
    num4=left_column.number_input(in_radio,0)
    if in_radio=="BPD":
        num4=num4
    elif in_radio=='電力 MW':
        num4=num4*5
    elif in_radio=='H2 t/d':
        num4=num4/1008*11.2*1000
    elif in_radio=='CO2 t/d':
        num4=num4/0.87

    right_column.title('e-fuel　出力')
    out_radio=right_column.radio(
        "出力単位",('BPD','電力 MW','H2 t/d','CO2 t/d')
    )
    if out_radio=='BPD':
        num4=num4
    elif out_radio=='電力 MW':
        num4=num4/5
    elif out_radio=='H2 t/d':
        num4=num4*1008/11.2/1000
    elif out_radio=='CO2 t/d':
        num4=num4*0.87
    right_column.text(out_radio)
    right_column.subheader(num4)        
    return

side_radio=st.sidebar.radio(
    "目次",('原油','水素','電力','e-fuel')
    )
if side_radio=='原油':
    page1()
elif side_radio=='水素':
    page2()
elif side_radio=='電力':
    page3()
elif side_radio=='e-fuel':
    page4()
