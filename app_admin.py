import streamlit as st
import numpy as np
import pandas as pd




def run_admin_app(df_origin):
    st.info('관리자 전용 페이지 입니다.')
    password = st.text_input('비밀번호를 입력하세요.', type='password')
    if password:
        if password == 'abc123':
            st.dataframe(df_origin)
            st.write(f'현재 데이터는 {df_origin.shape[0]}행,  {df_origin.shape[1]}열 입니다')
            examine_date = df_origin['EXAMIN_BEGIN_DE'].unique()
            st.write(f'현재 데이터의 조사 날짜는 {examine_date} 입니다.')
            st.write('')
            st.write('')
            st.write('')

            
            st.subheader('업데이트 된 데이터가 있으면 추가 해주세요.')
            st.write('https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=e057a550-f06b-11ec-a6e8-cdf27550dc0d#!')

            file = st.file_uploader('CSV 파일 업로드', type=['csv'])
            if file is not None:
                df_new = pd.read_csv(file)
                
                st.dataframe(df_new)
                
                st.warning('기존 데이터프레임에 추가하고 파일을 저장하시겠습니까?')
                admin_choice =st.text_input('계속 하려면 "save" 를 입력하세요')
                # 텍스트가 있으면
                if admin_choice:
                    # 텍스트가 save면
                    if admin_choice =='save':
                        # 두 데이터프레임 컬럼의 길이가 다를 때 예외처리
                        try:
                            # 컬럼명이 같으면
                            if np.all(df_origin.columns == df_new.columns):
                                #날짜가 중복되면
                                if df_new['EXAMIN_BEGIN_DE'].unique() in df_origin['EXAMIN_BEGIN_DE'].unique():
                                    st.error('중복된 데이터입니다.')

                                else:
                                    df_origin = pd.concat([df_origin, df_new])
                                    df_origin.dropna(axis=0, inplace=True)
                                    df_origin = df_origin.sort_values((['EXAMIN_BEGIN_DE', 'RESPOND_ID']))
                                    df_origin = df_origin.reset_index().drop('index', axis=1)
                                    df_origin.to_csv('df_origin.csv')

                                    st.success('저장에 성공했습니다.')

                                    st.dataframe(df_origin)
                                    st.write(f'현재 데이터는 {df_origin.shape[0]}행,  {df_origin.shape[1]}열 입니다')
                                    examine_date = df_origin['EXAMIN_BEGIN_DE'].unique()
                                    st.write(f'현재 데이터의 조사 날짜는 {examine_date} 입니다.')
                                    
                            else:
                                st.error('다른 형식의 파일입니다.')
                                
                        except ValueError:
                            st.error('다른 형식의 파일입니다.')
                            

                    else:
                        st.info('작업을 취소합니다.')
                        
                    
        else:
            st.error('잘못된 비밀번호 입니다.')