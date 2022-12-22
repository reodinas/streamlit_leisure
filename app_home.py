import streamlit as st


def run_home_app(df):
    
    st.subheader('여가문화 시간 및 사용 비중을 분석하는 앱입니다.')
    st.subheader('')
    check = st.checkbox('데이터 보기/숨기기', value=True)
    if check:
        st.dataframe(df)
        st.write(f'전체 데이터는 {df.shape[0]}행, {df.shape[1]}열 입니다')
        examine_date = df['날짜'].unique()
        st.write(f'전체 데이터의 조사 날짜는 {examine_date[0]} 부터 {examine_date[-1]} 까지 입니다.')
        st.write('')    

    # 그룹별로 보기
    check2 = st.checkbox('선택한 데이터만 보고 싶으면 체크해 주세요.')
    if check2:
        group_list = ['전체', '성별', '연령대', '거주지역', '가구소득', '날짜']
        selected_group = st.selectbox('그룹별로 보기', group_list)

        if selected_group == '전체':

            selected_col = st.multiselect('보고 싶은 컬럼을 선택하세요.', ['모든 컬럼'] + list(df.columns))

            if selected_col:
                if '모든 컬럼' in selected_col:
                    df_new = df
                    
                else:
                    df_new = df[selected_col]
                    
        else:
            group_list2 = sorted(df[selected_group].unique())
            selected_group2 = st.multiselect('보고 싶은 값을 선택하세요.', group_list2)

            if selected_group2:
                selected_col = st.multiselect('보고 싶은 컬럼을 선택하세요.', ['모든 컬럼'] + list(df.columns))

                if selected_col:
                    if '모든 컬럼' in selected_col:
                        df_new = df[df[selected_group].apply(lambda x: x in selected_group2)]
                    else:
                        df_new = df[df[selected_group].apply(lambda x: x in selected_group2)][selected_col]

        st.dataframe(df_new)
        st.write(f'{df.shape[0]}행, {df.shape[1]}열')
        

    st.subheader('')
    st.subheader('1. Chart 페이지에서는 이 데이터를 시각화해서 보여줍니다.')
    st.subheader('')
    
    st.subheader('2. Admin 페이지에서는 관리자로서, 매주 추가 조사되는 이 데이터를 지속 관리할 수 있습니다.')
    st.subheader('')
    st.header('')
    st.text('데이터 출처 : 문화 빅데이터 플랫폼 - 하루 평균 여가문화 시간 및 사용 비중')
    st.write('https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=e057a550-f06b-11ec-a6e8-cdf27550dc0d')
    st.subheader('')
    
    
    
    
   