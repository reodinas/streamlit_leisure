import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px



def run_home_app():
    df_origin = pd.read_csv('data/df_origin.csv', index_col=0)
    st.dataframe(df_origin)
    
    st.write(f'현재 데이터는 {df_origin.shape[0]}행,  {df_origin.shape[1]}열 입니다')
    examine_date = df_origin['EXAMIN_BEGIN_DE'].unique()
    st.write(f'현재 데이터의 조사 날짜는 {examine_date[0]} 부터 {examine_date[-1]} 까지 입니다.')
    st.write('')
    st.write('')
    st.write('')



    st.write('')
    st.write('')
    st.write('')
    

    df = df_origin.copy()
    # 조사날짜 컬럼 타입변경
    df['EXAMIN_BEGIN_DE'] = pd.to_datetime(df['EXAMIN_BEGIN_DE'], format='%Y%m%d')
    df = df.rename(columns={'EXAMIN_BEGIN_DE':'date', 
                        'SEXDSTN_FLAG_CD': 'gender',
                        'AGRDE_FLAG_NM': 'age',
                        'ANSWRR_OC_AREA_NM': 'area',
                        'HSHLD_INCOME_DGREE_NM': 'income',
                        'WORKDAY_DAY_AVRG_LSR_TIME_VALUE': 'lsr_work',
                        'WKEND_DAY_AVRG_LSR_TIME_VALUE': 'lsr_weekend',
                        'ONE_WEEK_TOT_LSR_TIME_VALUE': 'lsr_tot',
                        'LSR_TIME_REST_RCRT_USE_RATE': 'rest',
                        'LSR_TIME_HOBBY_USE_RATE': 'hobby',
                        'LSR_TIME_SELF_IMPT_USE_RATE': 'self',
                        'LSR_TIME_TWDPSN_RLTN_FLWSP_USE_RATE': 'relation',
                        'LSR_TIME_ETC_USE_RATE': 'etc'
                       })
    
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
    group_list = ['성별', '연령대', '거주 지역', '가구 소득 정도']

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

    st.subheader('선택한 그룹에 대한 여가시간 시계열 차트를 보여줍니다.')
    selected_group = st.selectbox('기준이 될 그룹을 선택해 주세요.', group_list)
    df_pivot = pd.pivot_table(df, index=['date', select_dict[selected_group]], aggfunc=np.mean, values=pivot_value)

    selected_col = st.selectbox('어떤 정보를 보여드릴까요?', col_list)
    df_plot = df_pivot[select_dict[selected_col]].unstack()

    fig = px.line(df_plot, x=df_plot.index, y=df_plot.columns)
    st.plotly_chart(fig)