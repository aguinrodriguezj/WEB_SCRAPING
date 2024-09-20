import scrapy
import os
from csv import DictWriter 

def append_header_as_row(file_name, field_names):
    """ 
    Abre un csv y agrega los nombres de las columnas (headers).
    Args:
    file_name: es el nombre del csv que abrimos,
    field_names: son los headers que añadimos como una lista.
    """
    
    # Compruebo si el archivo existe
    file_existe = os.path.isfile(file_name)
    
    # Si existe, se elimina
    if file_existe:
        os.remove(file_name)
        print(f'Archivo {file_name} eliminado.')       

    # Abre el archivo en modo 'append'
    with open(file_name, 'a+', newline='', encoding='utf-8') as write_obj:
        # Crea un objeto 'writer' desde el módulo csv
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        # Añade la cabecera al objeto
        dict_writer.writeheader()  
        
def append_dict_as_row(file_name, dict_of_elem, field_names):
    """ 
    Abre un csv y agrega una fila en forma de diccionario en el csv.
    Args:
    file_name: es el nombre del csv que abrimos,
    dict_of_elem: es un dictado con los elementos de la fila que se va a añadir al final del csv
    field_names: son los nombres de las columnas (headers)
    """
    # Abre el archivo en modo 'append'
    with open(file_name, 'a+', newline='', encoding='utf-8') as write_obj:
        # Crea un objeto 'writer' desde el módulo csv
        dict_writer = DictWriter(write_obj, fieldnames=field_names)
        #  Añade un diccionario de filas al csv
        dict_writer.writerow(dict_of_elem)


class poblacionmundial(scrapy.Spider):
    
    name = 'pob_mundial' # nombre del spider
    #custom_settings = {'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7'} # activarlo si da problemas
    start_urls= ["https://www.worldometers.info/world-population/population-by-country/"] # Lista de URL desde las que comienza el scraper
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3" # usamos un user-agent para que amazon no nos bloquee (sino obtendríamos un error 503). Se pueden añadir otros.
    }
    custom_settings = {
        #'REQUEST_FINGERPRINTER_IMPLEMENTATION': '2.7',
        #'FEED_URI': 'población_mundial_2024.csv', # nombre del archivo donde se guardan los datos
        #'FEED_FORMAT': 'csv', # formato del archivo
        'ROBOTSTXT_OBEY': True, # validamos el archivo robots.txt
        #'FEED_EXPORT_ENCODING': 'utf-8' # codificación usada en la exportación
    }

    
    def parse(self, response):
        """ 
        Es la función que hará el análisis y obtendrá los datos
        """
        
        # Extraer cabeceras de la tabla
        columnas = response.xpath('//table//thead//tr//th//text()').getall()
        columnas = [columnas[0]] + [columnas[1]] + [columnas[2]+columnas[3]] + [columnas[4]+columnas[5]] + [columnas[6]+columnas[7]] + [columnas[8]+columnas[9]] + [columnas[10]+columnas[11]] + [columnas[12]+columnas[13]] + [columnas[14]+columnas[15]] + [columnas[16]+columnas[17]] + [columnas[18]+columnas[19]] + [columnas[20]+columnas[21]]
               
        append_header_as_row(
            file_name = 'población_mundial_2024.csv',
            field_names = columnas
            )
        
        # Extraer las filas de la tabla
        table = response.xpath('//table//tbody//tr')
        
        for tb in table:
            row_data = tb.xpath('.//td//text()').getall()            
            row_data = [data.strip() for data in row_data] # limpia los espacios en blanco
            
            if len(row_data) == len(columnas):
                dictionary = dict(zip(columnas, row_data))
                append_dict_as_row(
                    file_name = 'población_mundial_2024.csv', 
                    dict_of_elem = dictionary, # diccionario de valores
                    field_names = columnas   # nombres de las columnas     
                )
