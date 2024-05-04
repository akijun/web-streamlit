import streamlit as st

def page1():
    left_column,right_column=st.columns(2)

    #原油入力
    left_column.title("原油　入力")
    in_radio=left_column.radio(
         "入力単位",('BPD','kL/年','t/年')
        )
    in_mag=left_column.radio(
        "入力倍率",('1','k','M','G','T','万','億'),horizontal=True
        )
    num=left_column.number_input(in_radio,value=0.000,step=0.001)

    ##単位をBPDに合わせる
    if in_radio=='BPD':
        num=num
    elif in_radio=='kL/年':
        num=num*6.2898/340
    elif in_radio=='t/年':
        num=num*6.2898/340*0.8
    #倍率をかける
    if in_mag=='1':
        num=num
    elif in_mag=='k':
        num=num*1000
    elif in_mag=='M':
        num=num*1000000
    elif in_mag=='G':
        num=num*1000000000
    elif in_mag=='T':
        num=num*1000000000000
    elif in_mag=='万':
        num=num*10000
    elif in_mag=='億':
        num=num*100000000

    #原油出力
    right_column.title("原油　出力")
    out_radio=right_column.radio(
        "出力単位",('BPD','kL/年','t/年')
    )    
    out_mag=right_column.radio(
        "出力倍率",('1','k','M','G','T','万','億'),horizontal=True
    )
    
    right_column.text(out_radio)

    if out_radio=='BPD':
        num=num
    elif out_radio=='kL/年':
        num=num*340/6.2898
    elif out_radio=='t/年':
        num=num*340/6.2898/0.8
    #倍率で割る
    if out_mag=='1':
        num=num
    elif out_mag=='k':
        num=num/1000
    elif out_mag=='M':
        num=num/1000000
    elif out_mag=='G':
        num=num/1000000000
    elif out_mag=='T':
        num=num/1000000000000
    elif out_mag=='万':
        num=num/10000
    elif out_mag=='億':
        num=num/100000000

    right_column.subheader(num)

    return


def page2():
    left_column,right_column=st.columns(2)

    #水素入力
    left_column.title("水素1　入力")

    in_radio=left_column.radio(
         "入力単位",('kg','t','Nm3','kWh @5kWh/Nm3'),
        )
    in_mag=left_column.radio(
        "入力倍率",('1','k','M','G','T','万','億'),horizontal=True
        )
    num2=left_column.number_input(in_radio,value=0.000,step=0.001)
     
     ##単位をkgにあわせる
    if in_radio=="kg":
         num2=num2
    elif in_radio=="t":
         num2=num2*1000
    elif in_radio=="Nm3":
         num2=num2/11.2
    elif in_radio=="kWh @5kWh/Nm3":
         num2=num2/5/11.2
       #倍率をかける
    if in_mag=='1':
        num2=num2
    elif in_mag=='k':
        num2=num2*1000
    elif in_mag=='M':
        num2=num2*1000000
    elif in_mag=='G':
        num2=num2*1000000000
    elif in_mag=='T':
        num2=num2*1000000000000
    elif in_mag=='万':
        num2=num2*10000
    elif in_mag=='億':
        num2=num2*100000000

    #水素出力
    right_column.title("水素1　出力")
    out_radio=right_column.radio(
         "出力単位",('kg','t','Nm3','kWh @5kWh/Nm3')
        )
    out_mag=right_column.radio(
        "出力倍率",('1','k','M','G','T','万','億'),horizontal=True
    )

    if out_radio=="kg":
         num2=num2
    elif out_radio=="t":
         num2=num2/1000
    elif out_radio=="Nm3":
         num2=num2*11.2
    elif out_radio=="kWh @5kWh/Nm3":
         num2=num2*5*11.2
     #倍率で割る
    if out_mag=='1':
        num2=num2
    elif out_mag=='k':
        num2=num2/1000
    elif out_mag=='M':
        num2=num2/1000000
    elif out_mag=='G':
        num2=num2/1000000000
    elif out_mag=='T':
        num2=num2/1000000000000
    elif out_mag=='万':
        num2=num2/10000
    elif out_mag=='億':
        num2=num2/100000000

    right_column.text(out_radio)
    right_column.subheader(num2)
    return


def page3():
    num5:float
    left_column,right_column=st.columns(2)

    left_column.title('水素2　入力')
    in_radio=left_column.radio(
        "入力単位",('w','t/年','Nm3/年')
    )
    in_mag=left_column.radio(
        "入力倍率",('1','k','M','G','T','万','億'),horizontal=True
    )
    num5=left_column.number_input(in_radio,value=0.000,step=0.001)

     ##単位をkWにあわせる
    if in_radio=="w":
         num5=num5/1000
    elif in_radio=="t/年":
         num5=num5/0.15
    elif in_radio=="Nm3/年":
         num5=num5*0.0892857/1000/0.15
   
       #倍率をかける
    if in_mag=='1':
        num5=num5
    elif in_mag=='k':
        num5=num5*1000
    elif in_mag=='M':
        num5=num5*1000000
    elif in_mag=='G':
        num5=num5*1000000000
    elif in_mag=='T':
        num5=num5*1000000000000
    elif in_mag=='万':
        num5=num5*10000
    elif in_mag=='億':
        num5=num5*100000000

    #水素出力
    right_column.title('水素2　出力')
    out_radio=right_column.radio(
        "出力単位",('w','t/年','Nm3/年')
    )
    out_mag=right_column.radio(
        "出力倍率",('1','k','M','G','T','万','億'),horizontal=True
    )
    if out_radio=="w":
         num5=num5*1000
    elif out_radio=="t/年":
         num5=num5*0.15
    elif out_radio=="Nm3/年":
         num5=num5/0.0892857*1000*0.15
     #倍率で割る
    if out_mag=='1':
        num5=num5
    elif out_mag=='k':
        num5=num5/1000
    elif out_mag=='M':
        num5=num5/1000000
    elif out_mag=='G':
        num5=num5/1000000000
    elif out_mag=='T':
        num5=num5/1000000000000
    elif out_mag=='万':
        num5=num5/10000
    elif out_mag=='億':
        num5=num5/100000000

    right_column.text(out_radio)
    right_column.subheader(num5)
    #right_column.number_input(out_radio,value=num5)
    return


