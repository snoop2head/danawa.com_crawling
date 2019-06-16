from selenium import webdriver
from bs4 import BeautifulSoup
import re
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)

x=0

for page_num in range(1,4):
    product_keyword = "냉장고" #에어컨 세탁기 냉장고 등등이 20종류.
    enuri_url = "http://www.enuri.com/list.jsp?cate=0602&from=search&islist=Y&skeyword="+product_keyword+"&cate_keyword=Y&hyphen_2=false&page="+str(page_num)
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
        stringfied_individual_price = re.sub("[^0-9]", "", individual_price.text)
        sheet1.write(x+1,2,stringfied_individual_price)
        print(stringfied_individual_price)

        #prepare for next iteration
        index +=1
        x +=1
        wb.save('냉장고12.xls')




#individual_title = all_title[index].text
#print(individual_title)
#sheet1.write(x+1,1,individual_title)

#print(individual_soup)
#print(len(individual_soup))
#print(type(individual_soup))
#print(individual_soup[0])
#print(individual_soup[1])
#print(individual_soup[2])

# longmin_individual_price = soup.find('dd',{'class':{'groupModelItem'}})['longminprice']
#print(longmin_individual_price)

#click on 중고
#<span class="jungoCheck noShowNormalProd unchk"><input type="checkbox" />중고/렌탈 제외</span>
#element = driver.find_element_by_xpath("//input[@type='checkbox']")
#element.click()
#wait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//span[text()='중고/렌탈 제외']"))).click()
#python_button.click()
#element = driver.find_element_by_id("gb_23")
#element.click()
#checkbox = driver.findElement(By.XPATH, "//span[@class='jungoCheck noShowNormalProd unchk']")
#checkbox.click()
#driver.find_element_by_tag_name("span")[0].click()
#wait = WebDriverWait(driver, 10)
#element = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@id='listShowTypeDiv']/div/span[1]")))
#element.click()

#product_division=soup.find_all('li',{'ingimodelno':'31392490'})
#all_price = soup.find_all('span',{'class':{'don groupModelLink'}})
#all_price_2 = soup.find_all('dd',{'class':{'groupModelItem'}})

#print(product_list[1])

#print(product_division)
#print(all_title)
#print(all_price)

