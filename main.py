import json
import requests
import time
import smtplib

f = input("Enter the Crypto Short Nam: \n")
price_target = int(input("Enter Price target: "))
loss_target = int(input("Enter Loss stop: "))

while True:
    url = "https://api.nomics.com/v1/currencies/ticker?key=1e0c0c160bc402daf0da9293ca1f7e1c2c6a3022&ids="+str(f).upper()
    response = requests.session()
    req = response.get(url).text
    load = json.loads(req)
    price = float(load[0]["price"])
    print(price)
    time.sleep(2)

    if price > price_target :
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("skylarcryptoalert@gmail.com", "mmwzcribduqqxnea")
        message = "its time to sell your coin"
        s.sendmail("skylarcryptoalert@gmail.com", "nothuman1701@gmail.com", message)
        print("MAIL SENT")
        s.quit()
    elif price < loss_target :
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        s.login("skylarcryptoalert@gmail.com", "mmwzcribduqqxnea")
        message = "its time to buy your coin"
        s.sendmail("skylarcryptoalert@gmail.com", "nothuman1701@gmail.com", message)
        print("MAIL SENT")
        s.quit()




































