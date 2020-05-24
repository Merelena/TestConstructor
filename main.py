from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from models import check_database, add_subject_to_db, open_db
from kivy.uix.popup import Popup
import test_constructor

Config.set('graphics', 'width', 800)
Config.set('graphics', 'height', 500)
Config.set('graphics', 'resizable', '0')

global subject, start, popup, flag, enable_continue


class StartApp(App):
    def build(self):
        global start
        self.title = 'Конструктор тестовых заданий'
        start = Start()
        return start


class Start(BoxLayout):
    """ Стартовое окно"""
    def __init__(self, **kwargs):
        super(Start, self).__init__(**kwargs)

    def button_continue(self):
        """Реакция на нажатие кнопки "Продолжить" стартового окна"""
        global flag, enable_continue
        flag = check_database(self.ids.text_input1.text)    # Проверка наличия учебного предмета в БД
        # Если учебного предмета нет в БД, появляется кнопка для добавления
        if not flag:
            start.ids.button1.opacity = 1
        else:
            start_app.stop()
            subject_file = open('subject.txt', 'w')
            subject_file.write(self.ids.text_input1.text)
            subject_file.close()


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


start_app = StartApp()

if __name__ == '__main__':
    open_db()
    from models import conn
    start_app.run()
    while not flag:
        continue
    conn.close()
    test_constr = test_constructor.TestConstructorApp()
    test_constr.run()
    conn.close()