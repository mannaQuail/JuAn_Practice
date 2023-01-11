# #1 코딩 연습한 프로그램에 대한 설명입니다.<br>
# #2 sudoku game
Date : 06/20/2020<br>
line number : 240<br>
usage language : C(bool type 때문에 업로드 파일 형식은 C++)<br>
description : 주어진 스도쿠 문제를 푸는 게임. 빈 공간은 0으로 표현하였음. '행', '열', '넣을 숫자'의 형식으로 입력하면 주어진 위치에 숫자가 입력되며, 모든 칸을 채우면 자동으로 종료된다.<br>
limitation : 스도쿠 문제를 입력하면 자동으로 그 문제를 푸는 프로그램까지 개발하였으나 컴퓨터가 바뀌며 날라갔음. 앞으로 git push를 수시로 해야겠다.<br><br>
# #3 2022년 KBO 삼성 라이온즈 타자들 분석
Date : 12/13/2022<br>
line number : 124<br>
usage language : python<br>
description : 삼성 라이온즈 타자들의 2022년 경기 데이터를 python selenium module을 사용해 크롤링한 다음 python beautifulSoup module을 사용하여 데이터를 파싱하였다. 이를 통해 가지고 선수들의 각종 지표(wOBA, wRAA, RAR)를 계산한 다음 최종적으로 WAR을 계산하였다. 그 결과는 다음과 같았다.<br>
|이름|wOBA|wRAA|RAR|WAR|
|---|---|---|---|---|
|**구자욱**|0.39|21.63|36.36|3.64|
|**강민호**|0.39|21.28|36.08|3.61|
|**김상수**|0.32|-2.27|6.40|0.64|
|**피렐라**|0.51|93.62|114.62|**11.46**|
|**김헌곤**|0.24|-17.83|-9.86|-0.99|
|**김지찬**|0.33|1.30|16.60|1.56|
|**오재일**|0.46|58.03|75.89|**7.59**|
|**강한울**|0.39|11.20|19.60|1.96|
|**이원석**|0.39|16.82|27.99|2.80|
|**오선진**|0.31|-4.42|5.78|0.58|
|**김태군**|0.37|7.14|14.98|1.50|
|**김재성**|0.43|15.65|21.82|2.18|
|**김현준**|0.37|11.79|25.86|2.59|
|**이재현**|0.30|-6.30|1.67|0.17|

limitation : 원래 WAR을 계산할 때는 수비적인 지표도 포함하여야 하지만 수비적인 지표는 주관적인 경우가 많아 포함시키지 못하였음.<br><br>
ref.
<ol>
  https://dev-dain.tistory.com/91 (selenium 사용법1)<br>
  https://coding-kindergarten.tistory.com/151 (selenium 사용법2)<br>
  https://charimlab.tistory.com/entry/ep01%EC%9B%B9%ED%81%AC%EB%A1%A4%EB%A7%81-11-%EB%8F%99%EC%A0%81-%ED%8E%98%EC%9D%B4%EC%A7%80%EC%9B%B9-%EB%8F%99%EC%9E%91-%EC%9E%90%EB%8F%99%ED%99%94Selenium-with-%ED%8C%8C%EC%9D%B4%EC%8D%AC (동적 크롤링시 사용해야 할 모듈(selenium) 검색)<br>
  https://wikidocs.net/85739 (Beautifulsoup 사용법1)<br>
  https://library.gabia.com/contents/9239/ (Beautifulsoup 사용법2)<br>
  https://sabermetrics-kbo.tistory.com/24  (WAR 계산 방법)<br>
  https://sabermetrics-kbo.tistory.com/23(wRAA 계산 방법)<br>
  http://www.statiz.co.kr/main.php (리그 평균 wOBA, wOBA scale 등 리그의 전체적인 지표를 확인)<br>
  https://sabermetrics-kbo.tistory.com/24 (WAR 계산 방법)<br>
</ol>

# #4 tetris game
Date : 12/20/2022<br>
line number : 506<br>
usage language : python<br>
description : 테트리스를 만들어 보았다. 화살표 키로 떨어지는 블록을 움직일 수 있고 한 줄이 다 체워지면 줄이 삭제되며 100점이 올라간다. 위 화살표를 누르면 블록이 시계방향으로 돌아간다. 300점마다 블록의 떨어지는 속도가 증가한다.<br>
limitation : 버그가 있음. 바닥에 닿을 때 순간적으로 블록을 돌리면 블록이 공중에 뜨는 현상이 발생. 추후 수정 예정.<br><br>
ref.<br>
<ol>
  https://ai-creator.tistory.com/559 (필드의 아이디어와 블록을 1차원 구조로 표현하는 아이디어만 빌렸음)
</ol>
