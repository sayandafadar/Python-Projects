import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

EMAIL = "dafadarts@gmail.com"
PASSWORD = "a7U6+cbOc3+h7a"
OUR_PRICE = 100.0

URl = "https://www.amazon.com/Instant-Pot-Multi-Use-Programmable-Pressure/dp/B00FLYWNYQ/ref=pd_sbs_1?pd_rd_w=jzwdN" \
      "&pf_rd_p=c52600a3-624a-4791-b4c4-3b112e19fbbc&pf_rd_r=S99EC8X62PWJ8ABTAE1C&pd_rd_r=3cc5b03a-637f-407a-b0f0" \
      "-1184e99a53b8&pd_rd_wg=tHejk&pd_rd_i=B00FLYWNYQ&psc=1 "

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/87.0.4280.141 "
                  "Safari/537.36 ",
    "Accept-Language": "en-US,en;q=0.9"
}

response = requests.get(URl, headers=header)

soup = BeautifulSoup(response.content, "lxml")
#print(soup.prettify())

price = soup.find(id="price_inside_buybox").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)

if price_as_float < OUR_PRICE:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs=EMAIL,
                            msg=f"Subject:Amazon Price Aleart!\n\nHey Instant Pot Duo 7-in-1 Electric Pressure Cooker, Sterilizer, "
                                f"Slow Cooker, Rice Cooker, Steamer, Saute, Yogurt Maker, and Warmer, 6 Quart, "
                                f"14 One-Touch Programs is now costing ${price_as_float} Your's set price was "
                                f"${OUR_PRICE}\n "
                                f"\n\n\nHere's the link {URl}.")
