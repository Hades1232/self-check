 

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import json
import os



def changeCityName(cityName):
    
    if cityName == '서울' or cityName == '서울시' or cityName == '서울교육청' or cityName =='서울시교육청' or cityName == "서울특별시":
        city = "서울특별시"   
    elif cityName == '부산' or cityName == '부산시' or cityName == '부산교육청' or cityName == '부산광역시교육청' or cityName == "부산광역시":
         city = '부산광역시',
    elif cityName == '대구' or cityName == '대구시' or cityName == '대구교육청' or cityName == '대구광역시교육청' or cityName == "대구광역시":
        city = "대구광역시"
    elif cityName == '인천' or cityName == '인천시' or cityName == '인천교육청' or cityName == '인천광역시교육청' or cityName == "인천광역시":
        city = "인천광역시"
    elif cityName == '광주' or cityName == '광주시' or cityName == '광주교육청' or cityName == '광주광역시교육청' or cityName == "광주광역시":
        city = "광주광역시"
    elif cityName == '대전' or cityName == '대전시' or cityName == '대전교육청' or cityName == '대전광역시교육청' or cityName == "대전광역시":
        city = "대전광역시"
    elif cityName == '울산' or cityName == '울산시' or cityName == '울산교육청' or cityName == '울산광역시교육청' or cityName == "울산광역시":
        city = "울산광역시"
    elif cityName == '세종' or cityName == '세종시' or cityName == '세종교육청' or cityName == '세종특별자치시' or cityName == '세종특별자치시교육청' or cityName == "세종특별시":
       city = "세종특별시"
    elif cityName == '경기' or cityName == '경기교육청' or cityName == '경기도교육청' or cityName == "경기도":
        city = "경기도"
    elif cityName == '강원' or cityName == '강원교육청' or cityName == '강원도교육청' or cityName == "강원도":
        city = "강원도"
    elif cityName == '충북' or cityName == '충북교육청' or cityName == '충청북도교육청' or cityName == "충청북도":
       city = "충청북도"
    elif cityName == '충남' or cityName == '충남교육청' or cityName == '충청남도교육청' or cityName == "충청남도":
       city = "충청남도"
    elif cityName == '전북' or cityName == '전북교육청' or cityName == '전라북도교육청' or cityName == "전라북도":
        city = "전라북도"
    elif cityName == '전남' or cityName == '전남교육청' or cityName == '전라남도교육청' or cityName == "전라남도":
        city = "전라남도"
    elif cityName == '경북' or cityName == '경북교육청' or cityName == '경상북도교육청' or cityName == "경상북도":
        city = "경상북도"
    elif cityName == '경남' or cityName == '경남교육청' or cityName == '경상남도교육청' or cityName == "경상남도":
        city = "경상남도"
    elif cityName == '제주' or cityName == '제주특별자치시' or cityName == '제주교육청' or cityName == '제주도교육청' or cityName == '제주특별자치시교육청' or cityName == '제주특별자치도' or cityName == "제주도":
       city = "제주도"
    else:
        print("잘못된 도시 이름입니다! info.json을 확인해주세요! (잘못된 도시 이름)")
        input()
        exit()
    return city
  

def getInfo(*args):
    
    
    #print(args[5])
    if args[0] == "이름을 적어주세요 (홍길동)":
        print("잘못된 이름입니다! info.json 파일을 확인해주세요. (기본에서 바꾸지 않음)")
        input()
        exit()

    elif args[1] == "생일을 적어주세요 (990111)":
        print("잘못된 생일입니다! info.json 파일을 확인해주세요. (기본에서 바꾸지 않음)")
        input()
        exit()

    elif len(args[1]) != 6:
        print("잘못된 생일입니다! info.json 파일을 확인해주세요. (길이 문제)")
        input()
        exit()

    elif args[2] == "지역을 적어주세요 ex (ㅇㅇ특별시)":
        print("잘못된 지역 이름입니다! info.json 파일을 확인해주세요. (기본에서 바꾸지 않음)")
        input()
        exit()

    elif args[3] == "학교를 적어주세요 (ㅇㅇ고등학교)":
        print("잘못된 학교 이름입니다! info.json 파일을 확인해주세요. (기본에서 바꾸지 않음)")
        input()
        exit()
    
    elif args[4] == "비밀번호를 적어주세요 (1234)":
        print("잘못된 비밀번호입니다! info.json 파일을 확인해주세요. (기본에서 바꾸지 않음)")
        input()    
        exit()

    elif len(args[4]) != 4:
        print("잘못된 비밀번호입니다! info.json 파일을 확인해주세요. (길이 문제)")
        input() 
        exit()

    elif args[5] != True:
      if args[5] != None:
        if args[5] != False:
            print("잘못된 신속항원검사 결과입니다! info.json 파일을 확인해주세요. (null이나 true나 false가 아님 / 따옴표가 없어야 함) ")
            input() 
            exit()
      

    elif args[6] < 1:
        print("적어도 시간은 1초 이상이여야합니다!")
        input()   
        exit()


