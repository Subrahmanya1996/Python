import geopy.geocoders
from geopy.geocoders import Nominatim
import pandas as pd
from functools import partial
geopy.geocoders.options.default_timeout = None
from geopy.extra.rate_limiter import RateLimiter
locator = Nominatim(user_agent='myGeocoder')
geolocator = Nominatim(user_agent="Geocoding")

df = pd.read_csv(R'C:\Users\subbu\Downloads\x.csv')
df.head(10)
df['ModAdd'] = df['Address']+' '+df['STATE']+' '+df['ZIP4'].astype(str)
geocode = RateLimiter(locator.geocode, min_delay_seconds=2)
df['location'] = df['ModAdd'].apply(geocode)
df['point'] = df['location'].apply(lambda loc: tuple(loc.point) if loc else None)
df[['latitude', 'longitude', 'altitude']] = pd.DataFrame(df['point'].tolist(), index=df.index)
df.drop(['altitude'])
df.to_csv('x.csv')
