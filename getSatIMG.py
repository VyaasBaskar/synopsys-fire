api_url = "https://earth-search.aws.element84.com/v0"
from time import sleep
from pystac_client import Client
import os
from PIL import Image
from func_timeout import *

client = Client.open(api_url)

# collection: Sentinel-2, Level 2A, COGs
collection = "sentinel-s2-l2a-cogs"

# AMS coordinates
lat, lon = 37.3020, -121.9970
geometry = {"type": "Point", "coordinates": (lon, lat)}

mysearch = client.search(
    collections=[collection],
    intersects=geometry,
    max_items=10,
)
#print(mysearch.matched())
items = mysearch.get_all_items()
#print(len(items))
#for item in items:
#    print(item)
item = items[0]
#print(item.datetime)
#print(item.geometry)
#print(item.properties)
assets = items[-1].assets  # last item's asset dictionary
#print(assets.keys())
#for key, asset in assets.items():
#    print(f"{key}: {asset.title}")
#print(assets["thumbnail"].href)
import rioxarray
visual_href = assets["visual"].href
visual = rioxarray.open_rasterio(visual_href)

@func_set_timeout(10)
def out_tif():
    visual.rio.to_raster("out.tif")#, cache=False)#, tiled=True, windowed=True)
    visual.close()

im = Image.open('out.tif')
im.thumbnail(im.size)
im.save('out.jpeg', "JPEG", quality=100)