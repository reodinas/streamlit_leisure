import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px

def run_eda_app(df):
     # 유저에게 입력받기
    select_dict = {
        '조사시작일': 'date', 
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
    group_list = ['선택하지 않음', '성별', '연령대', '거주 지역', '가구 소득 정도']

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

    pivot_value = ['lsr_work', 'lsr_weekend', 'lsr_tot', 'rest', 'hobby', 'self', 'relation', 'etc']

    st.subheader('날짜에 따라 선택한 그룹별로 분리된 차트를 보여줍니다.')
    selected_group = st.selectbox('그룹을 선택해 주세요.', group_list)
    selected_func = st.selectbox('집계함수를 선택해주세요', ['평균', '최대값', '최소값'])

    if selected_group == '선택하지 않음':
        if selected_func == '평균':
            df_pivot = pd.pivot_table(df, index=['date'], aggfunc=np.mean, values=pivot_value)
        elif selected_func == '최대값':
            df_pivot = pd.pivot_table(df, index=['date'], aggfunc=np.max, values=pivot_value)
        elif selected_func == '최소값':
            df_pivot = pd.pivot_table(df, index=['date'], aggfunc=np.min, values=pivot_value)
    else:
        if selected_func == '평균':
            df_pivot = pd.pivot_table(df, index=['date', select_dict[selected_group]], aggfunc=np.mean, values=pivot_value)
        elif selected_func == '최대값':
            df_pivot = pd.pivot_table(df, index=['date', select_dict[selected_group]], aggfunc=np.max, values=pivot_value)
        elif selected_func == '최소값':
            df_pivot = pd.pivot_table(df, index=['date', select_dict[selected_group]], aggfunc=np.min, values=pivot_value)

    selected_col = st.selectbox('보고 싶은 정보를 선택해주세요', col_list)

    if selected_group == '선택하지 않음':
        df_plot = df_pivot[select_dict[selected_col]].to_frame()
    elif selected_group == '가구 소득 정도':
        # 무응답 제거
        df_plot = df_pivot[select_dict[selected_col]].unstack().iloc[ : , :-1]
    else:
        df_plot = df_pivot[select_dict[selected_col]].unstack()

    fig = px.line(df_plot, x=df_plot.index, y=df_plot.columns)
    st.plotly_chart(fig)