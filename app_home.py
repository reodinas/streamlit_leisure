import pandas as pd
import numpy as np
import streamlit as st




def run_home_app(df):
    st.header('')
    st.subheader('한국인의 여가문화 시간 및 사용 비중을 조사한 데이터를 분석하는 앱입니다.')
    st.subheader('')
    st.subheader('1. EDA 페이지에서는 이 데이터를 시각화해서 분석합니다.')
    st.subheader('')
    st.subheader('2. ML 페이지에서는 가구소득을 무응답한 사람들의 소득정도를 분류 예측합니다.')
    st.subheader('')
    st.subheader('3. admin 페이지에서는 관리자로서 매주 추가 조사되는 이 데이터를 지속 관리할 수 있습니다.')
    st.subheader('')
    st.header('')
    st.text('데이터 출처 : 문화 빅데이터 플랫폼 - 하루 평균 여가문화 시간 및 사용 비중')
    st.write('https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=e057a550-f06b-11ec-a6e8-cdf27550dc0d')
    st.header('')
    st.text('데이터프레임')
    st.dataframe(df)
    
    st.write(f'현재 데이터는 {df.shape[0]}행,  {df.shape[1]}열 입니다')
    examine_date = df['date'].unique()
    st.write(f'현재 데이터의 조사 날짜는 {examine_date[0]} 부터 {examine_date[-1]} 까지 입니다.')
    st.write('')
    st.subheader('컬럼 정의')
    st.text('RESPOND_ID: 응답자ID,    date: 조사날짜,     gender: 성별')
    st.text('age: 연령대,             area: 거주지역,     income: 가구소득정도')
    st.text('lsr_work: 평일 일 평균 여가시간,       lsr_weekend: 주말 일 평균 여가시간')
    st.text('lsr_tot: 1주간 총 여가시간,           rest: 여가시간 중 휴식 및 오락 비율')
    st.text('hobby: 여가시간 중 취미활동 비율,      self: 여가시간 중 자기개발 비율')
    st.text('relation: 여가시간 중 대인관계 비율,    etc: 여가시간 중 기타 비율')
    st.text('rest + hobby + self + relation + etc = 100(%)')
 

    
    
   