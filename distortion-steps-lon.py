'''
Calculates distortion in distance of a projection by stepping through different longitudes
'''
from geopy.distance import great_circle
from pyproj import Proj, transform
import math


def distortion(lat1, lon1, lat2, lon2, epsg):
    inProj = Proj(init='epsg:4326')

    ### for EPSG code projection
    # epsg='epsg:'+epsg
    # outProj = Proj(init=epsg)

    ### for dynamic projection
    outProj1 = Proj(epsg.format(lat1))
    outProj2 = Proj(epsg.format(lat2))
    pLon1, pLat1 = transform(inProj, outProj1, lon1, lat1)
    pLon2, pLat2 = transform(inProj, outProj2, lon2, lat2)

    ### calculate projected distance
    distProj = math.sqrt(((pLat1-pLat2)*(pLat1-pLat2)) + ((pLon1-pLon2)*(pLon1-pLon2)))/1000

    ## using great circle distance
    loc1 = (lat1, lon1)
    loc2 = (lat2, lon2)
    distGC = great_circle(loc1, loc2).kilometers

    ### print distortion of projected distance
    print("{} \t {} %".format(lon1, abs(1-distGC/distProj)*100))


if __name__== "__main__":
    # define latitudes, longitude and projection string
    lat1 = 75.0
    lat2 = 76.0
    lon = -180.0
    proj4 = "+proj=stere +lat_0=90 +lat_ts={} +lon_0=0 +k=1 +x_0=0 +y_0=0 +datum=WGS84 +units=m +no_defs"

    # step through longitudes
    while lon < 180.0:
        if lon != 0.0:
            distortion(lat1, lon, lat2, lon, proj4)
        lon = lon+5.0
