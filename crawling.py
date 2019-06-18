from selenium import webdriver
from bs4 import BeautifulSoup
from urllib import request
from time import sleep
import re

path = './chromedriver.exe'
driver = webdriver.Chrome(path)
driver.implicitly_wait(3) # 암묵적으로 웹 자원을 (최대) 3초 기다리기
driver.get('https://nid.naver.com/nidlogin.login')
# Login
id = ''
pw = ''
#id, pw를 지웠으므로 본 코드는 동작하지 않습니다.
driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/span[2]/a').click()
driver.find_element_by_xpath('//*[@id="PM_ID_ct"]/div[1]/div[2]/div[1]/ul[1]/li[4]/a/span[1]').click()
driver.find_element_by_xpath('//*[@id="nx_query"]').send_keys('콘돔 지갑 보관')
driver.find_element_by_xpath('//*[@id="topSearch"]/fieldset/div/a[2]/span').click()
#지식인 검색결과 진입
url_list = []
output = open('output_asdf.txt', 'w', encoding='utf8')
first_page_flag = True
for cnt in range(2):
    for i in range(1, 11):
        if first_page_flag:
            driver.find_element_by_xpath('//*[@id="s_content"]/div[3]/div[2]/a[' + str(i) + ']').click()
        else:
            driver.find_element_by_xpath('//*[@id="s_content"]/div[3]/div[2]/a[' + str(i+1) + ']').click()
        result_page = driver.page_source
        soup = BeautifulSoup(result_page, 'html.parser')
        l = soup.find_all('a', {'class': "_nclicks:kin.txt _searchListTitleAnchor"})
        for i in l:
            i = str(i)
            i = i.replace('&amp', '&')
            i = i.replace(';', '')
            regex = re.compile('https.*spq=\d')
            i = regex.search(i).group()
            url_list.append(i)
    first_page_flag = False
url_list = set(url_list)
cnt = 0
for url in url_list:
    driver.get(url)
    page = driver.page_source
    soup = BeautifulSoup(page, 'html.parser')
    contents = soup.select('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default-old > div.c-heading__content')
    if len(contents) == 0:
        contents = soup.select('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple-old > div.c-heading__content')
    if len(contents) == 0:
        contents = soup.select('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--multiple > div.c-heading__title > div > div.title')
    if len(contents) == 0:
        contents = soup.select('#content > div.question-content > div > div.c-heading._questionContentsArea.c-heading--default > div.c-heading__title > div > div.title')
    if len(contents) == 0:
        continue
    tmp = contents[0].text
    tmp = re.sub('\s\s+', ' ', tmp)
    tmp += '\n'
    if '콘돔' in tmp:
        cnt += 1
        print('condom cnt: ', cnt)
        output.write(tmp)
driver.quit()
output.close()






