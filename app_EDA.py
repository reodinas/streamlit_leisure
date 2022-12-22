import streamlit as st
from my_function import timeseries_chart, pie_chart, bar_chart


def run_eda_app(df):
    # 유저에게 입력받기
    select_dict = {
        '날짜': '날짜', 
        '성별': '성별',
        '연령대': '연령대',
        '거주지역': '거주지역',
        '가구소득': '가구소득',
        '평일 일 평균 여가시간': '평일여가시간',
        '주말 일 평균 여가시간': '주말여가시간',
        '1주간 총 여가시간': '주간총여가시간',
        '여가시간 중 휴식 및 오락 비율': '휴식오락비율',
        '여가시간 중 취미생활 비율': '취미생활비율',
        '여가시간 중 자기개발 비율': '자기개발비율',
        '여가시간 중 대인관계 비율': '대인관계비율',
        '여가시간 중 기타 비율': '기타비율'
        }

    select_dict2 = {
        '날짜': 'date', 
        '성별': 'gender',
        '연령대': 'age',
        '거주지역': 'area',
        '가구소득': 'income',
        '평일 일 평균 여가시간': 'lsr_work',
        '주말 일 평균 여가시간': 'lsr_weekend',
        '1주간 총 여가시간': 'lsr_tot',
        '여가시간 중 휴식 및 오락 비율': 'rest',
        '여가시간 중 취미생활 비율': 'hobby',
        '여가시간 중 자기개발 비율': 'self',
        '여가시간 중 대인관계 비율': 'relation',
        '여가시간 중 기타 비율': 'etc'
        }

    group_list = ['전체', '성별', '연령대', '거주지역', '가구소득', '날짜']

    col_list = [
        '평일 일 평균 여가시간',
        '주말 일 평균 여가시간',
        '1주간 총 여가시간',
        '여가시간 중 휴식 및 오락 비율',
        '여가시간 중 취미생활 비율',
        '여가시간 중 자기개발 비율',
        '여가시간 중 대인관계 비율',
        '여가시간 중 기타 비율'
        ]

    st.header('')
    bar_chart(df, select_dict, group_list)
    st.header('')
    pie_chart(df, select_dict, group_list)
    st.header('')
    timeseries_chart(df, select_dict, group_list, col_list)
    