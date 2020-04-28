from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from models import check_database

Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'resizable', '0')


class Start(BoxLayout):
    """ Стартовое окно"""
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)

    def button_continue(self):
        """Реакция на нажатие кнопки "Продолжить" стартового окна"""
        if self.ids.text_input1.text == 'a':
            check_database()
        else: print('No')


    def button_add_subject(self):
        """Реакция на нажатие кнопки добавления нового учебного предмета"""
        print('Really OK')


class StartApp(App):
    def build(self):
        return Start()


start = StartApp()
if __name__ == '__main__':
    start.run()
