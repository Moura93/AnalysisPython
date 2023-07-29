import xarray as xr
import pandas as pd

# Extrair as variáveis de interesse
dataset = xr.open_dataset("Velocidades.nc")
u = dataset['u']
v = dataset['v']

# Extrair as coordenadas (latitude, longitude, datatime, nível)
latitudes = dataset.coords['latitude'].values
longitudes = dataset.coords['longitude'].values
datetimes = dataset.coords['time'].values
# levels = dataset.coords['level'].values

# Criar uma lista para armazenar os dados extraídos
dados_extraidos = []

# Iterar sobre as dimensões e extrair os valores correspondentes de u, v, latitudes, longitudes, datetimes e levels

for datetime in datetimes:
    for lat, lon in zip(latitudes, longitudes):
        u_value = u.sel(time=datetime, latitude=lat, longitude=lon).values.item()
        v_value = v.sel(time=datetime, latitude=lat, longitude=lon).values.item()

        dados_extraidos.append({
            'u': u_value,
            'v': v_value,
            'latitude': lat,
            'longitude': lon,
            'datetimes': datetime,
        })

# Criar um DataFrame com os dados extraídos
df = pd.DataFrame(dados_extraidos)

# Converter a coluna 'datetimes' para um objeto datetime
df['datetimes'] = pd.to_datetime(df['datetimes'])

df.to_excel('era5.xlsx')



