En este proyecto veremos cómo se pueden obtener datos de una tabla de precios históricos de los índices IBEX, haciendo uso de Selenium. Para ello deberemos introducir en un **formulario** tres campos:

- _Desde_: Fecha de comienzo del histórico. Como mínimo podemos introducir la fecha correspondiente a un año anterior a la fecha actual.
- _Hasta_: Fecha de finalización del histórico. Como máximo podemos introducir el día anterior a la fecha actual.
- _Indice_: Es una lista desplegable de índices. Debemos seleccionar uno.

Finalmente, pulsaremos sobre _BUSCAR_ para enviar el formulario y que nos devuelva la tabla de resultados que queremos obtener.

El notebook [**ibex35_historico_selenium.ipynb**](./ibex35_historico_selenium.ipynb) realizará las siguientes tareas:

- Abrir el navegador Chrome.
- Cubrir el formulario para obtener la tabla de datos requeridos.
- Extracción de los datos de la tabla.
- Cargar los datos en un DataFrame.
- Almacenamiento de los datos extraidos en un archivo CSV.
- Cerrar el navegador.
