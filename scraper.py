import requests
from bs4 import BeautifulSoup
import smtplib

URL = 'https://www.amazon.de/Sony-Digitalkamera-Touch-Display-Vollformatsensor-Kartenslots/dp/B07B4L1PQ8/ref=sr_1_3?keywords=sony+a7&qid=1561393494&s=gateway&sr=8-3'

headers = {
    "User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:70.0) Gecko/20100101 Firefox/70.0"}


def check_price():


page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()
converted_price = float(price[0:5])

if(converted_price < 1.700)
send_mail()

print(converted_price)
print(title.strip())


def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    # ! Cambiar mail y contra por uno real antes de compilar el programa
    server.login('unemail@gmail.com' 'contraseñaenctriptada')

    Subject = 'The Price Fell Down!'
