'''
    created on 05 April 2019
    
    @author: Gergely
'''
import pyglet
pyglet.resource.path = ['../resources']
player_image = pyglet.resource.image("alienblaster.png")
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")
asteroid_image.width = 50
asteroid_image.height = 50
bullet_image.width = 10
bullet_image.height = 10