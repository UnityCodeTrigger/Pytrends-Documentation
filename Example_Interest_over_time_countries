#Lo mismo pero filtrado por paises

from pytrends.request import TrendReq

# Configura la conexión a Google Trends
pytrends = TrendReq(hl='es-US', tz=360, geo='ES')  # Establece 'geo' como 'ES' para España. Prueba a poner 'FR' de Francia 

# Palabra clave para la que deseas obtener información
keyword = ["minecraft","Fortnite"]

# Construye la consulta
pytrends.build_payload(kw_list=keyword)

# Obtiene los datos de volumen de búsqueda para España
search_data = pytrends.interest_over_time()

# Imprime los datos de volumen de búsqueda para España
print(search_data)
