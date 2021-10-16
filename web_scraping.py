import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin


def odkazy(odkaz):
    """Fukce, ktera mi vraci list url adres z daneho odkazu"""
    r = requests.get(odkaz)  #Stahneme informace z webu
    html = r.text  #Prevedeme html na textovou podobu
    soup = BeautifulSoup(html, 'html.parser')  # Vytvorime html
    href_list = []  #Vytvorim novy list
    for i, a_elem in enumerate(soup.select(".Glist a.screenLink")):
        print(i, a_elem["href"])
        href = urljoin(
            odkaz,
            a_elem["href"])  #Spojime puvodni adresu s odkazem na dalsi stranku
        print(50 * "-")
        href_list.append(href)
    return href_list


print("Z tohohle muzes vybirat: ")
print(50 * "-")
list_mých_informací = []
url = "https://www.superhry.cz/skakacky/"
list_odkazu = odkazy(url)  #sem zadej adresu!
