import time
from driver import seleniumDriver
from scrape import scrapeDeals
from imageModify import imageStyle
from tgMessage import telegramMessage

if __name__ == "__main__":
    driverx = seleniumDriver()
    productList = scrapeDeals(driverx)
    for product in productList:
        imageStyle(product["image"], product["strikePrice"], product["oldPrice"], product["discount"])
        telegramMessage(product)
        time.sleep(1)
