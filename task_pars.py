import csv
import requests
from bs4 import BeautifulSoup

main_url = 'https://www.kivano.kg/mobilnye-telefony'

def get_html(url):
    '''html код сайта в текстовом виде'''
    res = requests.get(url)
    return res.text


def get_total_pages(html):
    soup = BeautifulSoup(html, 'html.parser')
    pages = soup.find('div', class_ = 'pager-wrap').find_all('a').get('href')
    total_page = pages.split('=')[1]
    return int(total_page)
       

def get_data_page(html):
    soup = BeautifulSoup(html, 'html.parser')
    all_page = soup.find_all('div', class_ = 'item product_listbox')
    all_info = []

    for page in all_page:
        try:
            title = page.find('div', class_ = 'listbox_title').find('a').get('href')
            title_full = 'https://www.kivano.kg' + title
        except:
            title_full = ''
        try:
            price = page.find('div', class_ = 'listbox_price').get('strong')
        except:
            price = ''
        try:
            img = page.find('div', class_ = 'listbox_img').get('img')
            img_full = 'https://www.kivano.kg' + img    
        except:
            img_full = ''
        
        data = {'title': title_full,
                'price': price,
                'image': img_full
                }
        all_info.append(data)

        write_csv(data)


def write_csv(data):
    with open('kivano.csv', 'a') as file:
        writer = csv.writer(file)
        
        write.writerow([data['title'],
                        data['price'],
                        data['image']
                        ])


def main():
    html = get_html(main_url)
    for page in range(1, get_total_pages):

        data_page = get_data_page(html)
        write_csv(data_page)


if __name__ == '__main__':              # точка входа
    main()









# def main():
#     main_url = 'https://www.kivano.kg/mobilnye-telefony'
#     base_url =

# if __name__ == '__main__':              # точка входа
#     main()



# def get_img(html):
#     '''из общего кода берет только класс и находит там все '''
#     soup = BeautifulSoup(html, 'html.parser')
#     link_img = soup.find('div', class_ = 'listbox_img').find_all('img')
#     links_img = []

#     for img in link_img:
#         link = 'https://www.kivano.kg' + link_img
#         links_img.append(link)
#     # return links_img
#     print(links_img)

# def get_title(html):
#     '''из общего кода берет только класс и находит там все '''
#     soup = BeautifulSoup(html, 'html.parser')
#     titles = soup.find('div', class_ = 'listbox_title').find_all('strong')  
#     links_title = []

#     for title in titles:
#         title_url = title.find('a').get('href')
#         full = 'https://www.kivano.kg' + title_url
#         links_title.append(full)
#     return links_title

# def get_price(html):
#     '''из общего кода берет только класс и находит там все '''
#     soup = BeautifulSoup(html, 'html.parser')
#     prices = soup.find('div', class_ = 'listbox_price').find_all('strong')  
#     links_price = []

#     for price in prices:
#         price_url = price.get('strong')
#         full = 'https://www.kivano.kg' + price_url
#         links_title.append(full)
#     return links_price



# def write_csv(data):
#     '''записывает на csv файл'''
#     with open('telefon.csv', 'a') as file:
#         writer = csv.writer(file)
#         writer.writerow([data['name'], data['number']])
#         print([data['name'], data['number']], 'parsed')



# if __name__ == '__main__':              # точка входа
#     main()