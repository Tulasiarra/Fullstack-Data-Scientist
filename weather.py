import random
def simulate_weather():
    weather = random.choice(["Sunny", "Rainy", "Cloudy", "Windy"])
    temp = random.randint(20, 40)
    print(f"Weather: {weather}, Temp: {temp}°C")
simulate_weather()
