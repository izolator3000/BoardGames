from back_end.myapp import myApp
from kivy.app import App
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button


class Application(App):





    def build(self):
        def enterValue(self):
            t.text = "3"
            l.text = "4"

        # play = myApp()

        grid = GridLayout(cols=1)

        l = Label(text="Мой текст: ",
                  size_hint=(1, .4),
                  font_size=30, height=10)

        t = TextInput(text="Ещё один текст", size_hint=(1, .3), font_size=20,
                      height=100)

        b = Button(text="Ввести значение", size_hint=(1, .3))
        b.bind(on_press=enterValue)

        grid.add_widget(l)
        grid.add_widget(t)
        grid.add_widget(b)
        return grid

