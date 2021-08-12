# Imports
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.pagelayout import PageLayout

# Main class
class MyPageLayoutApp(App):
    # Build UI
    def build(self):
        # Create layout
        layout = PageLayout()
        # Add widgets
        layout.add_widget(Button(text='Page 0'))
        layout.add_widget(Button(text='Page 1'))
        layout.add_widget(Button(text='Page 2'))
        layout.add_widget(Button(text='Page 3'))
        layout.add_widget(Button(text='Page 4'))
        layout.add_widget(Button(text='Page 5'))

        return layout 
 
if __name__ == "__main__":
   MyPageLayoutApp().run()