import requests
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver.support.select import Select
import time
from bs4 import BeautifulSoup
import sys
driver = webdriver.Chrome()
link = "https://translate.google.com/"
driver.get(link)
time.sleep(2)
# detectLanguageButton = driver.find_element("class", "VfPpkd-YVzG2b")
# detectLanguageButton.click()
newLanguage = driver.find_element("class", "VfPpkd-Bz112c-LgbsSe VfPpkd-Bz112c-LgbsSe-OWXEXe-e5LLRc-SxQuSe yHy1rc eT1oJ mN1ivc qiN4Vb KY3GZb szLmtb")
newLanguage.click()
editText = driver.find_element("class", "yFQBKb")
editText.send_keys("Japanese" + keys.Enter)
originalRecipe = open("C:\\Users\\monke\\PycharmProjects\\WebScraper\\Apple-Berry Pie.txt", "r")
originalRecipeInput = originalRecipe.read()
originalRecipe.close()
textInput = driver.find_element("class", "er8xn")
textInput.send_keys(originalRecipeInput)
textOutput = driver.find_element()
soup = BeautifulSoup(link.content, "html.parser")
output = soup.find(Class="HwtZe")
print(output)

