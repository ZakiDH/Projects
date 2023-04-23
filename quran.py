import re
import requests
from bs4 import BeautifulSoup
url = "https://quran.com/1"
page = requests.get(url)
soup = BeautifulSoup(page.content, "html.parser")
div_tag = soup.find("div", class_="TranslationView_container__M0fhJ")
arabic_text = re.findall("[\u0600-\u06FF]+", div_tag.text)
arabic_text_no_numbers = re.sub("[\u0660-\u0669]+", "", "".join(arabic_text))
print(arabic_text_no_numbers)