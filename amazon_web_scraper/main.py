import requests
from bs4 import BeautifulSoup
import smtplib

TARGET_PRICE = 200
USER = "paulospoulos6@gmail.com"
PASSWORD = "xhgyknjsahpyjaqb"
url = "https://www.amazon.com/Apple-Keyboard-Numeric-Computers-Silicon/dp/B09BRDJBRT/ref=sr_1_50?c=ts&keywords=Computer%2BKeyboards&qid=1672051150&s=pc&sr=1-50&ts_id=12879431&th=1"
headers = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15",
           'Accept-Language': "el-GR,el;q=0.9",
           'Connection': "keep-alive"}

response = requests.get(url=url, headers=headers).text
soup = BeautifulSoup(response, "lxml")
product_name = soup.find(name="span", id="productTitle").getText().strip()
print(product_name)
product_price = float(soup.find(name="span", class_="a-offscreen").getText().strip("$"))

if product_price < TARGET_PRICE :
    print('Sends email..')
    with smtplib.SMTP('smtp.gmail.com', port=587) as connection:
        connection.starttls()
        response = connection.login(user=USER, password=PASSWORD)
        connection.sendmail(from_addr=USER,
                            to_addrs=USER,
                            msg=f"The {product_name} \nis {product_price} NOW!")
else:
    pass




