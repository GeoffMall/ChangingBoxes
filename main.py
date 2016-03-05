from kivy.app import App
from kivy.clock import Clock
from kivy.graphics import Color
from kivy.properties import NumericProperty, ReferenceListProperty
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget

from random import randint

class ChangingBackgroundColor(Widget):
    r = NumericProperty(.5)
    g = NumericProperty(.5)
    b = NumericProperty(.5)
    a = NumericProperty(1)
    color = ReferenceListProperty(r, g, b, a)

    dif = NumericProperty(.025)
    roun = NumericProperty(4)

    def __init__(self, **kwargs):
        super(ChangingBackgroundColor, self).__init__(**kwargs)
        Clock.schedule_interval(self.update, 1.0 / 60.0)

    def update(self, dt):

        position = randint(0, 2)  # change to randint(0,3) to change a as well
        direction = randint(0, 1)

        if direction == 0:
            if self.color[position] == 0:
                self.color[position] += self.dif
            else:
                self.color[position] -= self.dif
        elif direction == 1:
            if self.color[position] == 1:
                self.color[position] -= self.dif
            else:
                self.color[position] += self.dif

        self.color[position] = round(self.color[position], self.roun)
        self.canvas.add(Color(self.color))

class TeachingApp(App):

    def build(self):
        number_of_rows = 20
        grid = GridLayout(rows = number_of_rows)
        for i in range(number_of_rows):
            for j in range(number_of_rows):
                grid.add_widget(ChangingBackgroundColor())
        return grid

if __name__ == '__main__':
    TeachingApp().run()