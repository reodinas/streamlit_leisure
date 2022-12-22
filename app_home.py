import streamlit as st




def run_home_app(df):
    st.subheader('여가문화 시간 및 사용 비중을 보여주는 앱입니다.')
    st.subheader('')
    
    st.dataframe(df)
    st.write(f'현재 데이터는 {df.shape[0]}행,  {df.shape[1]}열 입니다')
    examine_date = df['날짜'].unique()
    st.write(f'현재 데이터의 조사 날짜는 {examine_date[0]} 부터 {examine_date[-1]} 까지 입니다.')
    st.write('')
    # st.subheader('컬럼 정의')
    # st.text('RESPOND_ID: 응답자ID,    date: 조사날짜,     gender: 성별')
    # st.text('age: 연령대,             area: 거주지역,     income: 가구소득정도')
    # st.text('lsr_work: 평일 일 평균 여가시간,       lsr_weekend: 주말 일 평균 여가시간')
    # st.text('lsr_tot: 1주간 총 여가시간,           rest: 여가시간 중 휴식 및 오락 비율')
    # st.text('hobby: 여가시간 중 취미생활 비율,      self: 여가시간 중 자기개발 비율')
    # st.text('relation: 여가시간 중 대인관계 비율,    etc: 여가시간 중 기타 비율')
    # st.text('rest + hobby + self + relation + etc = 100(%)')
 
    st.subheader('1. Chart 페이지에서는 이 데이터를 시각화해서 보여줍니다.')
    st.subheader('')
    
    st.subheader('2. Admin 페이지에서는 관리자로서, 매주 추가 조사되는 이 데이터를 지속 관리할 수 있습니다.')
    st.subheader('')
    st.header('')
    st.text('데이터 출처 : 문화 빅데이터 플랫폼 - 하루 평균 여가문화 시간 및 사용 비중')
    st.write('https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=e057a550-f06b-11ec-a6e8-cdf27550dc0d')
    st.subheader('')
    

    
    
   