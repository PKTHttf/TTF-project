# from typing_extensions import Concatenate
import numpy as np
from logging import error
from mimetypes import MimeTypes
import streamlit as st
import email, smtplib, ssl # to automate email
import email as mail
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import datetime as dt # to work with date, time
from bs4 import BeautifulSoup # to work with web scrapping (HTML)
import pandas as pd # to work with tables (DataFrames) data
from IPython.core.display import HTML
from streamlit.elements import multiselect # to display HTML in the notebook
import PIL
# import barcode
# from barcode.writer import ImageWriter
# import cv
st.set_page_config(layout='wide')

# from cvcv import ncc_f
abv=ncc_f()
from ncc import ncc_f
from list_info import qc_list
go_list=["ALDER",
"ASH VN",
"ASH",
"BẠCH ĐÀN",
"BEECH",
"CĂM XE",
"CAO SU ĐEN",
"CAO SU",
"CHERRY",
"CHÒ CHỈ",
"SYCAMORE",
"DỪA",
"DƯƠNG LIỄU",
"GÒN",
"HICKORY",
"KAPUS",
"LÒNG MỨT",
"MAPLE",
"MÍT",
"MUỒNG",
"NEP PALLET",
"OAK",
"PƠ MU",
"POPLAR",
"RED ELM",
"RED OAK",
"SỌ KHỈ",
"TẠP",
"TEAK",
"THÔNG",
"TRÀM",
"TRÅU",
"WALNUT",
"WHITE OAK",
"WHITE POPLAR",
"WILLOW",
"XOÀI"
]
in_list=["ADL","ASV","ASH","BDA","BEE","CXE","CSD","CSU","CHE","CCI","SYC","DUA","DLI","GON","HIC","KAP","LMU","MAP","MIT","MNG","NPL","OAK","PMU","PLR","REL","ROK","SOK","TAP","TEK","THO","TRM","TRU","WAL","WOK","WPR","WIL","XOA"]
# abv
list_ncc = abv[0]

list_int= abv[1]
# cv.ncc_f()
# def increment_counter(increment_value=0):
#     rowss += increment_value

# def decrement_counter(decrement_value=0):
#     rowss -= decrement_value

st.subheader('Nhập thông tin:')
a2,a3,a4,a5=st.columns((1.5,1.5,1,1))
with a2:
    ncc=st.multiselect('NCC:',list_ncc)
with a3:
    qc=st.multiselect('QC kiểm:',qc_list)
with a4:
    go=st.multiselect('Loại gỗ:',go_list)
with a5:
    da=st.text_input('Độ ẩm:',)
cls1,cls2,cls3,cls4=st.columns(4)
# with cls1:
#     tk=st.number_input('Thẻ Kiện:',step=1)
with cls2:
    ml=st.text_input('MÃ LÔ:',)
with cls3:
    clg=st.text_input('Chất lượng gỗ',)
with cls4:
    ngaykiem=st.text_input('Ngày kiểm',)


