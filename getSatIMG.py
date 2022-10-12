api_url = "https://earth-search.aws.element84.com/v0"
from time import sleep
from pystac_client import Client

client = Client.open(api_url)

# collection: Sentinel-2, Level 2A, COGs
collection = "sentinel-s2-l2a-cogs"

# AMS coordinates
lat, lon = 52.37, 4.90
geometry = {"type": "Point", "coordinates": (lon, lat)}

mysearch = client.search(
    collections=[collection],
    intersects=geometry,
    max_items=10,
)
print(mysearch.matched())
items = mysearch.get_all_items()
print(len(items))
for item in items:
    print(item)
item = items[0]
print(item.datetime)
print(item.geometry)
print(item.properties)
assets = items[-1].assets  # last item's asset dictionary
print(assets.keys())
for key, asset in assets.items():
    print(f"{key}: {asset.title}")
print(assets["thumbnail"].href)
import rioxarray
visual_href = assets["visual"].href
visual = rioxarray.open_rasterio(visual_href)
# visual_clip.rio.to_raster("amsterdam_tci.tif", driver="COG")
