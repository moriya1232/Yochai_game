from kivy.core.window import Window
from kivy.app import App
from kivy.graphics.vertex_instructions import Ellipse
from kivy.properties import Clock, NumericProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.widget import Widget
from kivy.lang import Builder
import keyboard




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
    DT_JUMP = 3
    HEIGHT_JUMP = 300
    DELTA_TIME = 0.01
    SPEED_INCREASE_SCORE = 0.01
    SPEED_OBSTACLE = 6

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.obstacle = None

        self.child_position_x = self.STARTING_POINT_X
        self.child_position_y = self.STARTING_POINT_Y
        Clock.schedule_interval(self.update, self.DELTA_TIME)


    def update(self, dt):
        try:  # used try so that if user pressed other than the given key error will not be shown
            if keyboard.is_pressed(keyboard.KEY_UP):
                self.button_clicked()
                print('You Pressed up Key!')
        except:
            print("ERROR on press up key")

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

        self.score += self.SPEED_INCREASE_SCORE
        if self.obstacle is None:
            with self.canvas:
                # self.obstacle = Ellipse(pos = (self.width-OBSTACLE_SIZE, HEIGHT_LEAP_OBS), size=(OBSTACLE_SIZE,OBSTACLE_SIZE), color = (1,1,1,1))
                self.obstacle = Image(source = "images/carrot.png", pos = (self.width-self.OBSTACLE_SIZE, self.HEIGHT_LEAP_OBS), size=(self.OBSTACLE_SIZE,self.OBSTACLE_SIZE))
        else :
            x,y = self.obstacle.pos
            if x < 0:
                self.obstacle.pos = (self.width - self.OBSTACLE_SIZE, y)
            elif x < (self.child_position_x+(2/3* self.IMAGE_SIZE)):
                # success jumping
                if y < self.child_position_y:
                    self.obstacle.pos = (x - self.SPEED_OBSTACLE, y)
                else:
                    #TODO: need finish game
                    self.score -= 10
                    self.obstacle.pos = (self.width-self.OBSTACLE_SIZE, y)
            else:
                self.obstacle.pos = (x-self.SPEED_OBSTACLE,y)

    def button_clicked(self):
        print("boy need to jump")
        self.jump = True

def eli_game():
    AwesomeApp().run()


if __name__ == '__main__':
    eli_game()

