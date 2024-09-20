Bing es un motor de búsqueda desarrollado por Microsoft que, o bien mediante una búsqueda estándar o bien aplicando una serie de filtros, podemos encontrar imágenes, videos, compras, noticias, mapas y otras categorìas.

En este proyecto, me centraré sobre cómo se pueden obtener imágenes de Bing de diferentes tipos aplicando una serie de filtros, usando por un lado una combinación de **Requests y BeautifulSoup** y por otro lado una combinación de **BeautifulSoup y Selenium**.

El notebook [**buscador_imagenes_bing.ipynb**](./buscador_imagenes_bing.ipynb) realizará las siguientes tareas:

1. Utilizando una combinación de Request y BeautifulSoup.

- Generará la URL a la que tiene que acceder
- Buscará las imágenes requeridas.
- Descargará las imágenes y las guardará en una carpeta.
- Con las imágenes que ha descargado, creará un mosaico de imágenes aleatorias.

2. Utilizando una combinación de BeautifulSoup y Selenium.

- Abrir el navegador Chrome.
- Generará la URL a la que tiene que acceder.
- Buscará las imágenes requeridas.
- Descargará las imágenes y las guardará en una carpeta.
- Con las imágenes que ha descargado, creará un mosaico de imágenes aleatorias.
- Cerrar el navegador.
