#!/usr/bin/env kivy

import kivy
import uuid

kivy.require('1.8.0')

from kivy.app import App
from kivy.properties import NumericProperty, ReferenceListProperty,ObjectProperty, StringProperty

from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.textinput import TextInput

from lxml import etree

class TileScreen(Screen):

    up = ObjectProperty(None)
    box = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(TileScreen, self).__init__(**kwargs)

    def add_button(self, button):
        self.box.add_widget(button)

class InfoScreen(Screen):

    name_value = ObjectProperty()

class ScreenSwitchButton(Button):

    sub_screen = StringProperty()
    view = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(ScreenSwitchButton, self).__init__(**kwargs)


def parse_display_elements(screenHandler, display_element, parent_screen_id=None):
    tiles = display_element.findall('tile')
    screen_id = str(uuid.uuid4())
    view = None
    if len(tiles):
        # Is Tiles
        view = TileScreen(name=screen_id)
        for tile in tiles:
            b = ScreenSwitchButton(text=tile.find('name').text)
            b.view = view
            sub_display = tile.find('display')
            if sub_display is not None:
                b.sub_screen = parse_display_elements(screenHandler, sub_display, screen_id)
            view.add_button(b)
    else:
        info = display_element.find('info')
        view = InfoScreen(name=screen_id)
        view.name_value.text = info.find('title').text


    if view is not None:
        if parent_screen_id is not None:
            view.up.sub_screen = parent_screen_id
            view.up.view = view
        screenHandler.add_widget(view)
        return screen_id
    return None

def parse_xml_file(screenHandler):
    doc = etree.parse('hth.xml')
    display = doc.find('display')
    if display is not None:
        current_screen = parse_display_elements(screenHandler, display)
        screenHandler.current = current_screen

class DisplayPortal(BoxLayout):

    screenHandler = ObjectProperty(None)

    def __init__(self, **kwargs):
        super(DisplayPortal, self).__init__(**kwargs)
        parse_xml_file(self.screenHandler)


class H2HApp(App):

    def build(self):
        return DisplayPortal()



if __name__ == '__main__':
    H2HApp().run()

