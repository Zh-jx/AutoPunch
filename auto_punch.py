from selenium import webdriver
import time
import os, json
from selenium.webdriver.chrome.service import Service
#主要是selenium的应用，模拟用户访问浏览器的一些操作
def getinfo():
    f = open("/Users/wq/Desktop/userinfo.json",encoding="utf-8")#放置账号信息的json路径，用的是mac上面的绝对路径
    setting = json.load(f)
    useraccount = setting['useraccount']
    for i in range(len(useraccount)):
        username.append(useraccount[i]['username'])
        password.append(useraccount[i]['password'])
    print(username)
    print(password)
    
username=[]
password=[]

def punch(StudentId, Name):
    c_service = Service('/Users/wq//Downloads/chromedriver')
    c_service.command_line_args()
    c_service.start()
    driver=webdriver.Chrome('/Users/wq/Downloads/chromedriver') # 选择Chrome浏览器
    driver.get('http://xsc.sicau.edu.cn/SPCP') # 打开网站
    #采用xpath定位
    result = driver.find_element_by_xpath('//*[@id="code-box"]')
    text = result.text
    driver.find_element_by_xpath('//*[@id="StudentId"]').click()
    driver.find_element_by_xpath('//*[@id="StudentId"]').send_keys(StudentId)
    driver.find_element_by_xpath('//*[@id="Name"]').click()
    driver.find_element_by_xpath('//*[@id="Name"]').send_keys(Name)
    driver.find_element_by_xpath('//*[@id="codeInput"]').click()
    driver.find_element_by_xpath('//*[@id="codeInput"]').send_keys(text)
    driver.find_element_by_xpath('//*[@id="Submit"]').click()
    driver.find_element_by_xpath('//*[@id="platfrom2"]').click()
    try:
        driver.find_element_by_xpath('//*[@id="ckCLS"]').click()
        driver.find_element_by_xpath('//*[@id="SaveBtnDiv"]/button').click() 
    except:
        driver.find_element_by_xpath('//*[@id="layui-layer1"]/div[3]/a').click()
    driver.quit()
    c_service.stop()

if __name__ == "__main__":
    getinfo()#导入账号信息
    for i in range(len(username)):
        punch(username[i],password[i])
        #下面用的依然是mac上面的绝对路径，因为搭配crontab实现自动执行需要都是绝对路径
        with open("/Users/wq/Desktop/AutoTask.txt", "a") as f:
            f.write(username[i] + "已打卡！" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + '\n')
            f.close()


