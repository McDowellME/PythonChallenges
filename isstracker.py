#!/usr/bin/env python3

# challenge: https://github.com/csfeeser/Python/blob/master/challenges/API%20CHALLENGE-%20ISS.md

import requests
import datetime
# install: python3 -m pip install reverse_geocoder
import reverse_geocoder as rg

ISS_URL = "http://api.open-notify.org/iss-now.json"

def main():
    # access API and translate the JSON
    iss_dict = requests.get(ISS_URL).json()
    
    lat = iss_dict["iss_position"]["latitude"]
    lon = iss_dict["iss_position"]["longitude"]
    # use datetime to translate timestamp
    timestamp = datetime.datetime.fromtimestamp(iss_dict["timestamp"])

    # make lat and lon tuple for reverse geocoder
    coords_tuple = (lat, lon)
    # search with tuple
    geo_result = rg.search(coords_tuple)

    # slice to name and cc
    city = geo_result[0]["name"]
    country = geo_result[0]["cc"]
    location = f"{city}, {country}"

    print(f"CURRENT LOCATION OF THE ISS: \nTimestamp: {timestamp}\nLon: {lon}\nLat: {lat}\nLocation: {location}")

main()