# Scraping Wikipedia

## Descripción

Este programa es una herramienta de scraping web que extrae el texto principal de un articulo de Wikipedia, y utiliza la API de Google Gemini para generar un resumen estructurado. El resumen se organiza en categorías clave como fechas específicas, sucesos importantes, periodos relevantes, lugares clave y personas clave.

## Características

- Extracción de texto de un articulo de Wikipedia utilizando BeautifulSoup.
- Resumen inteligente con IA generativa (Google Gemini).
- Salida formateada en Markdown utilizando Rich para la consola.

## Requisitos

- Python 3.12 o superior.
- Una clave API de Google Generative AI (Gemini).

## Instalación

1. Clona este repositorio:
   ```
   git clone https://github.com/valenciaDev74/scraping-wikipedia.git
   cd scraping-wikipedia
   ```

2. Instala las dependencias:
   ```
   pip install requests beautifulsoup4 python-dotenv rich
   ```

3. Crea un archivo `.env` en la raíz del proyecto y agrega tu clave API:
   ```
   API_KEY=tu_clave_api_aqui
   ```

## Uso

Ejecuta el programa principal:

```
python main.py
```

Ingresa la URL de la página web que deseas analizar cuando se te solicite. El programa extraerá el texto, lo procesará con la IA y mostrará el resumen en la consola.

## Estructura del Proyecto

- `main.py`: Archivo principal con la lógica del programa.
- `pyproject.toml`: Configuración del proyecto.
- `README.md`: Este archivo.

## Notas

- Asegúrate de tener una conexión a internet para acceder a las páginas web y la API.
- El programa respeta los encabezados de User-Agent para scraping ético.
- No se recomienda usar este programa para scraping masivo sin permiso.

## Licencia

Este proyecto está bajo la Licencia MIT. Ver el archivo [LICENSE](LICENSE) para más detalles.