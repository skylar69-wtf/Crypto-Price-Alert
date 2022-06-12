import json
import requests
import time
import smtplib
# enter crypto symbol:- example: bitcoin = btc
f = input("Enter the Crypto Short Nam: \n")
# Enter your price you want to get alerted
price_target = int(input("Enter Price target: "))
#Enter your price you want to get alerted for loss
loss_target = int(input("Enter Loss stop: "))

while True:
    #paste your api key with out qoatations
    url = "https://api.nomics.com/v1/currencies/ticker?key="paste your key here"="+str(f).upper()
    response = requests.session()
    req = response.get(url).text
    load = json.loads(req)
    price = float(load[0]["price"])
    print(price)
    time.sleep(2)

    if price > price_target :
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        #enter your login details
        s.login("sendermail", "senderpass")
        message = "its time to sell your coin"
        # enter sendermail and recivermail
        s.sendmail("sendermail", "recivermail", message)
        print("MAIL SENT")
        s.quit()
    elif price < loss_target :
        s = smtplib.SMTP('smtp.gmail.com', 587)
        s.starttls()
        #enter your login details
        s.login("sendermail", "senderpass")
        #edit messege as per your choice
        message = "its time to buy your coin"
        s.sendmail("sendermail", "recivermail", message)
        print("MAIL SENT")
        s.quit()




































