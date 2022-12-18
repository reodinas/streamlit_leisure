import streamlit as st
import numpy as np
import pandas as pd
import os
from app_admin import run_admin_app
from app_home import run_home_app
from app_EDA import run_eda_app

import matplotlib.pyplot as plt
import seaborn as sb

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
    st.title('한국인의 여가 시간 및 사용 비중')

    df_origin = pd.read_csv('data/df_origin.csv', index_col=0)

    df = df_origin.copy()
    # 컬럼명 변경
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
    
    

    menu = ['Home', 'EDA', 'ML', 'admin']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        run_home_app(df)

    elif choice == 'EDA':
        run_eda_app(df)

    elif choice == 'ML':
        pass

    elif choice == 'admin':
        run_admin_app(df_origin)

    




if __name__ == '__main__':
    main()