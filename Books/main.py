import requests
from bs4 import BeautifulSoup
import smtplib
from url import URL

EMAIL = "dafadarts@gmail.com"
PASSWORD = "a7U6+cbOc3+h7a"
OUR_PRICE = 600.0

URl = URL()
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.141 "
                  "Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URl.url_2, headers=header)

soup = BeautifulSoup(response.content, "lxml")
# print(soup.prettify())

price = soup.find(class_="a-size-base a-color-price a-color-price").get_text()
price_without_currency = price.split("₹")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < OUR_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Amazon Price Aleart!\n\nHey Einstein's biography is now costing ₹{price_as_float} Your's set price was "
                                f"₹{OUR_PRICE}\n "
                                f"\n\n\nHere's the link {URl.url_2}.")
