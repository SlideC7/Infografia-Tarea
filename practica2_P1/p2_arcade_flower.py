import arcade
import math
import cmath

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Flor bajo la Lluvia"


def draw_flower():
    petal_number = 15
    final_angle = 360
    angle_step = final_angle // petal_number

    for angle in range(0, final_angle, angle_step):
        r = 70 
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        arcade.draw_circle_filled(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            30,
            arcade.color.YELLOW_ORANGE
        )
    for angle in range(0, final_angle, angle_step):
        r = 70 * 1.50
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        arcade.draw_circle_filled(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            30,
            arcade.color.YELLOW_ORANGE
        )

    for angle in range(0, final_angle, angle_step):
        r = 70 * 1.25
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        arcade.draw_circle_filled(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            15,
            arcade.color.YELLOW_ORANGE
        )
    for angle in range(0, final_angle, angle_step):
        r = 70 * 2
        phi = math.radians(angle)
        center_c = cmath.rect(r, phi)
        arcade.draw_circle_filled(
            int(center_c.real + SCREEN_WIDTH / 2),
            int(center_c.imag + SCREEN_HEIGHT / 2),
            30,
            arcade.color.YELLOW_ORANGE
        )
    arcade.draw_circle_filled(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, 50, arcade.color.YELLOW)


if __name__ == "__main__":

    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    arcade.set_background_color(arcade.color.WHITE)

    arcade.start_render()

    draw_flower()

    arcade.finish_render()

    arcade.run()
