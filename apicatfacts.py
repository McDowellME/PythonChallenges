#!usr/bin/env python3

# challange from https://github.com/csfeeser/Python/blob/master/challenges/API%20cat%20facts.md

import requests
import random

URL = "https://cat-fact.herokuapp.com/facts"

# Return the JSON from this API and convert it into a Python list (use requests.get())
resp = requests.get(URL)
catfacts = resp.json()

rando = []

# Loop through the data and print out the cat fact ONLY.
for cat in catfacts:
    rando.append(cat.get("text"))


# BONUS: return a RANDOM cat fact every time the script runs!
print(random.choice(rando))