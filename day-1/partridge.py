import math
import json


def calc_fuel_for_module(mass):
    def calc_fuel(mass):
        return math.floor(mass / 3) - 2
    total = 0
    new_mass = calc_fuel(mass)
    while new_mass > 0:
        total += new_mass
        new_mass = calc_fuel(new_mass)
    return total


with open('./masses.json', 'r') as f:
    raw = f.read()
    masses = json.loads(raw)
    total = 0
    for mass in masses:

        total = total + calc_fuel_for_module(mass)
    print(f'Total: {total}')
