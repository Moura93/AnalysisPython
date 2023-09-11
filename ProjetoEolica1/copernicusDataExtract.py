# Extração de dados da báse ERA5 do copernicus
# LINK: https://cds.climate.copernicus.eu/cdsapp

#!/dataset/reanalysis-era5-complete?tab=overview

import cdsapi
import xarray as xr

c = cdsapi.Client()
c.retrieve('reanalysis-era5-complete', {           # Requests follow MARS syntax
                                                   # Keywords 'expver' and 'class' can be dropped. They are obsolete
       'class'   : 'od',                           # since their values are imposed by 'reanalysis-era5-complete'
       'date'    : '2005-01-01/to/2009-01-31',     # The hyphens can be omitted
       'levelist': '128/129/130/131/132/133/134/135/136/137',# 1 is top level, 137 the lowest model level in ERA5. Use '/' to separate values.
       'expver'  : '1',
       'levtype' : 'ml',
       'param'   : '131/132',                      # Full information at https://apps.ecmwf.int/codes/grib/param-db/
                                                   # The native representation for temperature is spherical harmonics
       'stream'  : 'oper',                         # Denotes ERA5. Ensemble members are selected by 'enda'
       'time'    : '00/to/23/by/1',                # You can drop :00:00 and use MARS short-hand notation, instead of '00/06/12/18'
       'type'    : 'an',
       'area'    : '-3.30/-39.15/-3.55/-38.9',   # North, West, South, East. Default: global
       'grid'    : '0.25/0.25',                    # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
       'format'  : 'netcdf',                       # Output needs to be regular lat-lon, so only works in combination with 'grid'!
   }, 'Velocidades_2005-2009.nc')                            # Output file. Adapt as you wish.

# c.retrieve(
#     'reanalysis-era5-pressure-levels',
#     {
#         'product_type': 'reanalysis',
#         'format': 'netcdf',
#         'variable': [
#             'u_component_of_wind', 'v_component_of_wind',
#         ],
#         'pressure_level': '600',
#         'year': '2005',
#         'month': [
#             '01', '02', '03',
#             '04', '05', '06',
#             '07', '08', '09',
#             '10', '11', '12',
#         ],
#         'day': [
#             '01', '02', '03',
#             '04', '05', '06',
#             '07', '08', '09',
#             '10', '11', '12',
#             '13', '14', '15',
#             '16', '17', '18',
#             '19', '20', '21',
#             '22', '23', '24',
#             '25', '26', '27',
#             '28', '29', '30',
#             '31',
#         ],
#         'time': [
#             '00:00', '01:00', '02:00',
#             '03:00', '04:00', '05:00',
#             '06:00', '07:00', '08:00',
#             '09:00', '10:00', '11:00',
#             '12:00', '13:00', '14:00',
#             '15:00', '16:00', '17:00',
#             '18:00', '19:00', '20:00',
#             '21:00', '22:00', '23:00',
#         ],
#         'area': [
#             -3.4, -39.1, -3.5,
#             -39,
#         ],
#     },
#     'Velocidades.nc')

dataset = xr.open_dataset("Velocidades_2005-2009.nc")

print(dataset)