import streamlit as st
import numpy as np
import pandas as pd
import os




def run_admin_app():
    df_origin = pd.read_csv('data/df_origin.csv', index_col=0)
    st.dataframe(df_origin)
    st.write(f'현재 데이터는 {df_origin.shape[0]}행,  {df_origin.shape[1]}열 입니다')
    examine_date = df_origin['EXAMIN_BEGIN_DE'].unique()
    st.write(f'현재 데이터의 조사 날짜는 {examine_date} 입니다.')
    st.write('')
    st.write('')
    st.write('')

    
    st.subheader('추가 할 데이터가 있으면 추가 해주세요.')

    file = st.file_uploader('CSV 파일 업로드', type=['csv'])
    if file is not None:
        df_new = pd.read_csv(file)
        st.dataframe(df_new)
        
        st.warning('기존 데이터프레임에 추가하고 파일을 저장하시겠습니까?')
        admin_choice =st.text_input('그렇다면 "save" 를 타이핑하세요')
        if admin_choice =='save':
            df_origin = pd.concat([df_origin, df_new])
            df_origin = df_origin.sort_values((['EXAMIN_BEGIN_DE', 'RESPOND_ID']))
            df_origin = df_origin.reset_index().drop('index', axis=1)
            df_origin.to_csv('data/df_origin.csv')

            st.dataframe(df_origin)
            st.write(f'현재 데이터는 {df_origin.shape[0]}행,  {df_origin.shape[1]}열 입니다')
            examine_date = df_origin['EXAMIN_BEGIN_DE'].unique()
            st.write(f'현재 데이터의 조사 날짜는 {examine_date} 입니다.')