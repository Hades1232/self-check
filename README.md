# self-check
파이썬을 이용한 Selenium 크롤링으로 자가진단 매크로 만들기.

## 사용 방법

## ChromeDriver
</hr>

현재 GitHub에 있는 ChromeDriver는 99.0.4844.51 버전을 지원하며, 자신의 크롬 버전(chrome://settings/help)을 확인하신 후 자신의 크롬 버전과 맞는 [Chrome Driver](https://chromedriver.chromium.org/downloads)를 사용하시기 바랍니다.





## Json
</hr>

[Json 파일](https://github.com/Hades1232/self-check/blob/master/info.json)에서 몇가지 항목들을 바꿔줘야 합니다.

(* : 필수 수정 항목)

```c
"name" : 말 그대로 이름입니다. 사용자분의 이름을 적어주시면 됩니다. *

"birthday" : 또한 사용자분의 생일을 적어주시면 됩니다. (ex. 990131) *

"school" : 사용자분의 학교를 적어주시면 됩니다. (대학교는 추후에 만들 예정입니다) *

"city" : 아래의 지원되는 지역 항목을 보고 적어주시면 됩니다. *

"password" : 사용자분의 자가진단 비밀번호를 적어주시면 됩니다. *


"checkRAT" : 오늘 또는 전날 신속항원검사(RAT)를 했는가에 대한 여부입니다.
(true는 양성, false는 음성, null은 실시하지 않음을 나타냅니다. / 기본 값 : null)


"computerPerformance" : 중간 중간 과부화 (오류)를 방지하기 위한 일시정지 값입니다.
(기본 값 : 1 / 최소 값 : 1)


"pictureRoute" : 자가진단이 끝난 후 결과 값 (사진)을 저장하는 경로입니다. 
(기본 값은 현재 폴더이며 수정을 권해드리지 않습니다.)
```
 
<details>
<summary>지원하는 모든 지역 이름 보기</summary>
<p>지원하는 지역 이름은 다음과 같습니다:

'서울', '서울시', '서울교육청', '서울시교육청', '서울특별시'</br>
'부산', '부산광역시', '부산시', '부산교육청', '부산광역시교육청'</br>
'대구', '대구광역시', '대구시', '대구교육청', '대구광역시교육청'</br>
'인천', '인천광역시', '인천시', '인천교육청', '인천광역시교육청'</br>
'광주', '광주광역시', '광주시', '광주교육청', '광주광역시교육청'</br>
'대전', '대전광역시', '대전시', '대전교육청', '대전광역시교육청'</br>
'울산', '울산광역시', '울산시', '울산교육청', '울산광역시교육청'</br>
'세종', '세종특별시', '세종시', '세종교육청', '세종특별자치시', '세종특별자치시교육청'</br>
'경기', '경기도', '경기교육청', '경기도교육청'</br>
'강원', '강원도', '강원교육청', '강원도교육청'</br>
'충북', '충청북도', '충북교육청', '충청북도교육청'</br>
'충남', '충청남도', '충남교육청', '충청남도교육청'</br>
'전북', '전라북도', '전북교육청', '전라북도교육청'</br>
'전남', '전라남도', '전남교육청', '전라남도교육청'</br>
'경북', '경상북도', '경북교육청', '경상북도교육청'</br>
'경남', '경상남도', '경남교육청', '경상남도교육청'</br>
'제주', '제주도', '제주특별자치시', '제주교육청', '제주도교육청', '제주특별자치시교육청', '제주특별자치도'</br>
</p>
</details>



## 라이센스

Copyright © 2022 [Hades](https://github.com/Hades1232).
This project is Apache License 2.0 licensed.


