#[<li cate="06020409" class="prodItem wide" id="modelno_31392490" ingimodelno="31392490"><div class="sp_title"><strong class="tit"><a class="detailMultiLink prodName" href="JavaScript:"><em>2위</em> LG전자 디오스 S831S30</a></strong></div><div class="thum_area"> <a class="detailMultiLink" href="javascript:"> <div class="thumb_layer"><button class="thumb_zoom" onclick="onoff('zoom')" type="button">확대</button><button class="thumb_compare" onclick="onoff('combox')" type="button">비교</button><button class="thumb_zzim" type="button">찜</button> </div><div class="img_tag"><div><div class="blue"><span>821L</span></div></div></div><img class="listShowImg" onerror="this.src='http://imgenuri.enuri.gscdn.com/images/home/thum_none.jpg'" src="http://photo3.enuri.com/data/images/service/img_300/31392000/31392490.jpg"/> </a></div><div class="info_area"> <div class="case_price"> <dl class="option"> <dt><b>18년4월</b> 등록</dt><dd class="groupModelItem" id="modelnoGroup_26975373" lngdeliveryprice="1141090" longminprice="1141090"> <span class="groupTitle size groupModelLink" image="" kbno="0">일반</span> <span class="don groupModelLink"><b>1,141,090</b>원</span> <span class="chk_zzim"><a class="groupModelLink" href="JavaScript:" title="업체수">334</a><span class="oldCompZzimChk unchk"><input type="checkbox"/></span></span></dd><dd class="groupModelItem" id="modelnoGroup_31392490" lngdeliveryprice="1129880" longminprice="1129880"> <span class="groupTitle size groupModelLink" image="" kbno="0">(대량)사업자전용</span> <span class="don groupModelLink"><b>1,129,880</b>원</span> <span class="chk_zzim"><a class="groupModelLink" href="JavaScript:" title="업체수">1</a><span class="oldCompZzimChk unchk"><input type="checkbox"/></span></span></dd> </dl> </div> <div class="info_detail"> <dl class="prodtip"> <dt>TIP</dt> <dd class="keyword2">디오스 매직스페이스 양문형 냉장고!</dd> </dl> <div class="summary"><a class="dicLink att_txt_188285_7" href="JavaScript:">양문형냉장고</a><em>|</em>2도어<em>|</em><a class="dicLink att_txt_188442_0" href="JavaScript:">용량</a>:821L<em>|</em>냉장실:523L<em>|</em>냉동실:298L<em>|</em>홈바:<a class="dicLink att_txt_188588_4" href="JavaScript:">매직스페이스</a><em>|</em>자동정온<em>|</em><a class="dicLink att_txt_188365_30" href="JavaScript:">신선야채실</a><em>|</em><a class="dicLink att_txt_188256_7" href="JavaScript:">TOPLED라이팅</a><em>|</em><a class="dicLink att_txt_188407_15" href="JavaScript:">도어아이스메이커</a><em>|</em><a class="dicLink att_txt_195892_3" href="JavaScript:">무선랜(WiFi)</a><em>|</em><a class="dicLink att_txt_195892_7" href="JavaScript:">스마트진단</a><em>|</em><a class="dicLink att_txt_188321_22" href="JavaScript:">Big매직디스플레이</a><em>|</em>스퀘어핸들<em>|</em>재질:메탈<em>|</em>색상:퓨어<em>|</em><a class="dicLink att_txt_188453_5" href="JavaScript:">5세대리니어컴프레서</a><em>|</em><a class="dicLink att_txt_188385_0" href="JavaScript:">소비전력</a>:29.2kW(월)<em>|</em><a class="dicLink att_txt_188417_0" href="JavaScript:">에너지효율</a>:2등급<em>|</em><a class="dicLink att_txt_188469_0" href="JavaScript:">크기</a>:91.2 x 179 x 92.7cm   </div> <span class="etc_txt"> <a class="detailMultiLinkBBSOpen" href="javascript:">상품평<em class="kbnum">5,531</em><span class="star_graph"><span style="width:96%">별점</span></span></a><span class="bar"></span><a class="com reSearch" code="1" href="javascript:void(0);">LG전자</a><span class="bar"></span><a class="shareDivShow" href="javascript:">공유</a> <a class="eMoneyLink save_per" href="JavaScript:">적립</a> </span></div></div></li>]


from selenium import webdriver
from bs4 import BeautifulSoup
import re
from xlwt import Workbook

wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1', cell_overwrite_ok=True)


page_num = str(1) #3페이지까지 하면 됨.
product_keyword = "냉장고" #에어컨 세탁기 냉장고 등등이 20종류.
enuri_url = "http://www.enuri.com/list.jsp?cate=0602&from=search&islist=Y&skeyword="+product_keyword+"&cate_keyword=Y&hyphen_2=false&page="+page_num

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(r"C:\Users\pc\Desktop\chromedriver", chrome_options=options)
driver.implicitly_wait(10) # waiting web source for three seconds implicitly

# get url
driver.get(enuri_url)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

#print(soup)

#parsing information
all_title = soup.find_all('a',{'class':{'detailMultiLink prodName'}})
all_price = soup.find_all('span',{'class':{'don groupModelLink'}})

#print(all_title)

b =[]

def remove_tag(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext

for i in all_title:
    individual_title = i.text
    print(individual_title)

x=0

for i in all_title:
    individual_title = i.text
    print(individual_title)
    x +=1
    sheet1.write(x+1,1,individual_title)
    wb.save('냉장고.xls')


'''
for j in all_price:
    individual_price = re.sub("[^0-9]", "", j.text)
    print(individual_price)
    x +=1
    sheet1.write(x+1,2,individual_title)
    wb.save('냉장고.xls')
'''

