from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout


class SeaBattleApp(App):
    bl = BoxLayout()
    widget = Widget()
    bl.add_widget(widget)
    with widget.canvas:
        Color = (1, .5,.5 ,.5)

if __name__ == '__main__':
    SeaBattleApp().run()
