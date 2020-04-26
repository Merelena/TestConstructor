from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'resizable', '0')


class MainWindow(BoxLayout):
    def __init__(self, **kwargs):
        super(MainWindow, self).__init__(**kwargs)

    def on_press_button(self):
        print('Ok')


class TestConstructorApp(App):
    def build(self):
        return MainWindow()


constructor = TestConstructorApp()
if __name__ == '__main__':
    constructor.run()
