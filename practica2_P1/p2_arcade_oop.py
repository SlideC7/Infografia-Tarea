import arcade
from p2_arcade_flower import draw_flower
import random


SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flor bajo la Lluvia"

class Hola(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
        arcade.set_background_color(arcade.color.WHITE)

    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_rectangle_filled(
            SCREEN_WIDTH / 2,  
            SCREEN_HEIGHT / 4, 
            20,  
            300,
            arcade.color.GREEN_YELLOW  
        )
        for i in range(100):
            x = random.randint(0, SCREEN_WIDTH)
            y = random.randint(0, SCREEN_HEIGHT)
            color = arcade.color.BLUE  
            arcade.draw_ellipse_filled(x, y, 10, 10, color)
        draw_flower()

       
        


if __name__ == "__main__":
    app = Hola()
    arcade.run() 
