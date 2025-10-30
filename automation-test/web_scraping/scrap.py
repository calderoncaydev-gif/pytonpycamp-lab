import requests
from bs4 import BeautifulSoup

def obtener_datos_falabella(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Aquí debes inspeccionar la estructura HTML de la página de búsqueda de Falabella
    # y ajustar las selecciones CSS según sea necesario.
    
    # Ejemplo: extraer nombres de productos
    nombres_productos = [nombre.text.strip() for nombre in soup.select('.product-title')]

    # Ejemplo: extraer precios de productos
    precios_productos = [precio.text.strip() for precio in soup.select('.cmr-price-value')]

    # Imprimir resultados
    for nombre, precio in zip(nombres_productos, precios_productos):
        print(f"Producto: {nombre}, Precio: {precio}")

# Reemplaza la URL con la URL específica de búsqueda en Falabella
url_falabella = "https://www.falabella.com/falabella-cl/search?Ntt=MZYJBL-auriculares+de+conducci%C3%B3n+de+aire+I68"
obtener_datos_falabella(url_falabella)
