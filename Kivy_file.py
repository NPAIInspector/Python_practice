import Kivy

from Kivy.app import App
from Kivy.uix.button import Label


class sample(App):
    def build(self):
        return Label(text = "Hello Python!!!")

if __name__ == "__main__":
    sample().run()

    