import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

def main():
    st.title('레저 시간 프로젝트')

    week1 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221005.csv')
    week2 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221012.csv')
    week3 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221019.csv')
    week4 = pd.read_csv('data/CI_DAY_AVRG_LSR_CLTUR_TIME_ND_USE_RLIMP_INFO_20221026.csv')
    
    df = pd.concat([week1, week2, week3, week4])
    st.dataframe(df)


if __name__ == '__main__':
    main()