import flet as ft
import logging
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

ACCESS_ID = "xje5t5vu8cqcvvhadw78"
ACCESS_KEY = "68b3b2f2e6984ba4bf06be90a7ad78fa"
API_ENDPOINT = "https://openapi.tuyaus.com"

TUYA_LOGGER.setLevel(logging.DEBUG)

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Set up device_id
DEVICE_ID ="ebb63196d8a8ff3e05buvw"


def main(page: ft.Page):
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    flag = True

    def switch_led():
        nonlocal flag
        flag = not flag
        commands = {'commands': [{'code': 'switch_led', 'value': flag}]}
        openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

    nombre=ft.TextField(label="nombre disp")

    btn = ft.ElevatedButton(text="Pulsa para cambiar la luz", on_click=lambda e: switch_led())
    page.add(btn)

ft.app(target=main)
