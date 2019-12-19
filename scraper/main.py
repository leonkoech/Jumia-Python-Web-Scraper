import requests
import json
from bs4 import BeautifulSoup
import webbrowser
import backgroundruns
from notify_run import Notify
from subprocess import call

notify=Notify()
sp='            '
print('choose a category by number: \n [1] phones and tablets ',sp,'[2] electronics',sp,'[3] computing')
print(' [4] home and office',sp,'[5] health and beauty',sp,'[6] grocery \n [7] carrefour shop',sp,'[8] baby products',sp,'[9] fashion')
print(' [0] search whole website',sp,'[11]observe product')
argument=int(input())
print('if prompted to Overwrite existing configuration press Y\n')
notifylink=notify.register().endpoint
print(notifylink)
def pageandsoup(page):
    soup = BeautifulSoup(page.text, 'html.parser')
    # print(soup)
    item = soup.find(class_="products -mabaya")
    try:
        itemlist = item.find_all(class_="sku -gallery")
    except AttributeError:
        print('\n\nError: Product count is 0.\n       Please check the price range and retry')
        exit()
    print('product count = ',len(itemlist))
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
        pricefull=pricek+price0
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
    print('are these the products requested:Y/n')
    #wrong input
    if(input().capitalize()=='Y'):
        print("please enter the price of the product you've selected:\n")
        pricei=int(input())
        pricestr=str(pricei)
        print('enter price you are waiting for:\n')
        dip=int(input())
        database = "data_file.json"
        data = json.loads(open(database).read())
        for i in data:
            if i['price'] == pricestr:
                print(i['brand'])
                print(i['description'])
                print(i['url'])
                print('Is this the product?Y/n')
                if(input().upper()=='Y'):
                    print('click on subscribe  to receive a notification once the product of the price dips')
                    print('note: this process python code has to run in the background. so do not switch off your device.')
                    print('and if you do please rerun this python code')
                    print('and you can send this link to as many devices as needed')
                    print('\nopen link .....\n')
                    webbrowser.open(notifylink)
                    print('have you opened the link and subscribed?Y/n\n')
                    if(input().upper()=='Y'):
                        #install notify
                        #call('pip install notify',shell=True)
                        print('\n\nprocess started....\n\n')
                        backgroundruns.backgroundrun(price,dip,str(i['url']),str(i['description']))
                        print('package will check product on background and will send notifications to subscribed devices')
                        print('\n\nTo kill background process run pkill -f backgroundruns.py\n\n')
                        exit()
                    if(input().lower()=='n'):
                        print('\n\nError: Please open link and subscribe first')
                        exit()
                elif(input().lower()=='n'):
                    print('\n\nError: Wrong product detected')
                    exit()
                else:
                    print('wrong input')
                    exit()

def searchweb():
    print('enter product name:')
    querytxt = input()
    print('enter maximum price of item WITHOUT COMMAS')
    #remove commas
    maxPrice = int(input())
    maxPricestr=str(maxPrice)
    #remove spaces
    print('enter minimum price of item WITHOUT COMMAS')
    minPrice = int(input())
    minPricestr=str(minPrice)
    if(maxPrice<minPrice):
        print('\n\nError: Maximum price cannot be less than minimum price')
        exit()
    elif(maxPrice==minPrice):
        print('Error: Maximum and minimum price cannot be equal')
        exit()
    else:
        query=querytxt.replace(' ','%20')
        page = requests.get('https://www.jumia.co.ke/catalog/?q='+query+'&price='+minPricestr+'-'+maxPricestr)
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
elif(argument==11):
    searchweb(),
else:
    print ("Invalid category.\nPlease try again")


    
