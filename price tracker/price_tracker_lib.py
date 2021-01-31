from selenium import webdriver
from datetime import datetime, date


#gets price from ebay site
def get_price(driver,link, title):
    if "eBay" in title:
        driver.get(link)
        Price = driver.find_element_by_id("prcIsum").text
        driver.get("https://www.google.com/search?q=usd+to+in")
        conv_const = float(driver.find_element_by_xpath("//span[@class = 'DFlfde SwHCTb']").text)
        driver.quit()
        temp = ""
        for i in Price:
            if i.isdigit() or i == "." :
                temp = temp + i
        price = float(temp)
        price = price*conv_const
        driver.quit()
        return price
    elif "Amazon.in" in title:
        driver.get(link)
        try:
            Price = driver.find_element_by_id("priceblock_dealprice").text
        except:
            try:
                Price = driver.find_element_by_id("priceblock_ourprice").text
            except:
                Price = driver.find_element_by_xpath("//span[@class = 'priceBlockStrikePriceString a-text-strike']").text
        driver.quit()
        temp = ""
        for i in Price:
            if i.isdigit() or i == ".":
                temp = temp+i
        price = float(temp)
        driver.quit()
        return price
    elif "Flipkart.com" in title:
        try:
            Price = driver.find_element_by_xpath("//div[@class = '_30jeq3 _16Jk6d']").text
        except:
            Price = driver.find_element_by_xpath("//div[@class = '_3I9_wc _2p6lqe']").text
        driver.quit()
        temp = ""
        for i in Price:
            if i.isdigit() or i == "." :
                temp = temp+i
        price = float(temp)
        driver.quit()
        return price  
        