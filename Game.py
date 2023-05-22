import random
import time

# Game Settings
MAX_POWER = 100
POWER_CONSUMPTION_RATE = 10
CHARGE_AMOUNT = 50
MAX_CHARGING_STATIONS = 5
WEATHER_CONDITIONS = ["Sunny", "Rainy", "Sandstorm"]
MAX_DISTANCE = 10

# Rover class
class Rover:
    def __init__(self):
        self.power = MAX_POWER
        self.distance = 0
        self.charging_stations = []
    
    def move(self):
        if self.power > 0:
            self.distance += 1
            self.power -= POWER_CONSUMPTION_RATE
    
    def charge(self, station):
        if self.power < MAX_POWER:
            self.power = min(self.power + CHARGE_AMOUNT, MAX_POWER)
            station.used = True
            print("Rover charged at Charging Station!")
        else:
            print("Rover power is already at maximum!")

# Charging Station class
class ChargingStation:
    def __init__(self, position):
        self.position = position
        self.used = False

# Weather class
class Weather:
    def __init__(self):
        self.current_condition = "Sunny"
    
    def change_weather(self):
        self.current_condition = random.choice(WEATHER_CONDITIONS)

# Game initialization
rover = Rover()
weather = Weather()
charging_stations = [ChargingStation(random.randint(1, MAX_DISTANCE)) for _ in range(MAX_CHARGING_STATIONS)]

# Game loop
while rover.distance < MAX_DISTANCE:
    print(f"Rover Distance: {rover.distance}")
    print(f"Rover Power: {rover.power}/{MAX_POWER}")
    print(f"Weather: {weather.current_condition}\n")
    
    # Rover movement
    rover.move()
    
    # Check for weather events
    weather.change_weather()
    if weather.current_condition == "Sandstorm":
        print("Warning: Sandstorm! Rover movement impaired.")
        time.sleep(2)
    elif weather.current_condition == "Rainy":
        print("Warning: Rainy weather! Rover power consumption increased.")
        time.sleep(2)
    
    # Check if rover encounters a charging station
    for station in charging_stations:
        if station.position == rover.distance and not station.used:
            rover.charge(station)
            break
    
    # Check if rover runs out of power
    if rover.power <= 0:
        print("Rover ran out of power! Game Over.")
        break
    
    time.sleep(1)

# Game over
print("\n--- Game Over ---")
print(f"Final Distance: {rover.distance}")
print(f"Final Power: {rover.power}/{MAX_POWER}")
