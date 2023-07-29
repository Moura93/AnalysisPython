# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:12:39 2023

@author: Felipe Moura
"""

import ephem # pip install pyephem (on Python 2)
             # pip install ephem   (on Python 3)
import math
import datetime

def solartime(observer, sun=ephem.Sun()):
    sun.compute(observer)
    # sidereal time == ra (right ascension) is the highest point (noon)
    hour_angle = observer.sidereal_time() - sun.ra
    return ephem.hours(hour_angle + ephem.hours('12:00')).norm  # norm for 24h

def ul_time(observer):
    utc_dt = observer.date.datetime()
    longitude = observer.long
    return utc_dt + datetime.timedelta(hours=longitude/math.pi * 12)


# "solar time" for some other cities
for name in ['Los Angeles', 'New York', 'London',
             'Paris', 'Moscow', 'Beijing', 'Tokyo']:
    city = ephem.city(name)
    print("%-11s %11s %s" % (name, solartime(city), ul_time(city).strftime('%T')))

# set date, longitude manually
o = ephem.Observer()
o.date = datetime.datetime(2012, 4, 15, 1, 0, 2) # some utc time
o.long = '00:00:00.0' # longitude (you could also use a float (radians) here)
print("%s %s" % (solartime(o), ul_time(o).strftime('%T')))