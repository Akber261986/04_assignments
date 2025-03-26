planets = {
    "Mercury": 37.6,
    "Venus": 88.9,
    "Mars": 37.8,
    "Jupiter": 236.0,
    "Saturn": 108.1,
    "Uranus": 81.5,
    "Neptune": 114.0,
}

def main():
    user_input = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")
    planet_value = planets[planet]
    result = user_input * (planet_value/100)
    result = round(result, 2)
    print (f"Your {planet} weight is: {result}")

if __name__ == "__main__":
    main()