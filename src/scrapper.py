import os
from bs4 import BeautifulSoup
import requests

from model.errors import ScrappingErrors


class Scrapper:

    def __init__(self, stock_code, price):
        pass

    @staticmethod
    def scrap(link):
        """This function takes a link and scraps that link and extract information base on tags.
        :param link: str Link of the website
        :return price: float Return current price of stock
        """
        try:
            response = requests.get(link)
        except requests.exceptions.RequestException as e:
            print("Unable to reach servers...")
            return 0
        else:
            try:
                content = response.content
                soup = BeautifulSoup(content, "html.parser")
                element = soup.find("span", {"id": "Nse_Prc_tick"}).strong.get_text()
                string_price = element.strip()
                price = float(string_price)
                return price
            except ScrappingErrors as e:
                print("Unable to extract information from the DOM...")
                return 0
            finally:
                response.close()





