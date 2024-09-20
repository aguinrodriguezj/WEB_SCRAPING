En este proyecto, veremos cómo se pueden obtener las poblaciones actuales de los diferentes países o territorios dependientes del mundo. Además de la población, también obtendremos datos como:

- Porcentaje de cambio anual.
- Cambio Neto.
- Densidad de población.
- Superficie terrestre.
- Número de migrantes (neto).
- Tasa de fertilidad.
- Edad media.
- Porcentaje de población urbana.
- Porcentaje de población que representan en el mundo.

Estos datos han sido elaborados por las Naciones Unidas (Departamento de Asuntos Económicos y sociales, División de Población) y publicados por [Worldometers](https://www.worldometers.info/).

**Pasos que se han seguido**

1. Instalar, Crear y Activar entorno virtual conda.
2. Instalamos las dependencias necesarias para el proyecto.
3. Instalamos Scrapy.
4. Creamos la carpeta que contendrá nuestro proyecto.
5. Inspeccionamos la web para obtener los XPath que necesitamos.
6. Definimos los XPath.
7. Creamos el spider para analizar y extraer la información de la web que necesitamos. Estos datos los almacenará en un archivo CSV. Ejecutamos el spider
8. Cargamos los datos almacenados en el csv en un DataFrame.
