########################################################################
## SPINN DESIGN CODE
# YOUTUBE: (SPINN TV) https://www.youtube.com/spinnTv
# WEBSITE: spinndesign.com
# TUTORIAL: KIVY
########################################################################

########################################################################
## IMPORTS
########################################################################
from random import random
# Import kivy app
from kivy.app import App
# Import kivy widget
from kivy.uix.widget import Widget
# Import kivy button
from kivy.uix.button import Button
# Import graphics
from kivy.graphics import Color, Ellipse, Line


########################################################################
## PAINT WIDGET CLASS
########################################################################
class MyPaintWidget(Widget):
    # Touch event listener
    def on_touch_down(self, touch):
        # Create random color
        color = (random(), 1, 1)
        # Draw
        with self.canvas:
            Color(*color, mode='hsv')
            # Ellipse size
            d = 30.
            # draw Ellipse
            Ellipse(pos=(touch.x - d / 2, touch.y - d / 2), size=(d, d))
            # Create touch points/ draw line
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):
        # Add touch points to draw a line
        touch.ud['line'].points += [touch.x, touch.y]

########################################################################
## MAIN CLASS
########################################################################
class MyPaintApp(App):
    # Build app UI
    def build(self):
        # Parent widget
        parent = Widget()
        # Painter Widget
        self.painter = MyPaintWidget()
        # Clear button
        clearbtn = Button(text='Clear')
        # Bind button event
        clearbtn.bind(on_release=self.clear_canvas)
        # Add widgets to parent
        parent.add_widget(self.painter)
        parent.add_widget(clearbtn)
        # Return parent
        return parent

    # A function to clear the canvas
    def clear_canvas(self, obj):
        self.painter.canvas.clear()

########################################################################
## RUN THE APP
######################################################################## 
if __name__ == '__main__':
    MyPaintApp().run()

########################################################################
## <== END ==>
########################################################################