import requests
import lxml
from bs4 import BeautifulSoup


session = requests.Session()
header = {"User_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"}

for j in range(1, 7):
    url = f"https://cash-backer.club/shops?page={j}"

    response = session.get(url, headers=header)
    soup = BeautifulSoup(response.text, "lxml")

    all_product = soup.find("div", class_="row col-lg-9 col-md-9 col-12")

    products = all_product.find_all("div", class_="col-lg-2 col-md-3 shop-list-card pseudo-link no-link")

    for elem in products:
        price = elem.find("div", class_="shop-rate").text
        title = elem.find("div", class_="shop-title").text
        with open("cash-backer.txt", "a", encoding="utf-8") as file:
            file.write(f"{title} ---->>>>{price}\n")

        print(title)
        print(price)
        print(" ")