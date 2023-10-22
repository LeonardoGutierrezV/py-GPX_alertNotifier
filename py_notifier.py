import threading
import time
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import mainthread



class MainWidget(BoxLayout):
    label_str = StringProperty("")
    def __init__(self, *args, **kwargs):
        super(MainWidget, self).__init__(*args, **kwargs)
        self.orientation = "vertical"

        self.label = Label(text=self.label_str)
        self.bind(label_str=self.label.setter('text'))
        self.add_widget(self.label)
        self.add_widget(Button(text="Iniciar hilo", on_press=self.iniciar_hilo))

    def iniciar_hilo(self, *args):
        if self.label_str == '':
            t = threading.Thread(target=self.worker)
            t.start()

    def worker(self):
        self.update_label("Iniciando")
        time.sleep(1)
        for n in range(10):
            self.update_label(str(n))
            time.sleep(1)
        self.update_label("Terminado")
        time.sleep(1)
        self.update_label("")

    @mainthread
    def update_label(self, value):
        self.label_str = value



class MyApp(App):
    def build(self):
        return MainWidget()


if __name__ == '__main__':
    MyApp().run() 
