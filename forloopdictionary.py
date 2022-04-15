#!/usr/bin/ev python3

# challange: https://github.com/csfeeser/Python/blob/master/challenges/FOR%20LOOP%20DICTIONARY-%20farm_dictionary.md

farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]

vegetables =["carrots", "celery"]

def main():
    # Write a for loop that returns all the animals from the NE Farm!
    for animal in farms[0]["agriculture"]:
        print(animal)

    for farm in farms:
        print(farm["name"])

    choice = input("Choose a farm")

    for farm in farms:
        if farm["name"].lower() == choice.lower():
            print(farm["agriculture"])

    # not correct
    for x in farms[choice]["agriculture"]:
        if x not in vegetables:
            print(x)

main()