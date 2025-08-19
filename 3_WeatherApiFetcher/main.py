import requests

city = input("Enter city: ")
r = requests.get(f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric").json()
print(f"{city}: {r['weather'][0]['description']}, {r['main']['temp']}°C" if r.get("main") else "City not found!")
