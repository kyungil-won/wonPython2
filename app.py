from flask import Flask
from flask import request
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.keys import Keys
import time
app = Flask(__name__)
@app.route('/',methods=['GET'])
@app.route('/home')
def home(llitem=[]):
  driver = webdriver.Chrome('C:/Users/USER/PycharmProjects/SeleniumTest1/Drivers/chromedriver.exe')  # 또는 chromedriver.exe
  driver.implicitly_wait(15)  # 묵시적 대기, 활성화를 최대 15초가지 기다린다.

  # 페이지 가져오기(이동)
  driver.get('https://www.vivino.com/banfi-brunello-di-montalcino/w/22917?year=2013&price_id=17703713')
  # driver.get('https://www.vivino.com/crama-ferdi-lady-black-editie-limitata/w/7633874?year=2019&price_id=24558178')
  driver.execute_script("window.scrollTo(0, 1000)")

  time.sleep(5)
  html = driver.page_source  # 페이지의 elements모두 가져오기
  soup = BeautifulSoup(html, 'html.parser')  # BeautifulSoup사용하기
  search_soup = soup.select_one('.vivinoRating__averageValue--3Navj')  # BeautifulSoup사용하기
  search_soup2 = soup.select_one('.vivinoRating__caption--3tZeS')  # BeautifulSoup사용하기
  button = driver.find_element_by_css_selector('.tasteNote__popularKeywords--1q7RG')
  button.click()
  time.sleep(10)
  search_soup3 = driver.find_elements_by_css_selector('div.noteTag__name--CrZvX')

  print(search_soup.text)
  print(search_soup2.text)

  for item in search_soup3:
      llitem.append(item.text)


  return {"val1":search_soup.text,"val2":search_soup2.text,"val3":llitem}

  # 5초후 종료
  time.sleep(5)
  driver.quit()  # 웹 브라우저 종료. driver.close()는 탭 종료

if __name__ == '__main__':
    app.run(debug=True)