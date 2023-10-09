import time

import selenium
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys

import requests
from bs4 import BeautifulSoup

#Set options according to the browser you use
# Get all info from the link below
#https://www.selenium.dev/documentation/en/getting_started_with_webdriver/browsers/
options = webdriver.ChromeOptions()
# options.add_argument('--headless')

#uncomment the below code if you don't want a browser window to open
# options.add_argument('--headless') 

flag = 0
cchc = ''

#will contain the peices of all websites and show the best price accordingly
final_price_list = []
final_list = []
#Flipkart
def flipkart(itemName):
    print("Let's start scraping flipkart......")
    itemName = itemName
    baseurl='https://www.flipkart.com'
    flipurl = f'https://www.flipkart.com/search?q={itemName}&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off'
    headers = {
    'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }

        #scrape the main pro_list page of item
    req = requests.get(flipurl,headers=headers)
    soup = BeautifulSoup(req.content,'html.parser')

    try:
        
        
        #     print(content)
        pro_name= soup.find('div', {"class": '_4rR01T'})
        pro_price = soup.find('div', {"class": "_30jeq3 _1_WHN1"})
        image = soup.find_all('img',class_="_396cs4 _2amPTt _3qGmMb")

        for img in image:
            pro_image = img.get('src')

            #main list
        # pro_list = soup.find_all('div',class_='_2kHMtA')

        #     #will contain links of all product in the list
        # proLink = []

        # for i in pro_list:
        #     for link in i.find_all('a',href=True):
        #         proLink.append(baseurl + link['href'])

        # print(len(proLink))
        #     #scrape data from particular item
        # itemLink = proLink[0]

        # req = requests.get(itemLink,headers=headers)
        # soup = BeautifulSoup(req.content,'html.parser')
        # image = soup.find_all('img',class_="_396cs4 _2amPTt _3qGmMb")
        # rating = soup.find('div', class_="_3LWZlK")

        # for name in soup.find_all('span',class_="B_NuCI"):
        #     pro_name = name.text.strip()
        # for price in soup.find_all('div',class_="_30jeq3 _16Jk6d"):
        #     pro_price = price.text.strip()
        # for img in image:
        #     pro_image = img.get('src')

        #     #append the price scraped in float form
        # temp_pro_price = pro_price.replace("₹","")
        # final_pro_price = float(temp_pro_price.replace(",",""))
        # final_price_list.append(final_pro_price)


        result  = {
            'website': 'Flipkart',
            'itemLink': flipurl,
            'itemName': pro_name,
            'itemPrice': pro_price,
            'itemImage': pro_image[0]
        }  

        final_list.append(result)

        print("\n")    
        #print(itemLink)
        print(pro_name)
        print(pro_price)
        print(pro_image)
        # print(final_list)
        print("\n\n\nNow Let's scrape Amazon.....\n")
        ################

    except:
            #main list
        # pro_list = soup.find_all('div',class_='_1xHGtK _373qXS')

        #     #will contain links of all product in the list
        # proLink = []

        # for i in pro_list:
        #     for link in i.find_all('a',href=True):
        #         proLink.append(flipurl + link['href'])


        #     #scrape data from particular item
        # itemLink = proLink[0]

        # req = requests.get(itemLink,headers=headers)
        # soup = BeautifulSoup(req.content,'html.parser')
        # image = soup.find_all('div',class_="CXW8mj _3nMexc")
            
        # for name in soup.find_all('span',class_="G6XhRU"):
        #     pro_name = name.text.strip()
        # for price in soup.find_all('div',class_="_30jeq3 _16Jk6d"):
        #     pro_price = price.text.strip()
        # #     for img in image:
        # #         pro_image = img.get('src')

        # print("\n")    
        # print(itemLink)
        # print(pro_name)
        # print(pro_price)
        #     print(pro_image)
        print('\nProduct Not Found')
        print("\n\n\nNow Let's scrape Amazon.....\n")

def amazon(itemName):

    itemName = itemName
    amazon_url = f'https://www.amazon.in/s?k={itemName}&ref=nb_sb_noss'
    # print(amazon_url)
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }


    req = requests.get(amazon_url,headers=headers)
    soup = BeautifulSoup(req.content,'html.parser')
    # print(soup)


    pro_list = soup.find_all('div',{'data-component-type':'s-search-result'})
    try:
        # print(pro_list)
        prod = pro_list[0]

        imageTag = prod.find('div',class_='a-section aok-relative s-image-fixed-height')
        prodImage = imageTag.find('img')
        prodImageLink = prodImage['src']
        print("Image Link:",prodImageLink)

        atag = prod.h2.a
        prodName = atag.text

        name = soup.find('span', class_="a-size-medium a-color-base a-text-normal").text
        amazonPrice = soup.find('span',class_="a-price-whole").text
            

        result  = {
            'website': 'Amazon',
            'itemLink': amazon_url,
            'itemName': name,
            'itemPrice': amazonPrice,
            'itemImage': prodImageLink
        } 

        final_list.append(result)
