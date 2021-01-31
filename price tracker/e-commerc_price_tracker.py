
from selenium import webdriver
import smtplib
from email.message import EmailMessage
import csv
from datetime import datetime, date
import time
import sys

PATH = ""

#gets price from amazon site
def get_price_amazon(driver):
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

#gets price from ebay site
def get_price_ebay(driver):
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

#gets price from flipkart site
def get_price_flipkart(driver):
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

#sends mails, enter the credentials of the sender email in this function in given space else it won't work
def sending_mail(receiver_email,price):
    sender_email = "<----Enter your email address---->"
    password = "<----enter your password---->"
    m = EmailMessage()
    m.set_content("The product you wanted to buy is now available at ₹" + str(int(price)))
    m["Subject"] = "Hi there"
    m["From"] = sender_email
    m["To"] = receiver_email
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login(sender_email, password)
    server.send_message(m)
    server.quit()


def main(receiver_email,link,desired_price):
    link = input("Enter the link: ")
    desired_price = float(input("Enter desired price: "))
    receiver_email = input("enter your email address: ")
    file_name = receiver_email + ".text"
    time_delay= 5*3600 #5 hr time delay

    try:
        f = open(file_name,"r")
        ltc = datetime.strptime(f.read(), "%d/%m/%Y %H:%M:%S")
        diff =  (datetime.now() - ltc).total_seconds()
        if diff <= time_delay:
            seconds = time_delay - diff
            time.sleep(seconds)
        f.close()
    except:
        f = open(file_name, "w")
        f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        f.close()
    
    driver = webdriver.Chrome(PATH)
    driver.minimize_window()
    driver.get(link)

    title = driver.title
    if "Amazon.in" in title:
        c = 0
    elif "Flipkart.com" in title:
        c = 1
    elif "eBay" in title:
        c = 2


    while True:
        try:
            if c == 0 :
                price = get_price_amazon(driver)
            elif c == 1:
                price = get_price_flipkart(driver)
            else: 
                price = get_price_ebay(driver)
        except:
            print("invalid Link")
            sys.exit()
        if price <= desired_price:            
            sending_mail(receiver_email, price)
            sys.exit()
        
        time.sleep(time_delay)

        f = open(file_name,"w")
        f.write(datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
        f.close()

        driver = webdriver.Chrome(PATH)
        driver.minimize_window()
        driver.get(link)



