from selenium import webdriver
from selenium.webdriver.common.by import By
from config import *
import database
import cur_date

#getting the list of SKU urls
def get_sku_urls(outer_url: str) -> list:
    
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(outer_url)
    
    try:
        pagen_len = driver.find_element(By.CLASS_NAME, 'pagination')
        pagen_len = int(pagen_len.text.split()[-3]) #получаем количество страниц для пагинации
    except:
        pagen_len = 1
    
    
    sku_url = [] #список для хранения адресов SKU
    
    #gathering the links of SKU's
    for i in range(1, pagen_len + 1):
        driver.get(f'{outer_url}?PAGEN_1={i}')
        links = driver.find_element(By.CLASS_NAME, 'catalog-item-table-view').find_elements(By.CLASS_NAME, 'item-title')
        for link in links:
            sku_url.append(link.get_attribute('href'))
    
    #sku_url = set(sku_url) #deleting the duplicates of links
    for sku in sku_url:
        print(sku)
    
    print(len(sku_url))
    return sku_url
    

def get_page_data(urls: list) -> dict:
    #the function is getting yhe list of SKU url and parsing the data
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    data= {}
    for url in urls:
        driver.get(url)
        sku_name = driver.find_element(By.CLASS_NAME, 'content').find_element(By.TAG_NAME, "h1").text
        article = driver.find_element(By.CLASS_NAME, 'content').find_element(By.CLASS_NAME, 'article').text.split()[1]
        try:
            current_price = int(driver.find_element(By.CLASS_NAME, 'price_buy_detail').find_element(By.ID, 'curPrice').text.strip(' руб').replace(' ', ''))
        except:
            current_price = 0
        type = url.replace('https://www.tehnovideo39.ru/','').split("/")[0]
        model = ''
        for symbol in sku_name:
            symbol_table = 'abcdefghijklmnopqrstuvwxyz1234567890'
            symbol_to_replace = '\/._-*+@#$%& '
            if symbol.lower() in symbol_table:
                model+= symbol.lower()
            elif symbol in symbol_to_replace:
                model+= ' '
        model = model.strip()  
        
        data = {
            'date' : cur_date.get_current_datetime(),
            'url' : url,
            'sku_name' : sku_name,
            'article'  : article, 
            'current_price' : current_price,
            'type' : type,
            'model' : model,
        }
        print(data)
        database.write_to_database(data)
    return data
    


def main():

    url_list = [
        "https://www.tehnovideo39.ru/stiralnye_mashiny/",
        "https://www.tehnovideo39.ru/otparivateli/",
        "https://www.tehnovideo39.ru/monitory/",
        "https://www.tehnovideo39.ru/smartfony/",
    ]
    
    for url in url_list:
        get_page_data(get_sku_urls(url))
    

if __name__ == '__main__':
    main()
    

