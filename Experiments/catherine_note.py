
'''
for i in all_title:
    individual_title = i.text
    print(individual_title)
    x +=1
    sheet1.write(x+1,1,individual_title)
    wb.save('냉장고2.xls')
'''


'''
for j in all_price:
    individual_price = re.sub("[^0-9]", "", j.text)
    print(individual_price)
    x +=1
    sheet1.write(x+1,2,individual_title)
    wb.save('냉장고.xls')

b =[]

def remove_tag(content):
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', content)
    return cleantext

'''



