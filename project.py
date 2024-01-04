import requests
from datetime import datetime
from tabulate import tabulate
import sys

class City_2:
    API_KEY = open('api_key.txt', "r").read()
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather?appid=" + API_KEY + "&q="
    cities = []

    def __init__ (self, name):
        url = self.BASE_URL + name
        response = requests.get(url).json()
        try:
            self.name = name
            self.temperature = k_to_f(response["main"]["temp"])
            self.feels_like =  k_to_f(response["main"]["feels_like"])
            self.humidity = response["main"]["humidity"]
            self.local_time = format_time(response["dt"] + response["timezone"])
            self.add_city(self)
        except Exception:
            raise ValueError ("City doesn't exist!")

    @classmethod 
    def select_city(cls):
        #used at the beginning of using city class, or when adding a new city
        if len(cls.cities) == 0:
            print ("Welcome to the Weather Tracker! Enter a city to get started.")
        while True:
            user_city = input ("City to add: ")
            try:
                City_2(user_city.title())
                break
            except ValueError:
                print ("City doesn't exist!")

    @classmethod 
    def get_action(cls):
        cls.print_cities()
        print()
        header = ["Key", "Action"]
        contents = [["A", "Add City"], ["R", "Remove City"], ["S", "Sort By Category"], ["C", "Close Program"], ]
        print(tabulate(contents, header, tablefmt="grid"))
        action = input ("Action: ")
        
        match action.lower():
            case "a":
                cls.select_city()
            case "r":
                cls.remove_city()
            case "s":
                cls.sort_by()
            case "c":
                sys.exit ("Program closed")
            case _:
                print ("Invalid action!")
            

    @staticmethod
    def add_city(self):
        #adds new city object to cities[] list
        city = {"name": self.name, "temperature": self.temperature, "feels like": self.feels_like, "humidity": self.humidity,
                "local time": self.local_time}
        self.cities.append(city)

    @classmethod
    def remove_city (cls):
        break_out = False
        while True:
            user_remove = input ("City to remove: ").lower()
            for city in cls.cities:
                if user_remove == city["name"].lower(): 
                    cls.cities.remove(city)
                    break_out = True
                    break
            if break_out == True:
                break
            else:
                print ("City doesn't exist!")

    @classmethod
    def sort_by(cls):
        #prints list of commands for user to enter, sorts by category
        header = ["Key", "Value to Sort By"]
        contents = [["N", "Name"], ["T", "Temperature"], ["F", "Feels like"], ["H", "Humidity"], ["L", "Local time"]]
        print(tabulate(contents, header, tablefmt="grid"))
        while True:
            user_sort = input ("Sort by: ").lower()
            match user_sort:
                case "n":
                    cls.cities = sort(cls.cities, "name")
                    break
                case "t":
                    cls.cities = sort(cls.cities, "temperature")
                    break
                case "f":
                    cls.cities = sort(cls.cities, "feels like")
                    break
                case "h":
                    cls.cities = sort(cls.cities, "humidity")
                    break
                case "l":
                    cls.cities = sort(cls.cities, "local time")
                    break
                case _:
                    print ("Invalid command!")
    
    @classmethod
    def print_cities(cls):
        print()
        header = ["City name", "Temperature", "Feels Like", "Humidity", "Local Time",]
        contents = []
        for c in cls.cities:
            contents.append([c["name"], f"{c['temperature']}°F", f"{c['feels like']:.2f}°F", 
                             f"{c['humidity']}%", c['local time'],])
        print ("Weather Tracker:")
        print(tabulate(contents, header, tablefmt="grid"))

#####################################################################################################################3
        
def sort (arr, keyVal):
        return sorted(arr, key = lambda k : k[keyVal])

def k_to_f(temp):
        return float(f"{((temp-273.15) * 9/5 + 32):.2f}")

def format_time(time):
    return datetime.utcfromtimestamp(time).strftime("%#I:%M %p")


def main():
    City_2.select_city()
    while True:
        City_2.get_action()

if __name__ == "__main__":
    main()