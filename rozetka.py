from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from config import *
import database
import cur_date
import time

#getting the list of SKU urls
def get_sku_urls(outer_url: str) -> list:
    
    
    
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:84.0) Gecko/20100101 Firefox/84.0")
    options.add_argument("--disable-blink-features=AutomationControlled")
    driver = webdriver.Chrome(options=options)
    
    driver.maximize_window()
    
    driver.get(outer_url)
    
    #geting number of pagination pages
    try:
        pagen_len = int(driver.find_element(By.CLASS_NAME, 'pages').text.split()[-1])
    except:
        pagen_len = 1
    
    sku_url = [] #список для хранения адресов SKU
    
    #gathering the links of SKU's
    for i in range(1, pagen_len + 1):
        driver.get(f'{outer_url}page-{i}/')
        links = driver.find_elements(By.CLASS_NAME, 'item')
        for link in links:
            print(link.text)
            sku_url.append(link.get_attribute('href'))
    
    for sku in sku_url:
        print(sku)
    """
    print(len(sku_url)) #qty of sku in category
    return sku_url
    
def get_page_data(urls: list) -> dict:
    #the function is getting the list of SKU url and parsing the data
    driver = webdriver.Chrome()
    driver.maximize_window()
    
    data= {}
    for url in urls:
        driver.get(url)
        sku_name = driver.find_element(By.TAG_NAME, "h1").text
        try:
            article = driver.find_element(By.XPATH, '//*[@id="content"]/div[1]/div[1]/div[1]/div[3]/div[2]/span').text 
        except:
            article = ''
        try:
            current_price = int(driver.find_element(By.ID, '_price').text.replace(',-', '').replace('Цена: ', '').replace(' ', '').strip())
        except:
            current_price = 0
        type = url.replace('https://baltmaximus.com/','').split("/")[0]
        
        model = ''
        symbol_table = 'abcdefghijklmnopqrstuvwxyz1234567890'
        symbol_to_replace = '\/._-*+@#$%& '
        for symbol in sku_name:
            if symbol.lower() in symbol_table:
                model += symbol.lower()
            elif symbol in symbol_to_replace:
                model += ' '
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
    """
def main():

    url_list = [
        "https://www.rozetka39.ru/tehnika/krupnaya_bitovaya_tehnika/stiralnie_mashini/",
        #"https://www.rozetka39.ru/tehnika/chistota_i_poryadok/otparivateli/",
        #"https://www.rozetka39.ru/noutbuki_i_komputeri/monitori/",
        #"https://www.rozetka39.ru/telefoni_i_plansheti/smartfoni_i_telefoni/tip_smartfon/",
    ]
    
    for url in url_list:
        
        get_sku_urls(url)

if __name__ == '__main__':
    main()