with open("info.json", 'rt', encoding='UTF8') as f:
    
    data = json.load(f)




name = data["name"]
school = data["school"]
birthday = data["birthday"]
cityName = data["city"]
password = data["password"]
checkRAT = data["checkRAT"]
computerPerformance = int(data["computerPerformance"])
pictureRoute = data["pictureRoute"]



getInfo(name,birthday,cityName,school,password,checkRAT,computerPerformance,pictureRoute)

city = changeCityName(cityName)

def getSchoolType(school):
    
    if "초등학교" in school:
        schoolType = "초등학교"
    elif "중학교" in school:
        schoolType = "중학교"
    elif "대학교" in school:
        print("대학교는 추후 지원할 예정입니다. 죄송합니다.") 
        input()
        exit()
        #schoolType = "대학교"
    
    else:
       print("학교 이름이 정확하지 않습니다. (초등학교 / 중학교 / 고등학교 가 학교 이름에 없음)")
       input()
       exit() 
    return schoolType

schoolType = getSchoolType(school)

try:
    

    URL = 'https://hcs.eduro.go.kr/#/loginHome'
    options=webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome(executable_path='chromedriver', options=options)
    driver.get(url=URL)


    time.sleep(computerPerformance)

    driver.find_element_by_xpath('//*[@id="btnConfirm2"]').click()
    driver.find_element_by_xpath('/html/body/app-root/div/div[1]/div[2]/div/div[2]/div/div[1]/table/tbody/tr[1]/td/button').click()
    driver.find_element_by_xpath('//*[@id="sidolabel"]').click()
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/td/select/option[contains(text(), "' + city + '")]').click()
    driver.find_element_by_xpath('//*[@id="crseScCode"]').click()
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[2]/td/select/option[contains(text(), "' + schoolType + '")]').click()
    driver.find_element_by_xpath('//*[@id="orgname"]').send_keys(school)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[3]/td[2]/button').click()
    time.sleep(computerPerformance)
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[1]/ul/li/a/p/a').click()    
    driver.find_element_by_xpath('/html/body/div/div/div/div/div/div[2]/div[2]/input').click()
    driver.find_element_by_xpath('//*[@id="user_name_input"]').send_keys(name)
    driver.find_element_by_xpath('//*[@id="birthday_input"]').send_keys(birthday)
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    time.sleep(computerPerformance)
    driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button/img').click()
    time.sleep(computerPerformance)
    for i in range(0, 4):
        print(f'[aria-label="{password[i]}"]')
        try: 
            driver.find_element_by_xpath('//*[@aria-label="' + password[i] + '"]').click()
        except:   
            driver.find_element_by_xpath('//*[@id="WriteInfoForm"]/table/tbody/tr/td/div/button/img').click()
            time.sleep(computerPerformance)
            driver.find_element_by_xpath('//*[@aria-label="' + password[i] + '"]').click()
        

    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()
    time.sleep(computerPerformance + 0.3)
    driver.find_element_by_xpath('//*[@id="container"]/div/section[2]/div[2]/ul/li/a[1]').click()
    
    time.sleep(computerPerformance)
    driver.find_element_by_xpath('//*[@id="survey_q1a1"]').click()
    if checkRAT == None:
        driver.find_element_by_xpath('//*[@id="survey_q2a3"]').click()
    elif checkRAT == False:
        driver.find_element_by_xpath('//*[@id="survey_q2a1"]').click()
    elif checkRAT == True:
        driver.find_element_by_xpath('//*[@id="survey_q2a2"]').click()
    print("신속항원검사에서 양성이 나온 경우, 자가진단 매크로를 중지하시고 수동으로 다시 실시해주세요! (매크로는 작동됨)")
    
    driver.find_element_by_xpath('//*[@id="survey_q3a1"]').click()
    driver.find_element_by_xpath('//*[@id="btnConfirm"]').click()

    time.sleep(computerPerformance)
    
    os.system('cls')
    if pictureRoute == '':
        driver.save_screenshot(f"result.png")
        print(f"자가진단에 성공했습니다! 자세한건 result.png를 참고해주세요.")
    else:
        driver.save_screenshot(f"{pictureRoute}/result.png")
    
        print(f"자가진단에 성공했습니다! 자세한건 {pictureRoute}/result.png를 참고해주세요.")
    input()

except Exception as e:
    print(f"오류 발생 : {e}")