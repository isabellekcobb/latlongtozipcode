from arcgis.geocoding import reverse_geocode
from arcgis.geometry import Geometry
from arcgis.gis import GIS
import pandas as pd

gis = GIS("http://www.arcgis.com", "***", "***")
csv_input = pd.read_csv('path_result_plot.csv')
Lat=csv_input['latitude']
Lon=csv_input['longitude']

def get_zip(df, lon_field, lat_field):
    location = reverse_geocode((Geometry({"x":float(df[lon_field]), "y":float(df[lat_field]), "spatialReference":{"wkid": 4326}})))
    return location['address']['Postal']

zipcodes = df.apply(get_zip, axis=1, lat_field='Lat', lon_field='Lon')

with open('zipcodes.txt','w') as file:
    file.write(zipcodes)
