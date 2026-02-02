import flet as ft
import requests


def main(page: ft.Page):
    # Coordenadas de São João del-Rei (exemplo)
    latitude = -21.1311
    longitude = -44.2526

    url = "https://api.open-meteo.com/v1/forecast"

    temperatura_agora = ft.Text("00.0 ºC", weight=ft.FontWeight.BOLD, size=50)

    def previsao_agora():
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
            "timezone": "America/Sao_Paulo"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            atual = data["current"]

            temperatura = f"{atual['temperature_2m']} °C"
            umidade = f"{atual['relative_humidity_2m']}%"
            precipitacao = atual['precipitation']


            print("Clima agora:")
            print(f"Hora: {atual['time']}")
            print(f"Temperatura: {atual['temperature_2m']} °C")
            print(f"Umidade: {atual['relative_humidity_2m']}%")
            print(f"Chuva: {atual['precipitation']} mm")
            print(f"Vento: {atual['wind_speed_10m']} km/h")

        else: print("Erro na requisição:", response.status_code)

    page.appbar = ft.AppBar(
        title="Previsão",
        bgcolor="#000000",
        actions=[
            ft.TextField(label="Cidade")
        ]
    )

    page.add(
       ft.Column([
           ft.Row([
               ft.Container(
                   content=ft.Column([
                       ft.Row([temperatura_agora]),
                   ]),
                   bgcolor=ft.Colors.GREEN,

                   expand=True,
                   padding=10,
                   border_radius=10,
               )
           ]),
           ft.ElevatedButton("Buscar", on_click=previsao_agora),
       ])
    )


ft.run(main)
