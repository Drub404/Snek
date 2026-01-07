print("I have information for the following planets:\n")

print("   1. Venus   2. Mars    3. Jupiter")
print("   4. Saturn  5. Uranus  6. Neptune\n")

# Asks user for desired planet to visit and own weight
my_weight = int(input("What is your weight in kg?: "))
my_planet = int(input("What planet will you be visiting (1-6)?: "))

# Dictionairy that holds name of planet and relative gravity of each planet
gravity = {
    1: {"name": "Venus", "value": 0.91},
    2: {"name": "Mars", "value": 0.38},
    3: {"name": "Jupiter", "value": 2.34},
    4: {"name": "Saturn", "value": 1.06},
    5: {"name": "Uranus", "value": 0.92},
    6: {"name": "Neptune", "value": 1.19},
}

# Checks if entered weight is <= to 0
if my_weight <= 0:
    print("You have entered an invalid weight!")

# Checks if given planet number is not listed in gravity dictionairy
elif my_planet not in gravity:
    print("You must enter a valid planet number!")

# If all else = False then execute the calculation of user weight * relative gravity of chosen planet
else:
    my_planet_value = gravity[my_planet] # Sets number chosen to the right key in dictionairy gravity
    my_planet_name = my_planet_value["name"] # Uses the key to look for the planets name
    destination_weight = round(my_weight * my_planet_value["value"]) # Actual calculation of new weight
    print(f"You would weigh {destination_weight}kg on {my_planet_name}!")
