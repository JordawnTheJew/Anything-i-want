from tkinter.messagebox import YES
from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
from perlin_noise import PerlinNoise


  #keybinds 
def input(key):
    
    if key == "escape":
        quit()
    if key == 'left mouse down':
        place()
    elif key == 'right mouse down':
        e = mouse.hovered_entity
        destroy(e)


MC = Ursina()




#Window Settings
#window.fullscreen = True
window.exit_button = True
window.color = color.black
window.make_editor_gui
scene.fog_density = .005
scene.fog_color = color.green
SkyBox = Sky()

#Preload Textures
grass = load_texture('dirt')
wood = load_texture('stoneBlock')




#Objects
grass = Entity(model='cube', texture = 'dirt', Collider = True)
pic = Entity(model='cube', texture= "stoneBlock", Collider = True)



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
    p = duplicate (pic)
    p = collider = 'cube'

        

#Ground or Floor
Ground = Entity(model = None, collider = None)
GroundDepth = PerlinNoise (octaves=3.5,seed=216)

Groundx = 32 #Ground Width

#Ground modifiers
MaxX = 9
    
     #World height
Variation = 48

for g in range(Groundx*Groundx):
    grass = Entity(model='cube', texture = 'dirt')
    grass.x = floor(g/Groundx)
    grass.z = floor(g%Groundx)
    grass.y = floor((GroundDepth([grass.x/Variation,grass.z/Variation]))*MaxX) #Ground depth to add immersion, x and z are devided by int in Variation, and multiplied by MaxX
    grass.parent = Ground   #Added the ground as a parent class just in case i want to use the grass block later without messing up the floor





#Ground collision
Ground.combine(auto_destroy = False)
Ground.collider = 'mesh'
Ground.texture = 'dirt'

#update loop to check builder y position in order to determine if builder can jump on a block
def update():
    Blockcollision=False

    if Blockcollision==True:
        # With Delta time it will always update on the same intervals regardless of users fps
        Builder.y = lerp(Builder.y, target, 5 * time.dt) 
        #Builder towards ground
    else:
         Blockcollision-= 8 * time.dt

    #update objects
    pickaxe()


        
        
            

MC.run()
