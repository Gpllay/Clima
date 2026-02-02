import requests

# Coordenadas de São João del-Rei (exemplo)
latitude = -21.1311
longitude = -44.2526

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": latitude,
    "longitude": longitude,
    "hourly": "temperature_2m,precipitation",
    "timezone": "America/Sao_Paulo"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()
    print("Primeiras horas da previsão:")
    for t, temp, rain in zip(
        data["hourly"]["time"][:5],
        data["hourly"]["temperature_2m"][:5],
        data["hourly"]["precipitation"][:5]
    ):
        print(f"{t} → {temp}°C, chuva: {rain} mm")
else:
    print("Erro na requisição:", response.status_code)
