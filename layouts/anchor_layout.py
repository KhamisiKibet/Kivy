# Imports
import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout

# Main class
class MyAnchorLayoutApp(App):
    # Build UI
    def build(self):
        # Create layout
        layout = AnchorLayout(
                # anchor_x: left, right center
                # anchor_y: top, bottom center
                anchor_x='center', 
                anchor_y='center'
                )
        # Create button
        btn = Button(text='Hello World', 
            # Relative size to parent (50%)
            size_hint=(.2, .2)
            )
        # Add button to layout
        layout.add_widget(btn)
        # Return layout
        return layout 
 
if __name__ == "__main__":
   MyAnchorLayoutApp().run()