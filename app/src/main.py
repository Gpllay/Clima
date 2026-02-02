# Projeto Iniciado 02/02/2026 as 01:23
# Ultima Modificação:
# Inspirado em uma aula do Senai

import flet as ft
import requests


def main(page: ft.Page):
    # Coordenadas de São João del-Rei (exemplo)
    latitude = -21.1311
    longitude = -44.2526

    url = "https://api.open-meteo.com/v1/forecast"

    temperatura_agora = ft.Text("00.0 ºC", weight=ft.FontWeight.BOLD, size=50)
    condicao_atual = ft.Text("Sem informação", weight=ft.FontWeight.BOLD, size=40)

    def previsao_agora():
        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m,weather_code",
            "timezone": "America/Sao_Paulo"
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            data = response.json()
            atual = data["current"]

            temperatura = f"{atual['temperature_2m']} °C"
            umidade = f"{atual['relative_humidity_2m']}%"
            vento = f"Vento: {atual['wind_speed_10m']} km/h"
            #nuvem = atual["cloud_cover"]
            precipitacao = atual['precipitation']
            code = atual["weather_code"]


            temperatura_agora.value = temperatura

            #cloud_cover (%) - nuvem
            # 0–20    Ensolarado ☀️
            # 20–50   Parcialmente nublado 🌤️
            # 50–85   Nublado ⛅
            # 85–100  Céu totalmente encoberto ☁️

            if precipitacao > 0:
                print(f"Está chovendo agora! Intensidade: {precipitacao} mm")
            else:
                print("Não está chovendo no momento.")

            #weather_code
            # 0 -> Céu limpo
            # 1, 2 -> Parcialmente nublado
            # 3 -> Nublado
            # 45, 48 -> Neblina
            # 51–67 -> Chuvisco
            # 71–77 → Neve
            # 80–82 → Pancadas de chuva
            # 95–99 → Tempestade

            # Tabela oficial de códigos da Open-Meteo
            weather_codes = {
                0: "Céu limpo ☀️",
                1: "Principalmente limpo 🌤️",
                2: "Parcialmente nublado ⛅",
                3: "Nublado ☁️",
                45: "Nevoeiro 🌫️",
                48: "Nevoeiro com gelo 🌫️❄️",
                51: "Chuvisco leve 🌦️",
                53: "Chuvisco moderado 🌧️",
                55: "Chuvisco intenso 🌧️",
                56: "Garoa congelante leve ❄️🌧️",
                57: "Garoa congelante intensa ❄️🌧️",
                61: "Chuva leve 🌦️",
                63: "Chuva moderada 🌧️",
                65: "Chuva forte 🌧️🌧️",
                66: "Chuva congelante leve ❄️🌧️",
                67: "Chuva congelante forte ❄️🌧️",
                71: "Neve leve ❄️",
                73: "Neve moderada ❄️❄️",
                75: "Neve forte ❄️❄️❄️",
                77: "Grãos de neve ❄️",
                80: "Pancadas de chuva leves 🌦️",
                81: "Pancadas de chuva moderadas 🌧️",
                82: "Pancadas de chuva fortes ⛈️",
                85: "Pancadas de neve leves ❄️🌨️",
                86: "Pancadas de neve fortes ❄️🌨️❄️",
                95: "Tempestade ⛈️",
                96: "Tempestade com granizo ⛈️🧊",
                99: "Tempestade forte com granizo ⛈️🧊"
            }

            condicao = weather_codes.get(code, "Código desconhecido")

            print(f"Weather code: {code}")
            print(f"Condição atual: {condicao}")

            condicao_atual.value = condicao


            print("Clima agora:")
            print(f"Hora: {atual['time']}")
            print(f"Temperatura: {atual['temperature_2m']} °C")
            print(f"Umidade: {atual['relative_humidity_2m']}%")
            print(f"Chuva: {atual['precipitation']} mm")
            print(f"Vento: {atual['wind_speed_10m']} km/h")

            page.update()


        else: print("Erro na requisição:", response.status_code)

    page.appbar = ft.AppBar(
        title="Previsão",
        bgcolor="#000000",
        actions=[
            ft.TextField(label="Cidade")
        ]
    )

    layout = ft.Stack(
        expand=True,
        controls=[
            ft.Image(
                src="https://10wallpaper.com/wallpaper/3840x2400/1712/Snow_mountains_night_sky_stars_4K_HD_Desktop_3840x2400.jpg",
                fit=ft.BoxFit.COVER,
                width=1920,
            ),
            ft.Container(
                ft.Row([
                    ft.Column([
                        ft.Text("Clima Agora:"),
                        condicao_atual
                    ], expand=True, spacing=0),
                    ft.Column([
                        ft.Text("Temperatura Agora:"),
                        temperatura_agora
                    ], expand=True, spacing=0),
                ]),
                padding = 10
            )
        ]
    )

    page.add(
       ft.Column([
           ft.Row([
               ft.Container(
                   content=layout,
                   bgcolor=ft.Colors.GREEN,

                   expand=True,
                   #padding=10,
                   border_radius=10,
               )
           ], height = 120),
           ft.Button("Buscar", on_click=previsao_agora),
       ])
    )


ft.run(main)