def form(ncc):
    with st.form(key='columns_in_form'):
        rowss=30
        if not ncc:
            st.info('Nhập đầy đủ thông tin ở phía trên')
        else:
            st.subheader('Danh sách kiểm chi tiết:')
            mol1,mol2=st.columns(2)
            with mol1:
                mol1.subheader('KIỆN 1')
            with mol2:
                mol2.subheader('Kiện 2')

            r_1,r_2,r_3,t1_,r_4,r_5,r_6=st.columns((1,1,1,1,1,1,1))
            r1,r2,r3,t2_,r4,r5,r6=st.columns((1,1,2,1,1,1,2))
            # if 'count' not in st.session_state:
                # rowss = 0
            c1,c2,c3,t_2_m,c4,c5,c6=st.columns((1,1,1,1,1,1,1))


            # with c3:
            #     c3.write('Tổng số dòng = ', rowss+1)
            # h=rowss
                
            with r_1:
                a1=r_1.text_input('Dày',)
            with r_2:
                tk1=r_2.text_input('Thẻ kiện',)
            with r_4:
                a2=r_4.text_input('Dày2',)
            with r_5:
                tk2=r_5.text_input('Thẻ kiện2',)
            with r1:
                b1=[]
                for nr in range(rowss):
                    b1.append(r1.text_input('Rộng', key=f'dfuestidn {nr}'))
            with r2:
                    c1=[]
                    for ng in range(rowss):
                        c1.append(r2.text_input(label='Dài', key=f'dfuestion {ng}'))
            with r3:
                    d1= []
                    for ngg in range(rowss):
                        d1.append(r3.text_input(label='Số thanh', key=f'Quđsesdfgtion {ngg}'))
            with r4:
                    b2=[]
                    for nr in range(rowss):
                        b2.append(r4.text_input('Rộng2', key=f'dfuestdidn {nr}'))
            with r5:
                    c2=[]
                    for ng in range(rowss):
                        c2.append(r5.text_input(label='Dài1', key=f'dfuestsdion {ng}'))
            with r6:
                    d2= []
                    for ngg in range(rowss):
                        d2.append(r6.text_input(label='Số thanh1', key=f'Quesdfgsdtion {ngg}'))

            mol3,mol4=st.columns(2)
            with mol3:
                mol3.subheader('KIỆN 3')
            with mol4:
                mol4.subheader('Kiện 4')
            r__1,r__2,r__3,tt,r__4,r__5,r__6=st.columns((1,1,1,1,1,1,1))
            k1,k2,k3,tt_,k4,k5,k6=st.columns((1,1,2,1,1,1,2))
            c_1,c_2,c_3,c_4,c_5,c_6=st.columns((1,1,1,1,1,1))

            with r__1:
                a3=r__1.text_input('Dày3',)
            with r__2:
                tk3=r__2.text_input('Thẻ kiện3',)
            with r__4:
                a4=r__4.text_input('Dày4',)
            with r__5:
                tk4=r__5.text_input('Thẻ kiện4',)     
            with k1:
                    b3=[]
                    for nr in range(rowss):
                        b3.append(k1.text_input('Rộng3', key=f'dfuestsdidn {nr}'))
            with k2:
                    c3=[]
                    for ng in range(rowss):
                        c3.append(k2.text_input(label='Dài2', key=f'dfuesdftion {ng}'))
            with k3:
                    d3= []
                    for ngg in range(rowss):
                        d3.append(k3.text_input(label='Số thanh2', key=f'Quđsesdfdfgtion {ngg}'))
            with k4:
                    b4=[]
                    for nr in range(rowss):
                        b4.append(k4.text_input('Rộng4', key=f'dfuesdsteidn {nr}'))
            with k5:
                    c4=[]
                    for ng in range(rowss):
                        c4.append(k5.text_input(label='Dài3', key=f'dfuestsdddsfsdffion {ng}'))
            with k6:
                    d4= []
                    for ngg in range(rowss):
                        d4.append(k6.text_input(label='Số thanh3', key=f'Quesdfgsddfsdftion {ngg}'))
        st.form_submit_button('Submit')

    
        b1=["0" if v =="" else v for v in b1]
        c1=["0" if v =="" else v for v in c1]
        d1=["0" if v =="" else v for v in d1]
        b2=["0" if v =="" else v for v in b1]
        c2=["0" if v =="" else v for v in c2]
        d2=["0" if v =="" else v for v in d2]    
        b3=["0" if v =="" else v for v in b3]
        c3=["0" if v =="" else v for v in c3]
        d3=["0" if v =="" else v for v in d3]
        b4=["0" if v =="" else v for v in b4]
        c4=["0" if v =="" else v for v in c4]
        d4=["0" if v =="" else v for v in d4] 

        a1="0" if a1 =="" else a1
        a2="0" if a2 =="" else a2
        a3="0" if a3 =="" else a3
        a4="0" if a4 =="" else a4
        tk1="-" if tk1 =="" else tk1
        tk2="-" if tk2 =="" else tk2
        tk3="-" if tk3 =="" else tk3
        tk4="-" if tk4 =="" else tk4
