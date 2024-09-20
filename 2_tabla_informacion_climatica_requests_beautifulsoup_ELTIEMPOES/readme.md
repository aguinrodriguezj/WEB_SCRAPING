En este proyecto veremos cómo se pueden extraer datos de una página web que contiene información climática en diversas estaciones meteorológicas en toda España, haciendo uso de **requests** y **BeautifulSoup**.

En concreto, la página web es de "eltiempo.es" y me centraré en la localidad de A Coruña, obteniendo una tabla de valores climáticos para los próximos 9 días.

El notebook [**clima_beautifulsoup.ipynb**](./clima_beautifulsoup.ipynb) realizará las siguientes tareas:

- Solicitud GET a la URL y obtención de los datos HTML.
- Extracción de los datos requeridos.
- Almacenamiento los datos extraidos en un archivo CSV.
- Cargar los datos del CSV en un DataFrame.
