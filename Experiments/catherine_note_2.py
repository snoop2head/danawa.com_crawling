from selenium import webdriver
from bs4 import BeautifulSoup
import re
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

x=0

product_keyword = "냉장고" #에어컨 세탁기 냉장고 등등이 20종류.
enuri_url = "http://www.enuri.com/list.jsp?cate=0602&from=search&islist=Y&skeyword="+product_keyword+"&cate_keyword=Y&hyphen_2=false&page="+str(2)
print(enuri_url)

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver", chrome_options=options)
#print(driver.find_element_by_xpath("//span[@class='jungoCheck noShowNormalProd unchk']").text)
driver.implicitly_wait(10) # waiting web source for three seconds implicitly

# get url
driver.get(enuri_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#parsing information
product_list = soup.find_all('li',{'class':'prodItem wide'})
product_omitted_list=soup.find_all('li',{'class':'prodItem wide plustop'})
all_title = soup.find_all('a',{'class':{'detailMultiLink prodName'}})


individual_soup = product_list[6]
#print(individual_soup)
seventh_soup = product_omitted_list[0]
print(seventh_soup)

#write individual price in a cell
#individual_title = individual_soup.find('div',{'class':{'sp_title'}}).text
#print(individual_title)
#individual_price = individual_soup.find('span',{'class':{'don groupModelLink'}})
#print(individual_price)

#bolded_price =  individual_price.find('b')
#stringfied_individual_price = re.sub("[^0-9]", "", bolded_price.text)

#print(stringfied_individual_price)
