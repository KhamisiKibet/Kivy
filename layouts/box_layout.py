# Imports
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

# Main class
class MyBoxLayoutApp(App):
    # Build UI
    def build(self):
        # Create UI
        layout = BoxLayout(
            # Orientation: vertical/horizontal
            orientation='horizontal', 
            # Space between widgets
            spacing=10, 
            # Paddind space
            padding=10
            )
        # Create buttons
        btn1 = Button(text='Hello', 
            size_hint=(.7, 1) #70% of parent width and 100% of parent height
            )
        
        btn2 = Button(text='World')
        # Add buttons to layout
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        # Return layout
        return layout 
 
if __name__ == "__main__":
   MyBoxLayoutApp().run()