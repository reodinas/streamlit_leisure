import streamlit as st
import numpy as np
import pandas as pd
import os
from app_admin import run_admin_app
from app_home import run_home_app
from app_EDA import run_eda_app

import matplotlib.pyplot as plt
import seaborn as sb

# import platform
# from matplotlib import font_manager, rc
# plt.rcParams['axes.unicode_minus'] = False

# if platform.system() == 'Darwin':
#     rc('font', family='AppleGothic')
# elif platform.system() == 'Windows':
#     path = "c:/Windows/Fonts/malgun.ttf"
#     font_name = font_manager.FontProperties(fname=path).get_name()
#     rc('font', family=font_name)
# elif platform.system() == 'Linux': #리눅스 (구글 콜랩)
#         #!wget "https://www.wfonts.com/download/data/2016/06/13/malgun-gothic/malgun.ttf"
#         #!mv malgun.ttf /usr/share/fonts/truetype/
#         #font_manager._rebuild() 
#         plt.rc('font', family='Malgun Gothic') 



def main():
    st.title('한국인의 여가문화 시간 및 사용 비중')

    df_origin = pd.read_csv('data/df_origin.csv', index_col=0)

    # 컬럼명 변경
    df = df_origin.copy()
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
    # 조사날짜 컬럼 타입변경
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d').dt.strftime('%Y-%m-%d')


    # 유저친화적 데이터프레임
    df_user = df_origin.copy()
    df_user = df_user.rename(columns={'EXAMIN_BEGIN_DE':'날짜',
                        'SEXDSTN_FLAG_CD': '성별',
                        'AGRDE_FLAG_NM': '연령대',
                        'ANSWRR_OC_AREA_NM': '거주지역',
                        'HSHLD_INCOME_DGREE_NM': '가구소득',
                        'WORKDAY_DAY_AVRG_LSR_TIME_VALUE': '평일여가시간',
                        'WKEND_DAY_AVRG_LSR_TIME_VALUE': '주말여가시간',
                        'ONE_WEEK_TOT_LSR_TIME_VALUE': '주간총여가시간',
                        'LSR_TIME_REST_RCRT_USE_RATE': '휴식오락비율',
                        'LSR_TIME_HOBBY_USE_RATE': '취미생활비율',
                        'LSR_TIME_SELF_IMPT_USE_RATE': '자기개발비율',
                        'LSR_TIME_TWDPSN_RLTN_FLWSP_USE_RATE': '대인관계비율',
                        'LSR_TIME_ETC_USE_RATE': '기타비율'
                        })
    df_user['날짜'] = pd.to_datetime(df_user['날짜'], format='%Y%m%d').dt.strftime('%Y-%m-%d')
    df_user['성별'].replace({'F':'여성', 'M':'남성'}, inplace=True)
        
    

    menu = ['Home', 'Chart', 'admin']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        run_home_app(df_user)

    elif choice == 'Chart':
        run_eda_app(df_user)

    
    elif choice == 'admin':
        run_admin_app(df_origin)

    




if __name__ == '__main__':
    main()