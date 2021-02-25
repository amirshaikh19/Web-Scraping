from urllib.request import urlopen
from bs4 import BeautifulSoup as soup
import re
import pandas as pd

url_to_scrape="http://books.toscrape.com/"

url_data = urlopen(url_to_scrape)

#print(type(url_data))
url_data_html = url_data.read()

#print(url_data_html) #-->not proper html


url_soup = soup(url_data_html,'html.parser')
#print(url_soup) #->proper html

li_ele = url_soup.findAll('li',{"class":"col-xs-6 col-sm-4 col-md-3 col-lg-3"})
#print(len(li_ele))

info=[]
for d in li_ele:
    book_heading = d.find('h3')
    book_price = d.find('p',{"class":"price_color"})
    book_in_stock =d.find('p',{"class":"instock availability"})
    book_image_link =d.findAll('img', {'src':re.compile('.jpg')})
    # print(book_heading.text)
    # for image in book_image_link:
    #      print((image['src']))
    
    
    info1=[]
    
    if book_heading is not None:
        info1.append(book_heading.text)
    else:
        info1.append("-----")
        
    if book_price is not None:
        info1.append(book_price.text)
    else:
        info1.append("-----")
        
    if book_in_stock is not None:
        info1.append((book_in_stock.text[:-1]).strip())
    else:
        info1.append("-----")
        
        
    if book_image_link is not None:
        # info1.append([print((image['src'])) for image in book_image_link])
        for image in book_image_link:
            info1.append((image['src']).strip())
    else:
        info1.append(("-----"))  
        
    info.append(info1)

df = pd.DataFrame(info,columns=['Title','Price','availability','link'])
df.to_csv('information.csv',index=False,encoding='utf-8')

df=pd.read_csv('information.csv')
print(df.shape)

    
print(df.head(10))








# url_li_ele=li_ele[0]

# book_heading = url_li_ele.findAll('h3')

# print(book_heading[0].text)

# book_price = url_li_ele.findAll('p',{"class":"price_color"})

# print(book_price[0].text)

# book_in_stock =url_li_ele.findAll('p',{"class":"instock availability"})

# print(book_in_stock[0].text[:-1])

# book_image_link =url_li_ele.findAll('img', {'src':re.compile('.jpg')})

# for image in book_image_link:
#     print((image['src']))
    
#@CODED BY amirshaikh19
    
