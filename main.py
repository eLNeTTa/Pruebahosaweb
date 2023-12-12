import logging
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from tuya_connector import TuyaOpenAPI, TUYA_LOGGER

ACCESS_ID = "xje5t5vu8cqcvvhadw78"
ACCESS_KEY = "68b3b2f2e6984ba4bf06be90a7ad78fa"
API_ENDPOINT = "https://openapi.tuyaus.com"

TUYA_LOGGER.setLevel(logging.DEBUG)

openapi = TuyaOpenAPI(API_ENDPOINT, ACCESS_ID, ACCESS_KEY)
openapi.connect()

# Set up device_id
DEVICE_ID = "ebb63196d8a8ff3e05buvw"


class MyApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=10)

        self.flag = True

        def switch_led(instance):
            self.flag = not self.flag
            commands = {'commands': [{'code': 'switch_led', 'value': self.flag}]}
            openapi.post('/v1.0/iot-03/devices/{}/commands'.format(DEVICE_ID), commands)

        nombre = TextInput(text="Nombre disp")

        btn = Button(text="Pulsa para cambiar la luz")
        btn.bind(on_press=switch_led)

        layout.add_widget(nombre)
        layout.add_widget(btn)

        return layout


if __name__ == '__main__':
    MyApp().run()
