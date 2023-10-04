# Extração de dados da báse ERA5 do copernicus
# LINK: https://cds.climate.copernicus.eu/cdsapp

#!/dataset/reanalysis-era5-complete?tab=overview

import cdsapi
import xarray as xr

c = cdsapi.Client()
c.retrieve('reanalysis-era5-complete', {           # Requests follow MARS syntax
                                                   # Keywords 'expver' and 'class' can be dropped. They are obsolete
       'class'   : 'od',                           # since their values are imposed by 'reanalysis-era5-complete'
       'date'    : '2000-01-01/to/2004-07-31',     # The hyphens can be omitted
       'levelist': '128/129/130/131/132/133/134/135/136/137',# 1 is top level, 137 the lowest model level in ERA5. Use '/' to separate values.
       'expver'  : '1',
       'levtype' : 'ml',
       'param'   : '131/132',                      # Full information at https://apps.ecmwf.int/codes/grib/param-db/
                                                   # The native representation for temperature is spherical harmonics
       'stream'  : 'oper',                         # Denotes ERA5. Ensemble members are selected by 'enda'
       'time'    : '00/to/23/by/1',                # You can drop :00:00 and use MARS short-hand notation, instead of '00/06/12/18'
       'type'    : 'an',
       'area'    : '-3.5/-39.00/-3.5/-39.1',   # North, West, South, East. Default: global
       'grid'    : '0.25/0.25',                    # Latitude/longitude. Default: spherical harmonics or reduced Gaussian grid
       'format'  : 'netcdf',                       # Output needs to be regular lat-lon, so only works in combination with 'grid'!
   }, 'Vel_1P_WS_ML_2000-2004.nc')                 # Output file. Adapt as you wish.

dataset = xr.open_dataset("Vel_1P_WS_ML_2000-2004.nc")

print(dataset)