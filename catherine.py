from selenium import webdriver
from bs4 import BeautifulSoup
import re
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

x=0

for page_num in range(1,4):
    catalog_keyword = "에어컨" #에어컨 세탁기 냉장고 등등 키워드 골라 넣으면 엑셀 파일 자동 생성
    enuri_url = "http://www.enuri.com/list.jsp?cate=0602&from=search&islist=Y&skeyword="+catalog_keyword+"&cate_keyword=Y&hyphen_2=false&page="+str(page_num)
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
    all_title = soup.find_all('a',{'class':{'detailMultiLink prodName'}})
    product_omitted_seventh_list=soup.find_all('li',{'class':'prodItem wide plustop'})

    if not product_omitted_seventh_list:
        print("list is empty")
    else:
        seventh_soup = product_omitted_seventh_list[0]
        print(seventh_soup)
        product_list.insert(6,seventh_soup)

    index = 0
    while index < len(product_list):
        #write individual title in a cell
        individual_soup = product_list[index]
        individual_title = individual_soup.find('div',{'class':{'sp_title'}}).text
        sheet1.write(x+1,1,individual_title)
        print(individual_title)

        #write individual price in a cell
        individual_price = individual_soup.find('span',{'class':{'don groupModelLink'}})
        #print(individual_price)
        bolded_price =  individual_price.find('b')
        stringfied_individual_price = re.sub("[^0-9]", "", bolded_price.text)
        sheet1.write(x+1,2,stringfied_individual_price)
        print(stringfied_individual_price)

        #prepare for next iteration
        index +=1
        x +=1
        wb.save(catalog_keyword+ ' Listup.xls')
