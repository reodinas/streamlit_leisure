import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
from my_function import timeseries_chart, pie_chart
from 연습 import bar_chart

def run_eda_app(df):
    # 유저에게 입력받기
    select_dict = {
        '날짜': 'date', 
        '성별': 'gender',
        '연령대': 'age',
        '거주 지역': 'area',
        '가구 소득 정도': 'income',
        '평일 일 평균 여가시간': 'lsr_work',
        '주말 일 평균 여가시간': 'lsr_weekend',
        '1주간 총 여가시간': 'lsr_tot',
        '여가시간 중 휴식 및 오락 비율': 'rest',
        '여가시간 중 취미활동 비율': 'hobby',
        '여가시간 중 자기개발 비율': 'self',
        '여가시간 중 대인관계 비율': 'relation',
        '여가시간 중 기타 비율': 'etc'
        }
    group_list = ['전체', '성별', '연령대', '거주 지역', '가구 소득 정도', '날짜']

    col_list = [
        '평일 일 평균 여가시간',
        '주말 일 평균 여가시간',
        '1주간 총 여가시간',
        '여가시간 중 휴식 및 오락 비율',
        '여가시간 중 취미활동 비율',
        '여가시간 중 자기개발 비율',
        '여가시간 중 대인관계 비율',
        '여가시간 중 기타 비율'
        ]
    bar_chart(df, select_dict, group_list)

    pie_chart(df, select_dict, group_list)
    st.header('')

    timeseries_chart(df, select_dict, group_list, col_list)
    