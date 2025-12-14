import re
from bs4 import BeautifulSoup

def clean_text(text: str) -> str:
    return " ".join(text.split())

def extract_amount(text: str) -> int | None:
    match = re.search(r"(\d[\d\s]+)\s*руб", text.lower())
    if match:
        return int(match.group(1).replace(" ", ""))
    return None

def get_soup(html: str) -> BeautifulSoup:
    return BeautifulSoup(html, "html.parser")
