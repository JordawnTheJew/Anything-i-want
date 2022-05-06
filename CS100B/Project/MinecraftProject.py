from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise

MC = Ursina()

#Window Settings
#window.fullscreen = True
window.exit_button = True
window.color = color.black
window.make_editor_gui
scene.fog_density = .005
scene.fog_color 
SkyBox = Sky()
def input(key):
    if key == "escape":
        quit()


#Preload Textures
grass = load_texture('dirt')

#Objects
grass = Entity(model='cube', texture = 'dirt')
#grass.color = color.green

#FP Char
Builder = FirstPersonController()
Builder.x = 5
Builder.y = 2

#FP Char modifiers
Builder.cursor.visible = False
Builder.gravity = .5
Builder.jump_height = 1
#Builder.fall_after 
Builder.jump_up_duration = .9
Builder.fade_in = True
Builder.speed = 5
camera.fade_in = True
camera.fov = 110
Builder.height= .5
FirstPersonController

#Ground or Floor
Ground = Entity(model = None, collider = None)
GroundDepth = PerlinNoise (octaves=3.5,seed=216)

Groundx = 32 #Ground Width

#Ground modifiers
MaxX = 16 #World hight
Variation = 48

for g in range(Groundx*Groundx):
    grass = Entity(model='cube', texture = 'dirt')
    grass.x = floor(g/Groundx)
    grass.z = floor(g%Groundx)
    grass.y = floor((GroundDepth([grass.x/Variation,grass.z/Variation]))*MaxX) #Ground depth to add immersion, x and z are devided by int in Variation, and multiplied by MaxX
    grass.parent = Ground   #Added the ground as a parent class just in case i want to use the grass block later without messing up the floor

Ground.combine(auto_destroy = False)
Ground.collider = 'mesh'
Ground.texture = 'dirt'



MC.run()