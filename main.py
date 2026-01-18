import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
import json
import os


def resume(text: str) -> str | None:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {"parts": [{"text": f"Resume and list important points:\n{text}"}]}
        ]
    }

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        resumed_text = result["candidates"][0]["content"]["parts"][0]["text"]
        return resumed_text
    except requests.exceptions.RequestException as e:
        print(f"Error to request: {e}")


def get_page(url: str) -> BeautifulSoup:
    headers = {
        "User-Agent": "ScrapingWikipedia/1.0 (https://ejemplo.com/contacto; mi-email@ejemplo.com) requests-library"
    }
    response = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )
    return soup


def get_page_text(url: str) -> str:
    soup = get_page(url)
    text = soup.find("div", {"id": "bodyContent"}).text
    paragraphs = soup.find_all("p")
    full_text = "\n".join(
        [
            para.get_text(strip=True, separator=" ")
            for para in paragraphs
            if para.get_text(strip=True)
        ]
    )
    return full_text


def main():
    url = input("Enter a URL: ")
    text = get_page_text(url)
    resumed_text = resume(text)
    print(resumed_text)
    print("Hello from scraping-wikipedia!")


if __name__ == "__main__":
    main()
