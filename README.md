## Guía de Instalación de PyTrends
La biblioteca PyTrends permite acceder y utilizar la API de Google Trends para obtener datos sobre las tendencias de búsqueda. Sigue estos pasos para instalar PyTrends en tu entorno de desarrollo.

### Paso 1: Instalación de Python
Si aún no tienes Python instalado en tu sistema, debes hacerlo antes de continuar. Puedes descargar la última versión de Python desde el sitio oficial: Descargar Python.

### Paso 2: Instalación de PyTrends
Abre una terminal o línea de comandos y sigue los siguientes pasos:

### 2.1 Instalación utilizando pip
Pip es el sistema de gestión de paquetes para Python. Ejecuta el siguiente comando para instalar PyTrends utilizando pip:
<pre>
pip install pytrends
</pre>

### 2.2 Verificación de la instalación
Para verificar que la instalación se realizó correctamente, puedes abrir un entorno de Python interactivo ejecutando el comando python en tu terminal y luego intentar importar PyTrends:

<pre>
import pytrends
</pre>
Si no se produce ningún error, la instalación se completó con éxito.


## API

La API de Google Trends a través de PyTrends proporciona una manera conveniente de acceder a datos sobre las tendencias de búsqueda en Google. Aquí está una descripción de las principales funciones y parámetros que puedes utilizar con la API.

### Configuración de la Conexión
<pre>
from pytrends.request import TrendReq

pytrends = TrendReq(
    hl='en-US',     # Idioma de búsqueda (por ejemplo, 'en-US' para inglés)
    tz=360,         # Desplazamiento horario (por ejemplo, '360' para US CST)
    timeout=(10, 25),  # Tiempo de espera (conexión, lectura)
    proxies=['https://34.203.233.13:80'],  # Lista de proxies HTTPS
    retries=2,      # Número de intentos en caso de error
    backoff_factor=0.1,  # Factor de espera entre intentos de reintentos
    requests_args={'verify': False}  # Parámetros adicionales para la biblioteca 'requests'
)
</pre>

### Funciones Principales

<pre>
build_payload()
</pre>

Esta función construye una consulta de tendencias de búsqueda con los términos especificados y otros parámetros.

<pre>
kw_list = ["Python programming", "Data science"]
pytrends.build_payload(kw_list, cat=0, timeframe='today 5-y', geo='', gprop='')
kw_list: Lista de términos de búsqueda.
cat: Categoría a la que pertenecen los términos de búsqueda.
timeframe: Rango de tiempo para la consulta (ejemplo: 'today 5-y').
geo: Geolocalización para la consulta (por defecto, búsqueda global).
gprop: Propiedad de búsqueda (por defecto, web).
interest_over_time()
</pre>

Esta función obtiene los datos de tendencias de búsqueda.

<pre>
trends_data = pytrends.interest_over_time()
</pre>

### Otros Métodos
Además de *interest_over_time()*, PyTrends ofrece otros métodos para acceder a diferentes tipos de datos de tendencias, como *interest_by_region()*, -*related_queries()*, *related_topics()*, etc.

### Interest Over Time
`pytrends.interest_over_time()` se utiliza para obtener datos sobre el interés a lo largo del tiempo para una o más palabras clave específicas. Esta función devuelve un objeto de tipo `pandas.DataFrame`, que es una estructura de datos de la librería `pandas` que se asemeja a una tabla de base de datos o una hoja de cálculo de Excel.

**Input**
<pre>
from pytrends.request import TrendReq
# Configura la conexión a Google Trends
pytrends  = TrendReq(hl='es-US', tz=360)
# Palabra clave para la que deseas obtener información
keyword  = ["minecraft"]
# Construye la consulta
pytrends.build_payload(kw_list=keyword)
# Obtiene los datos de volumen de búsqueda
search_data  =  pytrends.interest_over_time()
# Imprime los datos de volumen de búsqueda
print(search_data)
</pre>

**Output**
|  date|  Keyword 1|isPartial |
|--|--|--|
| 2018-08-12 | 36 | False|
| 2018-08-19 | 34| False|
| 2018-08-26| 34| False|


1.  **Fecha (Date)**: La columna "date" simplemente muestra las fechas en las que se observó el nivel de interés.
    
2.  **Índice de Interés (Interest Index)**: Los números en esta columna representan el nivel relativo de interés en una palabra clave o término de búsqueda en las fechas correspondientes. Sin conocer el contexto exacto de los datos, es posible que estos números sean valores normalizados que indican la popularidad relativa de la palabra clave en relación con un período de tiempo o ubicación específico. Por ejemplo, un valor de 45 podría significar que el interés en la palabra clave en esa fecha específica fue aproximadamente el 45% del nivel más alto de interés observado en el período.
    
3.  **Valor Booleano (Boolean Value)**: La columna booleana muestra valores "True" o "False". En tu ejemplo, la última fila tiene un valor "True". Esto podría indicar algún tipo de evento o situación especial relacionada con la palabra clave en esa fecha específica. Sin más contexto, no puedo determinar con certeza qué representa este valor booleano.
