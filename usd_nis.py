__author__ = 'davesave'


import requests
from bs4 import BeautifulSoup

def num(s):
    try:
        return int(s)
    except ValueError:
        try:
            return float(s)
        except ValueError:
            return ""


def get_blomberg_currency(full_url):

    r = requests.get(full_url)
    soup = BeautifulSoup(r.content)
    tag = soup.select(".price")[0]


    t = tag.text.replace(" ", "")
    currency=""

    for ttt in t.split("\n"):
        if ttt == "\n":
            continue

        if num(ttt)!='':
            currency = num(ttt)

    return str(currency)



url = "http://www.bloomberg.com/quote/"
end = "USDILS:CUR"

print ("Got Currency " + get_blomberg_currency(url+end) + " for " + end )







