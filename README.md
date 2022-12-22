⏲ 한국인의 여가 문화 시간 및 사용 비중
========

여가 시간이 얼마나 되고, 여가 시간을 어떻게 사용하는 지를 차트로 시각화 한 앱입니다.



# Preview
![enter image description here](https://user-images.githubusercontent.com/120348461/208856740-7561748c-eecc-490c-92c6-8a97b0c7d259.jpg)
![enter image description here](https://user-images.githubusercontent.com/120348461/208857008-022ff65a-aece-4333-bd7d-dc057a6189de.jpg)

# Overview
* 이 웹 대시보드에서 사용한 여가시간에 관련된 데이터는 매주 설문조사하여 추가 공개됩니다.
* admin 페이지를 만들어 추가된 csv 파일을 업로드하면 데이터를 자동으로 합치고 서버에 저장하도록 구현했습니다.
* Chart 페이지에서 현재 서버에 저장된 데이터를 시각화한 차트를 구현했습니다.
* AWS EC2 서버를 사용했습니다.
* GitHub Actions를 사용하여 CI/CD 합니다.

# Stacks
<img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=Python&logoColor=white"><img src="https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white"><img src="https://img.shields.io/badge/Amazon EC2-FF9900?style=for-the-badge&logo=Amazon EC2&logoColor=white"><img src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=GitHub&logoColor=white"><img src="https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=Linux&logoColor=white">



# Dataset
![enter image description here](https://user-images.githubusercontent.com/120348461/208861638-638d045e-4503-45cc-880d-08856dd2a705.jpg)

여가시간에 대해 조사한 위와 같은 데이터가 매주 업데이트 됩니다.

출처: 문화 빅데이터 플랫폼 - 하루 평균 여가문화 시간 및 사용 비중

     <https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=e057a550-f06b-11ec-a6e8-cdf27550dc0d>

# Columns
* `RESPOND_ID` : 응답자ID
* `EXAMIN_BEGIN_DE` : 조사시작일자
* `SEXDSTN_FLAG_CD` : 성별 구분코드
* `AGRDE_FLAG_NM` : 연령대 구분명
* `ANSWRR_OC_AREA_NM` : 답변자 거주지역명
* `HSHLD_INCOME_DGREE_NM` : 가구소득정도명
* `WORKDAY_DAY_AVRG_LSR_TIME_VALUE` : 평일 일평균 여가시간값
* `WKEND_DAY_AVRG_LSR_TIME_VALUE`: 주말 일평균 여가시간값
* `ONE_WEEK_TOT_LSR_TIME_VALUE`: 1주 총 여가시간값
* `LSR_TIME_REST_RCRT_USE_RATE` : 여가시간 휴식오락 사용비율
* `LSR_TIME_HOBBY_USE_RATE` : 여가시간 취미생활 사용비율
* `LSR_TIME_SELF_IMPT_USE_RATE` : 여가시간 자기개발 사용비율
* `LSR_TIME_TWDPSN_RLTN_FLWSP_USE_RATE` : 여가시간 대인관계교제 사용비율
* `LSR_TIME_ETC_USE_RATE` : 여가시간 기타 사용비율

# Files
* `app.py`: main 실행 파일
* `app.home.py`: Home 페이지 모듈
* `app_EDA.py`: Chart 페이지 모듈
* `app_admin.py`: admin 페이지 모듈
* `my_function.py`: app_EDA에서 사용되는 차트들을 정의한 모듈
* `df_origin.csv`: 앱에서 사용, 저장되는 데이터
* `df_origin_backup.csv` : df_origin.csv의 백업파일
* `requirements.txt`: 프로젝트에 사용한 라이브러리. 설치방법: `pip install -r requirements.txt`
* `data` 폴더: df_origin.csv를 만들 때 사용했던 csv 파일들. 참고용으로 넣어놨지만 앱의 동작과 아무 관련 없습니다.
* `데이터확인.ipynb`: 데이터를 파악하기 위해 테스트한 코드
* `lsr1.ipynb`: 데이터프레임을 만들 때 테스트한 코드
* `lsr_eda.ipynb`: 차트를 만들 때 테스트한 코드
* `Classification.ipynb`: 머신러닝을 할 때 테스트한 코드

# Connect URL



# 개선할 점







