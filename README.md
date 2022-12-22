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


- Chart: 원하는 데이터를 보기 쉽게 차트로 시각화 합니다.
- admin: 관리자 컨셉으로 만든 페이지 입니다.  매주 추가 조사해 제공되는 데이터를 지속적으로 관리할 수 있습니다.


# Dataset
![enter image description here](https://user-images.githubusercontent.com/120348461/208861638-638d045e-4503-45cc-880d-08856dd2a705.jpg)

여가시간에 대해 조사한 위와 같은 데이터가 매주 업데이트 됩니다.

출처: [문화 빅데이터 플랫폼](https://www.bigdata-culture.kr/bigdata/user/data_market/detail.do?id=e057a550-f06b-11ec-a6e8-cdf27550dc0d)











