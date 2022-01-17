import random

from kivy.core.window import Window
from kivy.app import App
from kivy.graphics.context_instructions import Color
from kivy.graphics.vertex_instructions import Ellipse, Rectangle
from kivy.properties import Clock, NumericProperty, ObjectProperty
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.widget import Widget
from kivy.lang import Builder
import keyboard
from pynput.keyboard import Key, Listener




Builder.load_file("menu.kv")
Builder.load_file("animation.kv")


class AwesomeApp(App):
    WIDTH_SCREEN = 1000
    HEIGHT_SCREEN = 500
    #global Window

    def build(self):
        # Window.clearcolor = (127/256, 233/256, 131/256, 0.2)

        Window.size = (self.WIDTH_SCREEN, self.HEIGHT_SCREEN)
        self.title = 'אליעזר ילד שהוא גזר'
        return GameLayout()


class GameLayout(RelativeLayout):
    IMAGE_SIZE = 200
    HEIGHT_LEAP_OBS_BEGIN = 70
    OBSTACLE_SIZE = 100
    STARTING_POINT_X = 30
    STARTING_POINT_Y = 30
    DT_JUMP = 3
    HEIGHT_JUMP = 300
    DELTA_TIME = 0.01
    SPEED_INCREASE_SCORE = 0.01
    SPEED_OBSTACLE = 6

    menu_widget = ObjectProperty()
    score = NumericProperty(0.0)
    child_position_x = NumericProperty(0.0)
    child_position_y = NumericProperty(0.0)
    jump = False
    land = False
    game_started = False
    height_leap_obs_up = HEIGHT_LEAP_OBS_BEGIN
    height_leap_obs_down = HEIGHT_LEAP_OBS_BEGIN
    level = 0



    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.obstacle = None
        # print("width: " + str(self.width))
        # print("height: " + str(self.height))

        self.child_position_x = self.STARTING_POINT_X
        self.child_position_y = self.STARTING_POINT_Y
        with self.canvas.before:
            Color(127 / 256, 233 / 256, 131 / 256, 1)
            Rectangle(pos = (0,0), size = (AwesomeApp.WIDTH_SCREEN, self.STARTING_POINT_Y))

        Clock.schedule_interval(self.update, self.DELTA_TIME)

    def update(self, dt):
        if self.game_started:
            try:  # used try so that if user pressed other than the given key error will not be shown
                if keyboard.is_pressed(' '):
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
            self.level = int(self.score)
            if self.level < 0:
                self.level = 0
            elif self.level > 0:
                self.height_leap_obs_down = self.HEIGHT_LEAP_OBS_BEGIN - self.level
                if self.height_leap_obs_down < 0:
                    self.height_leap_obs_down = 0
                self.height_leap_obs_up = self.HEIGHT_LEAP_OBS_BEGIN + self.level
                if self.height_leap_obs_up > self.height:
                    self.height_leap_obs_up = self.height
            if self.obstacle is None:
                with self.canvas:
                    # self.obstacle = Ellipse(pos = (self.width-OBSTACLE_SIZE, HEIGHT_LEAP_OBS), size=(OBSTACLE_SIZE,OBSTACLE_SIZE), color = (1,1,1,1))
                    height_leap = random.randint(self.height_leap_obs_down, self.height_leap_obs_up)
                    self.obstacle = Image(source = "images/carrot.png", pos = (self.width-self.OBSTACLE_SIZE, height_leap), size=(self.OBSTACLE_SIZE,self.OBSTACLE_SIZE))
            else :
                x,y = self.obstacle.pos
                if x < 0:
                    height_leap = random.randint(self.height_leap_obs_down, self.height_leap_obs_up)
                    self.obstacle.pos = (self.width - self.OBSTACLE_SIZE, height_leap)
                elif x < (self.child_position_x+(2/3* self.IMAGE_SIZE)):
                    # success jumping
                    if y < self.child_position_y:
                        self.obstacle.pos = (x - self.SPEED_OBSTACLE, y)
                    else:
                        #TODO: need finish game
                        self.score -= 10
                        height_leap = random.randint(self.height_leap_obs_down, self.height_leap_obs_up)
                        self.obstacle.pos = (self.width-self.OBSTACLE_SIZE, height_leap)
                else:
                    self.obstacle.pos = (x-self.SPEED_OBSTACLE,y)
    def on_menu_button_pressed(self):
        print("ihhh")
        self.game_started = True
        self.menu_widget.opacity = 0

    def button_clicked(self):
        print("boy need to jump")
        self.jump = True

def eli_game():
    AwesomeApp().run()


if __name__ == '__main__':
    eli_game()

