'''
Application built from a  .kv file
==================================

After Kivy instantiates a subclass of App, it implicitly searches for a .kv
file. The file test.kv is selected because the name of the subclass of App is
TestApp, which implies that kivy should try to load "test.kv". That file
contains a root Widget.
'''
# Imports
import kivy
kivy.require('1.0.7')
from kivy.app import App
from kivy.core.window import Window
# from kivy.uix.image import AsyncImage

# Main class
class ImageViewerApp(App):
    # Specify the .kv directory
    # kv_directory = 'templates'
    # Window.clearcolor = (255, 76, 41, 1)
    pass


if __name__ == '__main__':
    ImageViewerApp().run()