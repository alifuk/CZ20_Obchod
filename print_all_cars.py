import requests

r = requests.get("http://127.0.0.1:8000/api/car/get_all")
cars = r.json()

for car in cars.values():
    print(car['brand'])
pass