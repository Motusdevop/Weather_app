import requests

from bs4 import BeautifulSoup
def get() -> dict:
    req = requests.get("https://ria.ru/world/")
    scr = req.text
    soup = BeautifulSoup(scr, 'lxml')

    title = soup.find(class_="list-item__content").find(class_="list-item__title color-font-hover-only").text
    time = soup.find(class_="list-item__info").find(class_="list-item__date").text
    link = soup.find(class_="list-item__content").find(class_="list-item__image").get("href")

    return {
        "title" : title,
        "time" : time,
        "link" : link
    }

if __name__ == "__main__":
    print(get())