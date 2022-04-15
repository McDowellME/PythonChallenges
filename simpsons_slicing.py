#!/usr/bin/env python3

# challange: https://github.com/csfeeser/Python/blob/master/challenges/SLICING-%20simpsons.md

challenge= ["science", "turbo", ["goggles", "eyes"], "nothing"]


trial= ["science", "turbo", {"eyes": "goggles", "goggles": "eyes"}, "nothing"]


nightmare= [{"slappy": "a", "text": "b", "kumquat": "goggles", "user":{"awesome": "c", "name": {"first": "eyes", "last": "toes"}},"banana": 15, "d": "nothing"}]

def main():
    eyes = challenge[2][1]
    goggles = challenge[2][0]
    nothing = challenge[3]

    print(f"My {eyes}! The {goggles} do {nothing}!")
    
    eyes = list(trial[2].keys())[0]
    goggles = list(trial[2].keys())[1]
    nothing = trial[3]

    print(f"My {eyes}! The {goggles} do {nothing}!")

    eyes = nightmare[0]["user"]["name"]["first"]
    goggles = nightmare[0]["kumquat"]
    nothing = nightmare[0]["d"]

    print(f"My {eyes}! The {goggles} do {nothing}!")
main()