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
timeframe: Rango de tiempo para la consulta (ejemplo: 'today 5-y', 'today 12-m').
geo: Geolocalización para la consulta (por defecto, búsqueda global).
gprop: Propiedad de búsqueda (por defecto, web).
interest_over_time()
</pre>

Esta función obtiene los datos de tendencias de búsqueda.


### Interest over the time
Esta función devuelve un DataFrame de Pandas que contiene datos de interés en función del tiempo para un término de búsqueda específico. Los datos de interés se proporcionan en forma de valores de búsqueda normalizados en el tiempo.

#### Valor de Retorno:

La función `interest_over_time` devuelve un DataFrame de Pandas que contiene los datos de interés a lo largo del tiempo para el término de búsqueda especificado. El DataFrame tendrá las siguientes columnas:

- `date`: La fecha del período de tiempo.
- `keyword`: El valor de interés relativo para el término de búsqueda en esa fecha.

**Input**
<pre>
from pytrends.request import TrendReq

# Configurar la API de Google Trends
pytrends = TrendReq(hl='es-US', tz=360)

# Palabra clave para la que deseas obtener información
keyword = ["Python"]

# Construir la consulta
pytrends.build_payload(kw_list=keyword)

# Obtener datos de interés a lo largo del tiempo
interest_over_time = pytrends.interest_over_time()

# Mostrar los datos de interés a lo largo del tiempo
print(interest_over_time)

</pre>

En este ejemplo, se obtienen los datos de interés a lo largo del tiempo para el término de búsqueda "minecraft" utilizando la función `pytrends.interest_over_time()`. Los datos se presentarán en forma de un gráfico de línea para visualizar las tendencias de búsqueda a lo largo del tiempo.

**Output**
|  date|  Interest Index|isPartial |
|--|--|--|
| 2018-08-12 | 36 | False|
| 2018-08-19 | 34| False|
| 2018-08-26| 34| False|


1.  **Fecha (Date)**: La columna "date" simplemente muestra las fechas en las que se observó el nivel de interés.
    
2.  **Índice de Interés (Interest Index)**: Los números en esta columna representan el nivel relativo de interés en una palabra clave o término de búsqueda en las fechas correspondientes. Sin conocer el contexto exacto de los datos, es posible que estos números sean valores normalizados que indican la popularidad relativa de la palabra clave en relación con un período de tiempo o ubicación específico. Por ejemplo, un valor de 45 podría significar que el interés en la palabra clave en esa fecha específica fue aproximadamente el 45% del nivel más alto de interés observado en el período.
    
3.  **Valor Booleano (Boolean Value)**: La columna booleana muestra valores "True" o "False". En tu ejemplo, la última fila tiene un valor "True". Esto podría indicar algún tipo de evento o situación especial relacionada con la palabra clave en esa fecha específica. Sin más contexto, no puedo determinar con certeza qué representa este valor booleano.
4.  

### Filtrar por países
Esta función devuelve un DataFrame de Pandas que contiene datos de interés en una ubicación geográfica específica en función de un término de búsqueda. Los datos de interés se proporcionan en forma de porcentajes relativos al período y la ubicación geográfica seleccionados.

#### Parámetros:

- `resolution`: Determina el nivel de resolución geográfica de los datos solicitados. Puede ser uno de los siguientes valores:
    - `'CITY'`: Datos a nivel de ciudad.
    - `'COUNTRY'`: Datos a nivel de país.
    - `'DMA'`: Datos a nivel de área metropolitana (DMA, por sus siglas en inglés).
    - `'REGION'`: Datos a nivel de región.
- `inc_low_vol`: Un valor booleano (`True` o `False`) que indica si se deben incluir datos de países o regiones con un bajo volumen de búsquedas en Google Trends.
- `inc_geo_code`: Un valor booleano (`True` o `False`) que indica si se deben incluir códigos ISO de países junto con los nombres en los datos.

#### Ejemplos de Paises disponibles
"US" - Estados Unidos
"GB" - Reino Unido
"DE" - Alemania
"FR" - Francia
"ES" - España
"IT" - Italia
"JP" - Japón
"BR" - Brasil
"IN" - India
"CN" - China

#### Valor de Retorno:

La función `interest_by_region` devuelve un DataFrame de Pandas que contiene los datos de interés en la ubicación geográfica especificada en función del término de búsqueda. El DataFrame tendrá las siguientes columnas:

- `geoName`: El nombre de la ubicación geográfica (ciudad, país, etc.).
- `value`: El valor de interés relativo en esa ubicación para el término de búsqueda.

**Input**
<pre>
from pytrends.request import TrendReq

# Configura la conexión a Google Trends
pytrends = TrendReq(hl='es-US', tz=360, geo='ES')  # Establece 'geo' como 'ES' para España

# Palabra clave para la que deseas obtener información
keyword = ["minecraft"]

# Construye la consulta
pytrends.build_payload(kw_list=keyword)

# Obtiene los datos de volumen de búsqueda para España
search_data = pytrends.interest_over_time()

# Imprime los datos de volumen de búsqueda para España
print(search_data)

</pre>
En este ejemplo, se obtienen los datos de interés por país para el término "Python programming" utilizando la función `interest_by_region`. Puedes ajustar los parámetros `resolution`, `inc_low_vol` e `inc_geo_code` según tus necesidades específicas.


### Suggestions
Esta función devuelve una lista de sugerencias de palabras clave relacionadas a partir de un término de búsqueda específico. Las sugerencias de palabras clave son términos que están relacionados con el término de búsqueda proporcionado y pueden ser útiles para expandir o refinar las consultas de búsqueda.

#### Parámetros:

- `keyword`: El término de búsqueda para el cual deseas obtener sugerencias de palabras clave.

#### Valor de Retorno:

La función `suggestions` devuelve una lista de diccionarios, donde cada diccionario representa una sugerencia de palabra clave relacionada. Cada diccionario contiene información sobre la sugerencia, incluyendo el título de la sugerencia.

**Input**
<pre>
from pytrends.request import TrendReq

# Configurar la API de Google Trends
pytrends = TrendReq(hl='es-US', tz=360)

# Término de búsqueda para el que deseas obtener sugerencias
keyword = "España"

# Obtener sugerencias de palabras clave relacionadas
suggestions = pytrends.suggestions(keyword)

# Mostrar las sugerencias obtenidas
for suggestion in suggestions:
    print(suggestion['title'])
</pre>

En este ejemplo, el atributo `suggestion['title']` se utiliza para acceder al título de cada sugerencia de palabra clave relacionada en el resultado y se imprime en la consola. Cada elemento en la lista de sugerencias devuelta por `pytrends.suggestions()` tiene un diccionario con varias claves, y `'title'` es una de ellas que contiene el título de la sugerencia de palabra clave.

**Output**
<pre>
España				#Title
Marks & Spencer		#Sugerencias
Lotería Nacional de España
Segunda División de España
Copa del Rey
</pre>
