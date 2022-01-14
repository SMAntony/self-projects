from math import radians, cos, sin, asin, sqrt
common_cities = {"Nagercoil": [11.059821, 78.387451],
"Kanyakumari": [23.745127, 91.746826]}
r = 6371 # Radius of earth in km

City1 = input("Enter the name of first city/state: ")
City2 = input("Enter the name of second city/state: ")

lat1 = radians(float(input(f"Enter the latitude of {City1}: ",)))
lon1 = radians(float(input(f"Enter the longtitude of {City1}: ")))
lat2 = radians(float(input(f"Enter the latitude of {City2}: ")))
lon2 = radians(float(input(f"Enter the longtitude of {City2}: ")))


def calculate_Haversine_formula(lat1, lat2, lon1, lon2):
    # implementing Haversine formula
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    d = 2 * r * asin(sqrt(sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2))
    return d

print(calculate_Haversine_formula(lat1, lat2, lon1, lon2), " km",sep = "")

#future plans
#1. Make it so that new cities entered will be appened to the dictionary
#2. Make it so that when city mentioned has long n lat values in the dict, do not ask the user