#     # b1=[]
#     # b1=[]
#     # c1=[]
#     # a1=a1.replace(',','.')

#     # for b_ in b:
#     #     new_string = b_.replace(',','.')
#     #     b1.append(new_string)
#     # for c_ in c:
#     #     new_string = c_.replace(',','.')
#     #     c1.append(new_string)
        df=""
        if a1=="0":
            st.info('Nhập đầy đủ thông tin vào form phía trên')
        else:  

            

            dict1={'MÃ THẺ KIỆN':tk1,'QC Dày':a1,'QC Rộng':b1,'QC Dài':c1,'Số thanh':d1}
            dict2={'MÃ THẺ KIỆN':tk2,'QC Dày':a2,'QC Rộng':b2,'QC Dài':c2,'Số thanh':d2}
            dict3={'MÃ THẺ KIỆN':tk3,'QC Dày':a3,'QC Rộng':b3,'QC Dài':c3,'Số thanh':d3}
            dict4={'MÃ THẺ KIỆN':tk4,'QC Dày':a4,'QC Rộng':b4,'QC Dài':c4,'Số thanh':d4}


    
            import pandas as pd
            df1=pd.DataFrame.from_dict(dict1)    
            df2=pd.DataFrame.from_dict(dict2)
            df3=pd.DataFrame.from_dict(dict3)
            df4=pd.DataFrame.from_dict(dict4)
            # df['QC Dày']= float(a1)
            df=pd.concat([df1,df2,df3,df4]).reset_index(drop=True)
            df

            df=df.astype({'QC Rộng':float,'QC Dài':float,'QC Dày':float,'Số thanh':int,'MÃ THẺ KIỆN':str})
            khoi=df['QC Dày']*df['QC Rộng']*df['QC Dài']*df['Số thanh']
            df['MÃ THẺ KIỆN']="K."+in_list[go_list.index(go[0])]+"."+df['MÃ THẺ KIỆN'].astype(str)
            df=df[df['QC Dài']>0]
            df['KHỐI LƯỢNG']=round(khoi/10**9,4)
            td=pd.to_datetime('today')
            df['NGÀY NHẬP LIỆU']=td
            # df['THẺ KIỆN']=tk
            df['NCC']=ncc[0]
            df['LOẠI GỖ']=go[0]
            df['NGƯỜI KIỂM']=qc[0]
            df['NGÀY NHẬP LIỆU']=df['NGÀY NHẬP LIỆU'].dt.date 

            total=round(sum(df['KHỐI LƯỢNG']),4)
            d1=df.sort_index(ascending=False).reset_index(drop=True)      
            st.subheader('KẾT QUẢ:\n\n')
            # tk1
            c1,c2=st.columns(2)
            with c1:
                df1=df[df['MÃ THẺ KIỆN'].str.contains(tk1)].reset_index(drop=True)
                df1
                st.write('TỔNG SỐ KHỐI: ',round(sum(df1['KHỐI LƯỢNG']),4))
            with c2:
                df2=df[df['MÃ THẺ KIỆN'].str.contains(tk2)].reset_index(drop=True)
                df2
                st.write('TỔNG SỐ KHỐI: ',round(sum(df2['KHỐI LƯỢNG']),4))
            l1,l2=st.columns(2)
            with l1:
                df3=df[df['MÃ THẺ KIỆN'].str.contains(tk3)].reset_index(drop=True)
                df3
                st.write('TỔNG SỐ KHỐI: ',round(sum(df3['KHỐI LƯỢNG']),4))
            with l2:
                df4=df[df['MÃ THẺ KIỆN'].str.contains(tk4)].reset_index(drop=True)
                df4
                st.write('TỔNG SỐ KHỐI: ',round(sum(df4['KHỐI LƯỢNG']),4))
            NCC=ncc[0]+" "+"("+clg+")"
            df['NCC']=  NCC
            df['MÃ LÔ']=ml
            # df['NCC']=NCC
            df['ĐỘ ẨM']=da
            df["NGÀY KIỂM"]=ngaykiem
            # with c2:
            #    image= image=st.image(qr_code(link=tk))

            df_2=df[['QC Dày','QC Rộng','QC Dài','Số thanh','KHỐI LƯỢNG']]

            df_2['Số thanh']=df_2['Số thanh'].astype(int)
            df_2['KHỐI LƯỢNG']=df_2['KHỐI LƯỢNG'].astype(str)

            df_2=df_2.astype(str)
            df_2=df_2.replace("0"," ")
            df_2=df_2.replace("0.0"," ")
    return df
