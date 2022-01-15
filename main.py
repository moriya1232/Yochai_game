from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder
width_height_image = 150
width_left_screen = 500
speed_run = 50

Builder.load_file("animation.kv")

class AwesomeApp(App):
    global Window
    width = 1000
    height = 300

    def build(self):
        Window.clearcolor = (127/256, 233/256, 131/256, 0.2)
        Window.size = (self.width, self.height)
        self.title = 'אליעזר ילד שהוא גזר'
        return MyLayout()

class MyLayout(Widget):
    pass


def eli_game():
    AwesomeApp().run()


if __name__ == '__main__':
    eli_game()

