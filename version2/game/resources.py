'''
    created on 05 April 2019
    
    @author: Gergely
'''
import pyglet


def center_image(image):
    """Sets an image's anchor point to its center"""
    image.anchor_x = image.width // 2
    image.anchor_y = image.height // 2


pyglet.resource.path = ['../resources']
player_image = pyglet.resource.image("alienblaster.png",rotate=270)
bullet_image = pyglet.resource.image("bullet.png")
asteroid_image = pyglet.resource.image("asteroid.png")
asteroid_image.width = 35
asteroid_image.height = 35

player_image.width = 50
player_image.height = 50
bullet_image.width = 10
bullet_image.height = 10

center_image(player_image)
center_image(bullet_image)
center_image(asteroid_image)