def page4():
    left_column,right_column=st.columns(2)
    left_column.title('電力　入力')
    in_radio=left_column.radio(
        "入力単位",('MW','GW','TW','億kW','万kW')
    )
    num3=left_column.number_input(in_radio,value=0.000,step=0.001)
    if in_radio=="GW":
        num3=num3
    elif in_radio=="MW":
        num3=num3/1000
    elif in_radio=="TW":
        num3=num3*1000
    elif in_radio=="億kW":
        num3=num3*100
    elif in_radio=="万kW":
        num3=num3*100/1000

    right_column.title('電力　出力')
    out_radio=right_column.radio(
        "出力単位",('MW','GW','TW','億kW','万kW')
    )
    if out_radio=="GW":
        num3=num3
    elif out_radio=='MW':
        num3=num3*1000
    elif out_radio=="TW":
        num3=num3/1000
    elif out_radio=="億kW":
        num3=num3/100
    elif out_radio=="万kW":
        num3=num3/100*1000
    right_column.text(out_radio)
    right_column.subheader(num3)
    return


def page5():
    num4:float
    left_column,right_column=st.columns(2)
    left_column.title('e-fuel　入力')
    in_radio=left_column.radio(
        "入力単位",('燃料BPD','燃料kL/年','燃料kg/d','電力 W','H2 t/d','H2 Nm3/年','CO2 t/d','CO2 Nm3/年')
    )
    in_mag=left_column.radio(
        "入力倍率",('1','k','M','G','T','万','億'),horizontal=True
    )
    num4=left_column.number_input(in_radio,value=0.000,step=0.001)
    if in_radio=="燃料BPD":
        num4=num4
    elif in_radio=='燃料kL/年':
        num4=num4*6.2898/340
    elif in_radio=='燃料kg/d':
        num4=num4/150/0.8
    elif in_radio=='電力 W':
        num4=num4*5/1000000
    elif in_radio=='H2 t/d':
        num4=num4/1008*11.2*1000
    elif in_radio=='H2 Nm3/年':
        num4=num4/1008*11.2*0.0892857/340
    elif in_radio=='CO2 t/d':
        num4=num4/0.87
    elif in_radio=='CO2 Nm3/年':
        num4=num4/0.87/509/340

       #倍率をかける
    if in_mag=='1':
        num4=num4
    elif in_mag=='k':
        num4=num4*1000
    elif in_mag=='M':
        num4=num4*1000000
    elif in_mag=='G':
        num4=num4*1000000000
    elif in_mag=='T':
        num4=num4*1000000000000
    elif in_mag=='万':
        num4=num4*10000
    elif in_mag=='億':
        num4=num4*100000000
    left_column.write(num4)

    right_column.title('e-fuel　出力')
    out_radio=right_column.radio(
        "出力単位",('燃料BPD','燃料kL/年','燃料kg/d','電力 W','H2 t/d','H2 Nm3/年','CO2 t/d','CO2 Nm3/年')
    )
    out_mag=right_column.radio(
        "出力倍率",('1','k','M','G','T','万','億'),horizontal=True
    )
    if out_radio=='燃料BPD':
        num4=num4
    elif out_radio=='燃料kL/年':
        num4=num4/6.2898*340
    elif out_radio=='燃料kg/d':
        num4=num4*150*0.8
    elif out_radio=='電力 W':
        num4=num4/5*1000000
    elif out_radio=='H2 t/d':
        num4=num4*1008/11.2/1000
    elif out_radio=='H2 Nm3/年':
        num4=num4*1008/11.2/0.0892857*340
    elif out_radio=='CO2 t/d':
        num4=num4*0.87
    elif out_radio=='CO2 Nm3/年':
        num4=num4*0.87*509*340
     #倍率で割る
    if out_mag=='1':
        num4=num4
    elif out_mag=='k':
        num4=num4/1000
    elif out_mag=='M':
        num4=num4/1000000
    elif out_mag=='G':
        num4=num4/1000000000
    elif out_mag=='T':
        num4=num4/1000000000000
    elif out_mag=='万':
        num4=num4/10000
    elif out_mag=='億':
        num4=num4/100000000
    right_column.text(out_radio)
    right_column.subheader(num4)
    #right_column.write(num4)        
    return

side_radio=st.sidebar.radio(
    "目次",('原油','水素1','水素2','電力','e-fuel')
    )
if side_radio=='原油':
    page1()
elif side_radio=='水素1':
    page2()
elif side_radio=='水素2':
    page3()
elif side_radio=='電力':
    page4()
elif side_radio=='e-fuel':
    page5()