data=form(ncc)
ncc_index=list_ncc.index(ncc[0])

ini=list_int[ncc_index]
def eccount(df,ini):
    df4=df
    uni_tk=df4["MÃ THẺ KIỆN"].unique().tolist()
    uni_dai=df4['QC Dài'].unique().tolist()
    uni_dai.sort()
    if len(uni_dai)==2:

        string_dai=str(int(uni_dai[0]))+"/"+str(int(uni_dai[-1]))
    elif len(uni_dai)==1:
        string_dai=str(int(uni_dai[0]))
    else:

        string_dai=str(int(uni_dai[0]))+"-"+str(int(uni_dai[-1]))
    df4['QC Dài 2']=string_dai
    df4["MÃ THẺ KIỆN2"]=df4["MÃ THẺ KIỆN"]
    df4["MÃ THẺ KIỆN3"]=df4["MÃ THẺ KIỆN"]
    df4['QC Dày2']=df['QC Dày']
    df4["ncc"]=ini
    df4['Loại Gỗ']=in_list[go_list.index(go[0])]
    eccount=df4[["MÃ THẺ KIỆN","MÃ THẺ KIỆN2","MÃ THẺ KIỆN3",'QC Dày','QC Dài 2','MÃ LÔ','Loại Gỗ','QC Dày2','ncc','KHỐI LƯỢNG']]

    eccount_gr=eccount.groupby(["MÃ THẺ KIỆN","MÃ THẺ KIỆN2","MÃ THẺ KIỆN3",'QC Dày','QC Dài 2','MÃ LÔ','Loại Gỗ','QC Dày2','ncc'])['KHỐI LƯỢNG'].sum().reset_index()
    return eccount_gr

def push(df,str):
    import streamlit as st
    import pandas as pd
    from google.oauth2 import service_account
    import gspread #-> Để update data lên Google Spreadsheet
    from gspread_dataframe import set_with_dataframe #-> Để update data lên Google Spreadsheet
    from oauth2client.service_account import ServiceAccountCredentials #-> Để nhập Google Spreadsheet Credentials
    credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive'],
    )
    gc = gspread.authorize(credentials)
    spreadsheet_key='1_ZhSbjL2EfbyTLyWCpTrHJi6kCku1j0eVwQ_g1R2QTM'

    import gspread_dataframe as gd
    import gspread as gs

    ws = gc.open("TTF - Nhập liệu gỗ tròn").worksheet(str)
    existing = gd.get_as_dataframe(ws)

    updated = existing.append(df)
    gd.set_with_dataframe(ws, updated)
    st.success('Tải lại trang để tiếp tục nhập liệu')



list_email=['qlcl@tanthanhgroup.com','ttf.qcgo@gmail.com']

if st.button('Xuất danh sách'):
    # send_email("Thẻ kiện: "+tk+" - "+NCC+" - "+qc[0],total,tk,qr_code(link=tk),NCC,qc[0],ml,td,html,list_email)
    sheet='3. DS NHẬP ECOUNT'
    # from cv import push
    ECC=eccount(data,ini)
    push(ECC,sheet)
    data=data[["MÃ THẺ KIỆN","NGÀY NHẬP LIỆU","NGÀY KIỂM",	"NGƯỜI KIỂM",	"NCC",	"LOẠI GỖ",	"QC Dày",	"QC Rộng","QC Dài",	"Số thanh",	 "KHỐI LƯỢNG", 	"MÃ LÔ",'ĐỘ ẨM']]
    data=data[data["QC Dài"]>0]
    push(data,'1. NHẬP LIỆU')
