from tkinter import Scale
from tkinter.messagebox import YES
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
scene.fog_color = color.salmon
SkyBox = Sky()

#Preload Textures
grass = load_texture('dirt')
stone = load_texture('stoneBlock')




#Objects
grass = Entity(model='cube', texture = 'dirt')
pic = Entity(model='cube', texture= "wiremesh", scale=(1,1,1))



#grass.color = color.green

#FP Char
Builder = FirstPersonController()
Builder.x = 5
Builder.y = 2

#FP Char modifiers
Builder.cursor.visible = True
Builder.gravity = .5
Builder.jump_height = 1
"Builder.fall_after"
Builder.jump_up_duration = .9
Builder.fade_in = True
Builder.speed = 5
camera.fade_in = True
camera.fov = 110
Builder.height= .5
FirstPersonController


def pickaxe():
    pic.position = round(Builder.position + camera.forward * 3)
    pic.y += 2
    pic.x = round(pic.x)
    pic.y = round(pic.y)
    pic.z = round(pic.z)
#Building
def place():
    p = duplicate(pic)
    p.texture = 'stoneBlock' 
    p.model = 'cube'
    p.collider = 'cube'

  #keybinds 
def input( key):
    
    if key == "escape":
        quit()
    if key == 'left mouse down':
        place()
    if key == 'right mouse down':
        e = mouse.hovered_entity
        destroy(e)

        

#Ground or Floor
Ground = Entity(model = None, collider = None)
GroundVariation = PerlinNoise (octaves=3.5,seed=216)

Groundx = 32 #Ground Width
Groundz = 8
#Ground modifiers
MaxX = 32
    
     #World height
Variation = 100

for g in range(Groundx*Groundx):
    grass = Entity(model='cube', texture = 'dirt')
    grass.x = floor(g/Groundx)
    grass.z = floor(g%Groundx)
    grass.y = floor((GroundVariation([grass.x/Variation,grass.z/Variation]))*MaxX) #Ground variation to add immersion, x and z are devided by int in Variation, and multiplied by MaxX
    grass.parent = Ground   #Added the ground as a parent class just in case i want to use the grass block later without messing up the floor
    grass.collider = 'mesh'




#Ground collision
#Ground.combine(auto_destroy = False) //Caused deletion of ground...
Ground.collider = None
Ground.texture = 'dirt'
Ground.model = 'cube'
#update loop to check builder y position in order to determine if builder can jump on a block
def update():
    Blockcollision=False

    if Blockcollision==True:
        # With Delta time it will always update on the same intervals regardless of users fps
        Builder.y = lerp(Builder.y, target_y, 1234* time.dt) 
        #Builder towards ground
    else:
         Blockcollision-= 8 * time.dt

    #update objects
    pickaxe()


        
        
            

MC.run()
