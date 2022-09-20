from flask import Flask, render_template, request
from urllib.request import urlopen
import json
import time
import smtplib


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/data', methods=["GET","POST"])
def data():
    if request.method == "POST":
        f = request.form.get('name')
        mail = request.form.get('mail')
        price_target = float(request.form.get('profit'))
        loss_target = float(request.form.get('loss'))
        while(1):
            url = urlopen(f"https://api.nomics.com/v1/currencies/ticker?key=1e0c0c160bc402daf0da9293ca1f7e1c2c6a3022&ids={str(f).upper()}")
            req = url.read().decode('utf-8')
            load = json.loads(req)
            price = float(load[0]["price"])
            print(price)
            time.sleep(2)

            if price > price_target:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("skylarcryptoalert@gmail.com", "mmwzcribduqqxnea")
                message = (f"its time to sell your coin \ncurrent price is:{price}")
                s.sendmail("skylarcryptoalert@gmail.com", mail, message)
                s.quit()
                return("MAIL SENT")


            elif price < loss_target:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login("skylarcryptoalert@gmail.com", "mmwzcribduqqxnea")
                message = (f"its time to buy your coin\ncurrent price is:{price}")
                s.sendmail("skylarcryptoalert@gmail.com", mail, message)
                s.quit()
                return("MAIL SENT")



if __name__ == '__main__':
    app.run()







































