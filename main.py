import tkinter as tk
from PIL import Image, ImageTk
from itertools import count, cycle
# from kivy.app import App
# from kivy.uix.widget import Widget
# from kivy.lang import Builder

width_height_image = 150
width_left_screen = 500
speed_run = 50
#
# Builder.load_file("animation.kv")
#
# class AwesomeApp(App):
#     def build(self):
#         return MyLayout()
#
# class MyLayout(Widget):
#     pass

class ImageLabel(tk.Label):
    """
    A Label that displays images, and plays them if they are gifs
    :im: A PIL Image instance or a string filename
    """

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        frames = []

        try:
            for i in count(1):
                global width_height_image
                frames.append(ImageTk.PhotoImage(im.copy().resize((width_height_image,width_height_image))))
                im.seek(i)
        except EOFError:
            pass
        self.frames = cycle(frames)

        # try:
        #     self.delay = im.info['duration']
        # except:
        self.delay = int(1000/speed_run)

        if len(frames) == 1:
            self.config(image=next(self.frames))
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.config(image=next(self.frames))
            self.after(self.delay, self.next_frame)

# def jump(root, image_label):
    # image_label.place_configure(rely = 0)
    # root.after(1000, land, image_label)

# def land(image_label):
    # image_label.place_configure(rely =0)


def eli_game(name):
    global width_left_screen
    global width_height_image

    root = tk.Tk()
    root.title(name)
    canvas = tk.Canvas(width=width_left_screen, height=width_height_image + 100)
    canvas.grid(row=0, column=0)
    lbl = ImageLabel(root)
    lbl.grid(row = 0, column = 0, sticky = 'ws')
    lbl.load('boy.gif')
    root.mainloop()

    # AwesomeApp().run()


if __name__ == '__main__':
    eli_game('אליעזר ילד שהוא גזר')

