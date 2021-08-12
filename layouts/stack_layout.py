import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.stacklayout import StackLayout

class MyStackLayoutApp(App):
    def build(self):
        layout = StackLayout(padding=5, spacing=10)
        for i in range(25):
            btn = Button(text=str(i), width=40 + i * 5, size_hint=(None, 0.15))
            layout.add_widget(btn)

        return layout 
 
if __name__ == "__main__":
   MyStackLayoutApp().run()