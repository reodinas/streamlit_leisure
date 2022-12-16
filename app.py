import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import plotly.express as px

import platform
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
elif platform.system() == 'Windows':
    path = "c:/Windows/Fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=path).get_name()
    rc('font', family=font_name)
else:
    print('Unknown system...')


def main():
    st.title('레저 시간 프로젝트')

    week1 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221005.csv')
    week2 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221012.csv')
    week3 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221019.csv')
    week4 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221026.csv')
    # concat
    df_origin = pd.concat([week1, week2, week3, week4])
    st.dataframe(df_origin)
    st.write(df_origin.shape)

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




if __name__ == '__main__':
    main()