#!/usr/bin/env python3

# challenge: https://github.com/csfeeser/Python/blob/master/challenges/DICTIONARIES-%20tuesday.md

def main():

    # Save a user's input to the variable char_name from the following question:
    #  Which character do you want to know about? (Starlord, Mystique, Hulk)
    char_name = input("Which character do you want to know about? (Starlord, Mystique, Hulk)\n").capitalize()
    # char_name = char_name.lower()
    # char_name = char_name.capitalize()

    # Save a user's input to the variable char_stat from the following question:
    #  What statistic do you want to know about? (real name, powers, archenemy)
    char_stat = input("What statistic do you want to know about? (real name, powers, archenemy)\n").lower()
    # char_stat = char_stat.lower()

    # dictionary
    marvelchars = {
    "Starlord":
    {"real name": "peter quill",
    "powers": "dance moves",
    "archenemy": "Thanos"},

    "Mystique":
    {"real name": "raven darkholme",
    "powers": "shape shifter",
    "archenemy": "Professor X"},

    "Hulk":
    {"real name": "bruce banner",
    "powers": "super strength",
    "archenemy": "adrenaline"}
                } 

    # Use the char_name and char_stat values to pull the appropriate value from the dictionary above.
    value = marvelchars[char_name][char_stat]

    # Create a print function that combines that information into this output:
    #  <char_name>'s <char_stat> is: <value>
    print(f"{char_name}'s {char_stat} is: {value}")

main()