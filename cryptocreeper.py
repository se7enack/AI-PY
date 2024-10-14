#!/usr/bin/env python3

from tkinter import *
import locale
import json
import requests
import webbrowser


url = "https://api.coincap.io/v2/assets"

try:
    req = requests.get(url, verify=False)
    x = json.loads(req.text)
except:
    print("exit")
    exit(0)
  

def callback():
   showsyms()
   webbrowser.open_new_tab(asseturl)


def showsyms():
    values = []
    for y in range(len(x['data'])):
         values.append(x['data'][y]['symbol'])
    values = sorted(values)
    return values


options = showsyms()


def makeusd(cash):
    print(cash)
    x = str(cash).startswith("0.00")
    if x == True:
        usd = f"${cash}"
    else:
        usd = '${:,.2f}'.format(float(cash))
    return(usd)


def update(txt):
    myLabel.configure(text=txt)    
    
    
def showsyms():
    global asseturl
    try:
        req = requests.get(url, verify=False)
        x = json.loads(req.text)
        for y in range(len(x['data'])):
            if x['data'][y]['symbol'] == clicked.get(): 
                name = x['data'][y]['name']
                symbol = x['data'][y]['symbol']
                asseturl = f"https://www.blockchain.com/explorer/assets/{symbol}"
                priceUsd = float(x['data'][y]['priceUsd'])
                changePercent24Hr = str(round(float(x['data'][y]['changePercent24Hr']), 2))
                if changePercent24Hr.startswith('-'):
                    p = f"Down {changePercent24Hr}% in the last 24 hours"
                else:
                    p = f"Up {changePercent24Hr}% in the last 24 hours"
                price = makeusd(priceUsd)
                update(f"\n{name}: {price}\n\n{p}\n")
    except:
        exit(1)

root = Tk()
root.title("Crypto Creeper")
root.geometry("250x200")

myLabel = Label(root, text='\n\nPick a Crypto\n\n')
myLabel.pack()

clicked = StringVar()
clicked.set('BTC')

drop = OptionMenu(root, clicked, *options)
drop.pack()

Button(root, text=" Update ", command=showsyms).pack()
Button(root, text="Explorer", command=callback).pack()

root.mainloop()
