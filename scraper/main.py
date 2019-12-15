import requests
import json
from bs4 import BeautifulSoup

sp='            '
print('choose a category by number: \n [1] phones and tablets ',sp,'[2] electronics',sp,'[3] computing')
print(' [4] home and office',sp,'[5] health and beauty',sp,'[6] grocery \n [7] carrefour shop',sp,'[8] baby products',sp,'[9] fashion')
print(' [0] search whole website')
category=int(input())
def pageandsoup(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    item = soup.find(class_="products -mabaya")
    itemlist = item.find_all(class_="sku -gallery")
    print('items count = ',len(itemlist))
    data=[]
    for item in itemlist:
        Jmitem={}
        title=item.find(class_='title')
        brand=title.find(class_='brand').text.strip()
        description=title.find(class_='name').text.strip()
        pricecontainer=item.find(class_='price-container clearfix')
        saleflag=pricecontainer.find(class_='price-box ri')
        full_price=saleflag.find(class_='price').text.split(' ')
        withcomma=full_price[1].strip().split(',')
        pricek=withcomma[0].strip()
        price1=full_price[1].strip()
        price0=price1[-3:]
        # print(price0)
        pricefull=pricek+price0
        # print(pricefull)
        price=int(pricefull)
        link=item.find('a',href=True)
        Jmitem['price']=str(price).strip()
        Jmitem['description']=str(description).strip()
        Jmitem['brand']=str(brand).strip()
        Jmitem['url']=link['href'].strip()
        print ("URL:", link['href'])
        print(price)
        data.append(Jmitem)
    with open("data_file.json", "w") as writeJSON:
        json.dump(data, writeJSON,indent = 4, ensure_ascii=False,sort_keys=True)
def searchweb():
    print('enter product name:')
    querytxt = input()
    print('enter maximum price of item')
    #remove commas
    maxJmprice = input().replace(',','')
    #remove spaces
    maxPrice=maxJmprice.strip()
    print('enter minimum price of item')
    minJmprice = input().replace(',','')
    minPrice=minJmprice.strip()
    query=querytxt.replace(' ','%20')
    page = requests.get('https://www.jumia.co.ke/catalog/?q='+query+'&price='+minPrice+'-'+maxPrice)
     
    print('https://www.jumia.co.ke/catalog/?q='+query+'&price='+minJmprice+'-'+maxJmprice)
    pageandsoup(page)
def setpagerequest(link):
    print('enter maximum price of item')
    maxJmprice = input().replace(',','')
    maxPrice=maxJmprice.strip()
    print('enter minimum price of item')
    minJmprice = input().replace(',','')
    minPrice=minJmprice.strip()
    page = requests.get('https://www.jumia.co.ke/'+link+'?price='+minPrice+'-'+maxPrice)
    pageandsoup(page)
def switch_demo(argument):
    if(argument==1):
        setpagerequest('phones-tablets/')
    elif(argument==2):
        setpagerequest('electronics/'),
    elif(argument==3):
        setpagerequest('computing/'),
    elif(argument==4):
        setpagerequest('home-office/'),
    elif(argument==5):
        setpagerequest('health-beauty/'),
    elif(argument==6):
        setpagerequest('grocery/'),
    elif(argument==7):
        setpagerequest('carrefour-shop/'),
    elif(argument==8):
        setpagerequest('baby-products/'),
    elif(argument==9):
        setpagerequest('fashion/'),
    elif(argument==0):
        searchweb(),
    else:
        print ("Invalid category.\nPlease try again")
#this is called first
switch_demo(category)