#         temp_pro_price = amazonPrice.replace("₹","")
#         final_pro_price = float(temp_pro_price.replace(",",""))
#         final_price_list.append(final_pro_price)

        print("\nName:",name)
        print("Product Link: ",amazon_url)
        print("Price:",amazonPrice)
        # print(result)
        time.sleep(2)
    except:
        print("Product not found!")
        print("\n\n\nNow Let's scrape Croma.........\n")

def croma(itemName):
    itemName = itemName.replace("+", "%20")
    croma_base_url = 'https://www.croma.com'
    croma_url = f'https://www.croma.com/searchB?q={itemName}%3Arelevance&text={itemName}'
    driver = webdriver.Chrome(options=options)
    headers = {
        'User-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0'
    }

    driver.get(croma_url)

    soup=BeautifulSoup(driver.page_source,'html.parser')

    #list of all the products on the newUrl
    pro_list = []
    pro = soup.findAll('div',class_='content-wrap')
    for j in pro:
        for i in j.findAll('ul',class_='product-list'):
    #         print(i)
            for k in i.findAll('li',class_='product-item'):
                pro_list.append(k)

    try:
        prod = pro_list[0]

        imageTag = prod.find('div',class_='product-img')
        prodImage = imageTag.find('img')
        prodImageLink = prodImage['src']
        print("Image Link:",prodImageLink)

        atag = prod.h3.a
        prodLink = croma_base_url + atag['href']
        print("\nProduct Link:",prodLink)
        name = prod.h3.text
        print("Name:",name)

        cromaPrice = prod.find('span',class_='amount').text
        

        result  = {
            'website': 'Croma',
            'itemLink': prodLink,
            'itemName': name,
            'itemPrice': cromaPrice,
            'itemImage': prodImageLink
        } 

        final_list.append(result)
        #append the price scraped in float form
        temp_pro_price = cromaPrice.replace("₹","")
        final_pro_price = float(temp_pro_price.replace(",",""))
        final_price_list.append(final_pro_price)
        
        print("\nPrice:",cromaPrice)
        print(result)
        print("\n\n\nNow Let's scrape Ajio.........\n")

    except:
        print("Product not found!")

def inputData(itemName):
    final_list.clear()
    # proItem = input("Enter product name:\n")
    itemName = itemName.replace(" ","+")
    
    # print("\n\nWebsites you can compare your product from\n[1] Flipkart\n[2] Amazon\n[3] Croma\n[4] Ajio \n\n More websites coming soon! \n\n")
    # cchc == input("Start Comparing? [Y/N]:\n")
        
    # if cchc == 'Y' or 'y':
    # print("\n\n\nCool let's start then!")
    flipkart(itemName)
    amazon(itemName)
    croma(itemName)
    print(final_list)
    return final_list