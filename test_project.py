from project import k_to_f, sort, format_time
from datetime import datetime

def test_k_to_f():
    assert k_to_f(100) == -279.67
    assert k_to_f(273.15) == 32
    assert k_to_f(453.15) == 356

def test_sort():
    city1 = {"Name": "Irvine", "Temperature": 70}
    city2 = {"Name": "Ontario", "Temperature": 40}
    cities = [city1, city2]
    assert sort(cities, "Temperature")[0]["Name"] == "Ontario"

def test_format_time():
    time = 1704067200 #12:00 AM new years 2024
    assert format_time(time) == "12:00 AM"
