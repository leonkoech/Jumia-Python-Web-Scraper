import requests
import json
from bs4 import BeautifulSoup
import webbrowser
from notify_run import Notify
from subprocess import call
call('chmod +x backgroundruns.py',shell=True)
call('nohup python3 backgroundruns.py >/dev/null 2>&1 &',shell=True)
notify=Notify()
def backgroundrun(current,dip,link,description):
    #TO:DO 
    # if current price is less than or equal to dip send notification
    #start by checking the link and check the price
    #check link
    while(link!=''):
        page=requests.get(link)
        soup = BeautifulSoup(page.text, 'html.parser')
        #check price
        full_price = soup.find(class_="-b -ltr -tal -fs24").text.split(' ')
        withcomma=full_price[1].strip().split(',')
        pricek=withcomma[0].strip()
        price1=full_price[1].strip()
        price0=price1[-3:]
        pricefull=pricek+price0
        price=int(pricefull)
        while(price==current or price<current):
            print('message sent to device')
            notify.send('PRICE DROP:'+description,link)
            call('pkill -f backgroundruns.py',shell=True)
            exit()
            break
        else:
            exit()
    else:
        #if link is empty exit() or break
        call('pkill -f backgroundruns.py',shell=True)
        exit()
