import csv
import requests
from bs4 import BeautifulSoup


def get_html(url):
    res = requests.get(url)
    return res.text

def get_total_pages(html):
    soup = BeautifulSoup(html, "html.parser")
    pages = soup.find('ul', class_ = "pagination").find_all('a')[-1].get('href')
    total_pages = pages.split('=')[-1]
    return int(total_pages) 

def write_csv(data):
    with open('kivano.csv', 'a') as file:
        writer = csv.writer(file)

        writer.writerow((data['title'], data['price'], data['image']))

def get_page_data(html):
    soup = BeautifulSoup(html, "html.parser")
    ads = soup.find('div', class_ = "list-view").find_all('div', class_ = "item product_listbox")
    
    for ad in ads:
        try:
            title = ad.find('div', class_ = "listbox_title").find('a').text.strip()
        except:
            title = ''
        
        try:
            price = ad.find('div', class_ = "listbox_price").find('strong').text.strip()
        except:
            price = ''
        
        try:
            images = ad.find('div', class_ = "listbox_img").find('img').get('src')
            image = 'https://www.kivano.kg' + images
        except:
            image = ''
        

        data = {'title': title, 'price': price, 'image': image}
        
        write_csv(data)
        

def main():
    main_url = "https://www.kivano.kg/mobilnye-telefony"
    page_url = "?page="
    html = get_html(main_url)

    total_pages = get_total_pages(html)

    for i in range(1, total_pages + 1):
        url_gen = main_url + page_url + str(i)
        page_html = get_html(url_gen)
        get_page_data(page_html)
        

if __name__ == '__main__':
    main()
