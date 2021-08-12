# App imports
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout

class MyGridLayoutApp(App):
    # Build UI
    def build(self):
        # Create UI
        # layout = GridLayout(
        #     # Grid columns
        #     cols=2
        #     )
        # Add Grid widgets
        # layout.add_widget(Button(text='Hello 1'))
        # layout.add_widget(Button(text='World 1'))
        # layout.add_widget(Button(text='Hello 2'))
        # layout.add_widget(Button(text='World 2'))

        # layout.add_widget(Button(text='Hello 1', size_hint_x=None, width=100))
        # layout.add_widget(Button(text='World 1'))
        # layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
        # layout.add_widget(Button(text='World 2'))

        # layout = GridLayout(cols=2, 
        #     # Force widgets to match grid size
        #     row_force_default=True, 
        #     row_default_height=20
        #     )

        # layout.add_widget(Button(text='Hello 1', size_hint_x=None, width=100))
        # layout.add_widget(Button(text='World 1', size_hint_y=None, height=100))
        # layout.add_widget(Button(text='Hello 2', size_hint_x=None, width=100))
        # layout.add_widget(Button(text='World 2'))

        layout = GridLayout(
            # Grid columns
            cols=2, 
            # Grid rows
            rows = 5, 
            # Paddind space
            padding=100,
            # Space between widgets 
            spacing=20
            )

        layout.add_widget(Button(text='Hello 1'))
        layout.add_widget(Button(text='World 1'))
        layout.add_widget(Button(text='Hello 2'))
        layout.add_widget(Button(text='World 2'))


        return layout 
 
if __name__ == "__main__":
   MyGridLayoutApp().run()