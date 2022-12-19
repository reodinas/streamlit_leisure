import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


# 시계열차트
def timeseries_chart(df, select_dict, group_list, col_list):
    pivot_value = ['lsr_work', 'lsr_weekend', 'lsr_tot', 'rest', 'hobby', 'self', 'relation', 'etc']

    st.subheader('날짜에 따라 선택한 그룹별로 분리된 차트를 보여줍니다.')
    selected_group = st.selectbox('그룹을 선택해 주세요.', group_list[:-1])
    selected_func = st.selectbox('집계함수를 선택해주세요', ['평균', '최대값', '최소값'])

    if selected_group == '전체':
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

    selected_col = st.selectbox('보고 싶은 정보를 선택해 주세요', col_list)

    if selected_group == '전체':
        df_plot = df_pivot[select_dict[selected_col]].to_frame()
    elif selected_group == '가구 소득 정도':
        # 무응답 제거
        df_plot = df_pivot[select_dict[selected_col]].unstack().iloc[ : , :-1]
    else:
        df_plot = df_pivot[select_dict[selected_col]].unstack()

    fig = px.line(df_plot, x=df_plot.index, y=df_plot.columns)
    st.plotly_chart(fig)


# 파이차트
def pie_chart(df, select_dict, group_list):
    st.subheader('여가시간 평균 사용비율 차트를 보여줍니다.')
    selected_group = st.selectbox('그룹을 선택해주세요', group_list, key='pie')
    value_list = ['rest', 'hobby', 'self', 'relation', 'etc']
    if selected_group == '전체':
        df_pie = df.loc[:, value_list]
        fig = px.pie(df_pie, values=df_pie.mean(), names=df_pie.columns, title='{} 여가시간 평균 사용비율'.format(selected_group), hole=0.3)
        # text를 차트 안에 삽입, textinfo 설정
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig)
    else:
        df_pie = pd.pivot_table(df, index=select_dict[selected_group], aggfunc=np.mean, values=value_list).T
        selected_col = st.selectbox('보고 싶은 정보를 선택해 주세요.', df_pie.columns)
        fig = px.pie(df_pie, values=selected_col, names=df_pie.index, title='{},  {}의 여가시간 평균 사용비율'.format(selected_group, selected_col), hole=0.3)
        # text를 차트 안에 삽입, textinfo 설정
        fig.update_traces(textposition="inside", textinfo="percent+label")
        st.plotly_chart(fig)