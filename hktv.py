import requests
import time
from datetime import datetime
from bs4 import BeautifulSoup
from requests.exceptions import Timeout
from dotenv import dotenv_values
from sendmail import send_alert


def read_links():
    global URLS
    URLS = []
    f = open("links.txt", "r", encoding="utf8")
    lines = f.readlines()
    for line in lines:
        p_line = line.strip()
        if p_line.startswith('https'):
            URLS.append(p_line)

def get_page_soup(url):
    try:
        html = ''
        page = requests.get(url, headers=HEADERS, timeout=30)
        if page:
            html = page.content
    except Timeout:
        print('timeout')
    except:
        print('connection error')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def stock_check():
    urls_to_check = [url for url in URLS if url not in F_URLS]
    no_of_links = len(urls_to_check)
    print(datetime.now())
    for url in urls_to_check:
        print("checking {} of {} - ".format(urls_to_check.index(url)+1, no_of_links), end='')
        soup = get_page_soup(url)
        button = soup.find('button', class_="sepaButton addToCartButton large")
        not_sale = soup.find('error', class_="error")
        product_name = soup.find('h1', class_="last").string
        if button:
            butt_text = button.find('span').get_text()
            if butt_text == "加入購物車":
                print('in stock, sending alert...')
                send_alert(product_name, url)
                F_URLS.append(url)
        elif not_sale:
            print('remove the link below:')
            print(url)
        else:
            print('out of stock')
            time.sleep(3)
    print('\n')


if __name__ == '__main__':
    config = dotenv_values('.env')
    HEADERS = {}
    HEADERS["user-agent"] = config['USER_AGENT']
    CHECK_INTERVAL = int(config['CHECK_INTERVAL'])
    URLS = [] # store all urls in the links file
    F_URLS = [] # store urls that alert has been sent out

    while(True):
        read_links()
        stock_check()
        time.sleep(CHECK_INTERVAL*60)
