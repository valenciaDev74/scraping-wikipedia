import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from rich.console import Console
from rich.markdown import Markdown
from urllib.parse import urlparse
import json
import os

console = Console()


def is_wp_url(url: str) -> bool:
    parsed_url = urlparse(url)
    domain = parsed_url.netloc.lower()
    if domain == "wikipedia.org" or domain.endswith(".wikipedia.org"):
        return True
    return False


def resume(text: str) -> str | None:
    load_dotenv()
    API_KEY = os.getenv("API_KEY")
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-3-flash-preview:generateContent?key={API_KEY}"
    headers = {"Content-Type": "application/json"}
    promt = f"""
                Actúa como un analista de datos especializado en extracción de información y síntesis de textos. 

                Tu tarea es procesar el texto que se proporciona a continuación y extraer exclusivamente los
                puntos más relevantes organizados en las siguientes categorías:

                1. **Fechas específicas**: Días, meses o años exactos de eventos clave.
                2. **Sucesos importantes**: Hitos o acciones principales narradas en el texto.
                3. **Periodos relevantes**: Intervalos de tiempo o eras mencionadas.
                4. **Lugares clave**: Ubicaciones geográficas, ciudades o recintos específicos.
                5. **Personas clave**: Nombres de figuras individuales o grupos de personas determinantes.

                ### Instrucciones Adicionales:
                - Mantén las descripciones breves y directas.
                - Si una categoría no tiene información relevante en el texto, escribe "No mencionado".
                - Devuelve la información en formato [Markdown con viñetas].
                - No añadas información externa; cíñete estrictamente al contenido del texto.
                - Omite cualuier comentario tuyo. El principio y al final del texto no debe haber comentarios.

                ### Texto a analizar:
                [{text}]
                """
    data = {"contents": [{"parts": [{"text": promt}]}]}

    try:
        response = requests.post(url, headers=headers, data=json.dumps(data))
        response.raise_for_status()
        result = response.json()
        resumed_text = result["candidates"][0]["content"]["parts"][0]["text"]
        return resumed_text
    except requests.exceptions.RequestException as e:
        console.print(f"[red]Error to request: {e}[/red]")
        return None


def get_page(url: str) -> BeautifulSoup:
    headers = {
        "User-Agent": "ScrapingWikipedia/1.0 (https://github.com/valenciaDev74/scraping-wikipedia; https://github.com/valenciaDev74) requests-library"
    }
    response = requests.get(url, timeout=10, headers=headers)
    soup = BeautifulSoup(
        response.content,
        "html.parser",
    )
    return soup


def get_page_text(url: str) -> str:
    soup = get_page(url)
    # text = soup.find("div", {"id": "bodyContent"}).text # type: ignore
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
    if not is_wp_url(url):
        console.print("[red]The URL provided is not a Wikipedia link.[/red]")
        return
    text = resume(get_page_text(url))
    if text is None:
        return
    text = Markdown(text)
    console.print(text)


if __name__ == "__main__":
    main()
