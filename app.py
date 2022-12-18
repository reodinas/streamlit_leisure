import streamlit as st
import numpy as np
import pandas as pd
import os
from app_admin import run_admin_app
from app_home import run_home_app

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
    st.title('레저 시간 프로젝트')

    menu = ['Home', 'EDA', 'ML', 'admin']

    choice = st.sidebar.selectbox('메뉴', menu)

    if choice == 'Home':
        run_home_app()

    elif choice == 'EDA':
        pass

    elif choice == 'ML':
        pass

    elif choice == 'admin':
        run_admin_app()

    




if __name__ == '__main__':
    main()