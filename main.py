from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.config import Config
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from models import check_database, add_subject_to_db
from kivy.uix.popup import Popup

Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'resizable', '0')

global subject, start, popup


class Start(BoxLayout):
    """ Стартовое окно"""
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)

    def button_continue(self):
        """Реакция на нажатие кнопки "Продолжить" стартового окна"""
        flag = check_database(self.ids.text_input1.text)    # Проверка наличия учебного предмета в БД
        # Если учебного предмета нет в БД, появляется кнопка для добавления
        if not flag:
            self.ids.button1.opacity = 1

    def button_add_subject(self):
        """Реакция на нажатие кнопки добавления нового учебного предмета"""
        global popup
        popup = AddSubject()
        popup.open()


class AddSubject(Popup):
    """Окно добавления нового учебного предмета"""
    def __init__(self, **kwargs):
        super(AddSubject, self).__init__(**kwargs)

    def add_subject(self):
        global subject
        subject = self.ids.text_input2.text
        add_subject_to_db(subject)
        popup.dismiss()
        start.ids.button1.opacity = 0
        start.ids.text_input1.text = subject
        print(subject)

    def delete_text(self):
        self.ids.text_input2.text = ''


class TestConstructorApp(App):
    def build(self):
        global start
        start = Start()
        return start


if __name__ == '__main__':
    TestConstructorApp().run()
