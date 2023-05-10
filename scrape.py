from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from dbAsinSaving import insert
import time


def cleanPriceInformations(priceInformations_raw):
    oldPrice_raw = (priceInformations_raw[0].text).split()
    for part in oldPrice_raw:
        if '€' in part: oldPrice = part

    discount_raw = (priceInformations_raw[1].text).split()
    for part in discount_raw:
        if '%' in part: discount = part

    return oldPrice, discount

def cleanLinkProduct(linkProduct_raw):
    index = linkProduct_raw.find('?')
    asin = linkProduct_raw[index-10:index]
    return asin

def scrapeDeals(driver):
    driver.get("https://it.camelcamelcamel.com/top_drops")

    # Get Cookies
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="qc-cmp2-ui"]/div[2]/div/button[2]'))).click()

    # Get categories
    categoriesSection = driver.find_element(By.ID, "bn")
    categoriesList_seleniumElements = categoriesSection.find_elements(By.CSS_SELECTOR, "option[id^='it_']")
    categoriesList = []
    for category_seleniumElement in categoriesList_seleniumElements:
        categoriesList.append(category_seleniumElement.text)
        
    # Get urls where there are our products
    urlList = []
    for category in categoriesList:
        url = "https://it.camelcamelcamel.com/{}?t=relative&s=relative&i=1&bn={}&d={}".format("top_drops", (category.replace(" ", "-")).lower(), "20")
        urlList.append(url)

    # Get our products informations from each category url
    productList = []
    asinList = []
    for url in urlList:
        print(url)
        driver.get(url)
        try:
            productTable = driver.find_element(By.CSS_SELECTOR, "div[id^='ptable_']")
            productCardsList = productTable.find_elements(By.CLASS_NAME, "card")
            time.sleep(10)
            for product in productCardsList:
                    try:
                        # Retrieve product title
                        title = product.find_element(By.CSS_SELECTOR, "h6[class='popular_ptitle']>a").text
                        #print(title)

                        # Retrieve product asin
                        link_raw = product.find_element(By.CSS_SELECTOR, "h6[class='popular_ptitle']>a").get_attribute("href")
                        asin = cleanLinkProduct(link_raw)
                        asinList.append(asin)
                        #print(asin)

                        # Retrieve product strikePrice
                        strikePrice = product.find_element(By.CSS_SELECTOR, ".current_price.text-center").text
                        #print(strikePrice)

                        # Retrieve product old price and discount
                        priceInformations_raw = product.find_elements(By.CSS_SELECTOR, ".compare_price.text-center")
                        oldPrice, discount = cleanPriceInformations(priceInformations_raw)
                        #print(oldPrice, discount)

                        # Retrieve product image url
                        image = product.find_element(By.CSS_SELECTOR, "img[id^='img_']").get_attribute("src")
                        #print(image)

                        productList.append({"title": title, "asin": asin, "strikePrice": strikePrice, "oldPrice": oldPrice, "discount": discount, "image": image})

                    except NoSuchElementException: print("No product informations")
        except NoSuchElementException: print("No products found")
    insert(asinList)
    driver.close()

    return productList