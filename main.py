from datetime import datetime
import os
import pyautogui as py
from time import sleep
import json
import requests
from bs4 import BeautifulSoup
from langdetect import detect
from googletrans import Translator
import pyperclip

with open(
    f"{os.path.expanduser( '~' )}\\OneDrive\\Documentos\\python\\last_date.txt", "r"
) as f:
    last_date = f.read().strip()
if str(datetime.now().date()) != last_date:
    url = "https://www.techpowerup.com/"
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    translator = Translator()

    divs = soup.find_all("div", class_=["text", "datesep"])
    news_titles = [news.text for news in divs[1:]]
    listasno = []

    for title in news_titles:
        new_t = title.replace("\n", "").replace("\t", "").replace("\\", "")
        translated_text = translator.translate(new_t, dest="pt").text
        listasno.append(translated_text)

    with open(
        f"{os.path.expanduser( '~' )}\\OneDrive\\Documentos\\python\\bullshits.json",
        "w",
    ) as outfile:
        json.dump(listasno, outfile)

with open(
    f"{os.path.expanduser( '~' )}\\OneDrive\\Documentos\\python\\bullshits.json"
) as json_file:
    dicio = json.load(json_file)
pyperclip.copy(
    "Ultimas noticias do site techpowerup.com, utilizando um script de webscrapling em python:"
)
py.hotkey("ctrl", "v")
py.press("ENTER")
for Texto in dicio[::-1]:
    pyperclip.copy(Texto)
    py.hotkey("ctrl", "v")
    # sleep(.1)
    py.press("ENTER")
hoje = datetime.now().strftime("%d/%m/%Y-%H:%M")
pyperclip.copy(
    f"Essas foram as noticias no site da techpowerup (As ultimas mensagens são as noticias mais recentes) hoje, traduzidas, {hoje}"
)
py.hotkey("ctrl", "v")
py.press("ENTER")
with open(
    f"{os.path.expanduser( '~' )}\\OneDrive\\Documentos\\python\\last_date.txt", "w"
) as f:
    f.write(str(datetime.now().date()))
