from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def ccb():

    ccburl = "http://forex1.ccb.com/cn/forex/exchange-quotations.html"

    driver = webdriver.Edge()
    driver.get(ccburl)

    driver.implicitly_wait(1)

    elem = driver.find_element(By.ID, "jshckpj")
    elem = elem.find_elements(By.TAG_NAME, "ul")
    elemlist = []

    for i in elem:
        i = i.find_elements(By.TAG_NAME, "li")

        datalist = []
        for j in i:
            datalist.append(j.get_attribute("innerText"))
        elemlist.append(datalist)

    driver.close()

    return elemlist


def icbc():

    icbcurl = "http://www.icbc.com.cn/forex/foreignEx/forex.html"

    driver = webdriver.Edge()
    driver.get(icbcurl)

    driver.implicitly_wait(1)

    elem = driver.find_element(By.TAG_NAME, "tbody")
    elem = elem.find_elements(By.TAG_NAME, "tr")
    elemlist = []

    for i in elem:
        i = i.find_elements(By.TAG_NAME, "td")

        datalist = []
        for j in i:
            datalist.append(j.get_attribute("innerText"))
        elemlist.append(datalist)

    driver.close()

    return elemlist


def abc():

    abcurl = "http://ewealth.abchina.com/ForeignExchange/ListPrice/"

    driver = webdriver.Edge()
    driver.get(abcurl)

    driver.implicitly_wait(1)

    elem = driver.find_element(By.CLASS_NAME, "bindCon")
    elem = elem.find_elements(By.TAG_NAME, "tr")
    elemlist = []

    for i in elem:
        i = i.find_elements(By.TAG_NAME, "td")

        datalist = []
        for j in i:
            datalist.append(j.get_attribute("innerText"))
        elemlist.append(datalist)

    elemlist = elemlist[0:-1:2]

    driver.close()

    return elemlist


def boc():

    bocurl = "https://www.bankofchina.com/sourcedb/whpj/index.html"

    driver = webdriver.Edge()
    driver.get(bocurl)

    driver.implicitly_wait(1)

    elem = driver.find_elements(By.TAG_NAME, "tbody")[1]
    elem = elem.find_elements(By.TAG_NAME, "tr")
    elemlist = []

    for i in elem:
        i = i.find_elements(By.TAG_NAME, "td")

        datalist = []
        for j in i:
            datalist.append(j.get_attribute("innerText"))
        elemlist.append(datalist)

    driver.close()

    elemlist=elemlist[1:]

    return elemlist

s=str([ccb(),icbc(),abc(),boc()])

with open("D:/Desktop/a/data","w",encoding="utf-8") as file:
    file.write(s)

