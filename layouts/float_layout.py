# Imports
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout

# Main class
class MyFloatLayoutApp(App):
    # Build UI
    def build(self):
        # Create layout
        layout = FloatLayout(
            size=(300, 300)
            )
        button = Button(text='Hello world')
        # button = Button(
        #             text='Hello world',
        #             size_hint=(.5, .25),
        #             pos=(100, 200) #Absolute position
        # )
        # button = Button(
        #         text='Hello world', 
        #         size_hint=(.2, .2),
        #         pos_hint={'x':.5, 'y':.5} #relative postion
        #     )

        layout.add_widget(button)
        return layout 
 
if __name__ == "__main__":
   MyFloatLayoutApp().run()