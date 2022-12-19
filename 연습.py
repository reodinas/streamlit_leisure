import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px


# select_dict = {
#         '조사시작일': 'date', 
#         '성별': 'gender',
#         '연령대': 'age',
#         '거주 지역': 'area',
#         '가구 소득 정도': 'income',
#         '평일 일 평균 여가시간': 'lsr_work',
#         '주말 일 평균 여가시간': 'lsr_weekend',
#         '1주간 총 여가시간': 'lsr_tot',
#         '여가시간 중 휴식 및 오락 비율': 'rest',
#         '여가시간 중 취미활동 비율': 'hobby',
#         '여가시간 중 자기개발 비율': 'self',
#         '여가시간 중 대인관계 비율': 'relation',
#         '여가시간 중 기타 비율': 'etc'
#         }
# group_list = ['전체', '성별', '연령대', '거주 지역', '가구 소득 정도']

# col_list = [
#         '평일 일 평균 여가시간',
#         '주말 일 평균 여가시간',
#         '1주간 총 여가시간',
#         '여가시간 중 휴식 및 오락 비율',
#         '여가시간 중 취미활동 비율',
#         '여가시간 중 자기개발 비율',
#         '여가시간 중 대인관계 비율',
#         '여가시간 중 기타 비율'
#         ]

def bar_chart(df, select_dict, group_list):
    st.subheader('평균 여가시간 차트를 보여줍니다.')
    value_list = ['lsr_tot', 'lsr_weekend', 'lsr_work']
    selected_group = st.selectbox('그룹을 선택해주세요', group_list, key='bar')
    
    if selected_group == '전체':
        df_bar = df[value_list].mean().to_frame()
        df_bar.rename(columns={0:'전체 데이터'}, inplace=True)
        fig = px.bar(df_bar.T, y=df_bar.index, barmode='group')
        fig.update_layout(
            title=dict(text='<b>주간, 휴일, 평일의 평균 여가시간</b>'),
            xaxis_title="<b></b>",
            yaxis_title="<b>시간</b>",
            showlegend=True
        )
        st.plotly_chart(fig)

    else:  
        df_bar = pd.pivot_table(df, index=select_dict[selected_group], aggfunc=np.mean, values=value_list)  
        df_bar = df_bar.sort_values('lsr_tot', ascending=False)

        fig = px.bar(df_bar, x=df_bar.index, y=df_bar.columns, barmode='group')
        fig.update_layout(
            title=dict(text='<b>주간, 휴일, 평일의 평균 여가시간</b>'),
            xaxis_title="<b>{}</b>".format(selected_group),
            yaxis_title="<b>시간</b>",
            showlegend=True
        )
        st.plotly_chart(fig)

    
# def pie_chart(df, select_dict, group_list):
#     st.subheader('여가시간 평균 사용비율 차트를 보여줍니다.')
#     selected_group = st.selectbox('그룹을 선택해주세요', group_list)
#     value_list = ['rest', 'hobby', 'self', 'relation', 'etc']
#     if selected_group == '전체':
#         df_pie = df.loc[:, value_list]
#         fig = px.pie(df_pie, values=df_pie.mean(), names=df_pie.columns, title='{} 여가시간 평균 사용비율'.format(selected_group), hole=0.3)
#         # text를 차트 안에 삽입, textinfo 설정
#         fig.update_traces(textposition="inside", textinfo="percent+label")
#         st.plotly_chart(fig)
#     else:
#         df_pie = pd.pivot_table(df, index=select_dict[selected_group], aggfunc=np.mean, values=value_list).T
#         selected_col = st.selectbox('보고 싶은 정보를 선택해 주세요.', df_pie.columns)
#         fig = px.pie(df_pie, values=selected_col, names=df_pie.index, title='{},  {}의 여가시간 평균 사용비율'.format(selected_group, selected_col), hole=0.3)
#         # text를 차트 안에 삽입, textinfo 설정
#         fig.update_traces(textposition="inside", textinfo="percent+label")
#         st.plotly_chart(fig)    
        
