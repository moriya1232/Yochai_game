from kivy.core.window import Window
from kivy.app import App
from kivy.event import EventDispatcher
from kivy.graphics.vertex_instructions import Ellipse
from kivy.properties import Clock, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.lang import Builder



Builder.load_file("animation.kv")




class AwesomeApp(App):
    WIDTH_SCREEN = 1000
    HEIGHT_SCREEN = 500
    global Window

    def build(self):
        Window.clearcolor = (127/256, 233/256, 131/256, 0.2)
        Window.size = (self.WIDTH_SCREEN, self.HEIGHT_SCREEN)
        self.title = 'אליעזר ילד שהוא גזר'
        return GameLayout()


class GameLayout(BoxLayout):
    score = NumericProperty(0.0)
    child_position_x = NumericProperty(0.0)
    child_position_y = NumericProperty(0.0)
    jump = False
    land = False
    IMAGE_SIZE = 200
    OBSTACLE_SIZE = 80
    HEIGHT_LEAP_OBS = 70
    STARTING_POINT_X = 30
    STARTING_POINT_Y =30
    DT_JUMP = 10
    HEIGHT_JUMP = 200
    DELTA_TIME = 0.01

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.obstacle = None

        self.child_position_x = self.STARTING_POINT_X
        self.child_position_y = self.STARTING_POINT_Y
        Clock.schedule_interval(self.update, self.DELTA_TIME)


    def update(self, dt):
        if self.jump and self.child_position_y >= self.HEIGHT_JUMP:
            self.jump = False
            self.land = True
        elif self.jump and self.child_position_y <= self.HEIGHT_JUMP:
            self.child_position_y +=self.DT_JUMP
        elif self.land and self.child_position_y >= self.STARTING_POINT_Y:
            self.child_position_y -= self.DT_JUMP
        elif self.land and self.child_position_y <= self.STARTING_POINT_Y:
            self.jump = False
            self.land = False
            self.child_position_y = self.STARTING_POINT_Y

        self.score += 0.01
        if self.obstacle is None:
            with self.canvas:
                # self.obstacle = Ellipse(pos = (self.width-OBSTACLE_SIZE, HEIGHT_LEAP_OBS), size=(OBSTACLE_SIZE,OBSTACLE_SIZE), color = (1,1,1,1))
                self.obstacle = Image(source = "images/carrot.png", pos = (self.width-self.OBSTACLE_SIZE, self.HEIGHT_LEAP_OBS), size=(self.OBSTACLE_SIZE,self.OBSTACLE_SIZE))
        else :
            x,y = self.obstacle.pos
            event = EventDispatcher()
            if x < (self.child_position_x+(2/3* self.IMAGE_SIZE)):
                self.obstacle.pos = (self.width-self.OBSTACLE_SIZE, y)
            else:
                self.obstacle.pos = (x-10,y)

    def button_clicked(self):
        print("boy need to jump")
        self.jump = True

def eli_game():
    AwesomeApp().run()


if __name__ == '__main__':
    eli_game()

