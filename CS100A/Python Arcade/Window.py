"""
Jump man
"""
from tkinter import Y
import arcade
from zmq import PROTOCOL_ERROR_ZMTP_MALFORMED_COMMAND_MESSAGE


# Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Jump man concept 0.0.1"

#Scaling of sprites for window

CharacterScale=1
TileScaling=0.5

class MyGame(arcade.Window):
    # Main application class.

    def __init__(self):

        #Call Parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        #Lists to keep track of sprits that will go into.
        self.wall_list = None
        self.player = None

        #variable for player sprite
        self.player_sprite = None
        

        arcade.set_background_color(arcade.csscolor.DARK_SALMON)

    def setup(self):
        # Settingup the game here. Will call this function to restart the game.
        #Creating the sprite list
        self.player_list = arcade.SpriteList()
        self.wall_list = arcade.SpriteList(use_spatial_hash=True)

        #setting the player up and their postiton at specific coords
        image_source = ":resources:images/animated_characters/male_adventurer/maleAdventurer_idle.png"
        self.player_sprite = arcade.Sprite(image_source, CharacterScale)
        self.player_sprite.center_x = 64
        self.player_sprite.center_y = 128
        self.player_list.append(self.player_sprite)


        #Creating the ground, using a loop to place the sprites horizontally
        for x in range(0, 1250, 64):
            wall = arcade.Sprite (":resources:images/tiles/grassMid.png", TileScaling)
            wall.center_x = x
            wall.center_y = 32
            self.wall_list.append(wall)

        #Crates at these Cords
        coordiante_list= [[512, 96], [256, 96], [768, 96]]


        for coordinate in coordiante_list:
            wall = arcade.Sprite(
                 ":resources:images/tiles/boxCrate_double.png", TileScaling
            )

            wall.position = coordinate
            self.wall_list.append(wall)


    def on_draw(self):
        #this will render the screen
        self.clear()
        # code to draw the screen will go here

        #draw our sprites
        self.wall_list.draw()
        self.player_list.draw()

def main ():
    # main function
    window = MyGame()
    window.setup()
    arcade.run()

if __name__ == "__main__":
    main()
            
        