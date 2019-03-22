from geopy.distance import geodesic
from geopy.distance import great_circle
from pyproj import Proj, transform
import math


## latLon EPSG: 4326
## polarstereo north EPSG: 3413
## polarstereo antarctic EPSG: 3031

## point 1
lat1 = -54.0
lon1 = 1.0

## point 2
lat2 = -54.0
lon2 = 2.0


## project
inProj = Proj(init='epsg:4326')
outProj = Proj(init='epsg:3031')
pLon1, pLat1 = transform(inProj, outProj, lon1, lat1)
pLon2, pLat2 = transform(inProj, outProj, lon2, lat2)
print("Projected point 1: ", pLat1, pLon1)
print("Projected point 2: ", pLat2, pLon2)
distProj = math.sqrt(((pLat1-pLat2)*(pLat1-pLat2)) + ((pLon1-pLon2)*(pLon1-pLon2)))/1000
print('Projected Distance: {} km'.format(distProj))

## geodetic
loc1 = (lat1, lon1)
loc2 = (lat2, lon2)
distGeo = geodesic(loc1, loc2).kilometers
print("Geodetic Distance: {} km".format(distGeo))

## using great circle distance
loc1 = (lat1, lon1)
loc2 = (lat2, lon2)
distGC = great_circle(loc1, loc2).kilometers
print("Great Circle Distance: {} km".format(distGC))

print("--")
print("Distortion from Projected Distance:")
print("Distortion Geodetic: {} %".format((1-distProj/distGeo)*100))
print("Distortion Great Circle: {} %".format((1-distProj/distGC)*100))
print("Distortion for 1 km: {} km".format((distProj-distGC)/distProj))

print("--")
print("Distortion from Geodetic and Great Circle Distance:")
print("Distortion Geodetic: {} %".format((1-distGeo/distProj)*100))
print("Distortion Great Circle: {} %".format((1-distGC/distProj)*100))