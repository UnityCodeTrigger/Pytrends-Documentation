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
