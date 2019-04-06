'''
    created on 05 April 2019
    
    @author: Gergely
'''
import random

import pyglet

from version3.game import physicalobject, asteroid
from version3.game.util import distance
from . import resources


def asteroids(num_asteroids, player_position, batch=None):
    asts = []
    for i in range(num_asteroids):
        asteroid_x, asteroid_y = player_position
        while distance((asteroid_x, asteroid_y), player_position) < 100:
            asteroid_x = random.randint(0, 800)
            asteroid_y = random.randint(0, 600)
        new_asteroid = asteroid.Asteroid(
            img=resources.asteroid_image, x=asteroid_x, y=asteroid_y, batch=batch)
        new_asteroid.rotation = random.randint(0, 360)
        new_asteroid.velocity_x = random.random() * 40
        new_asteroid.velocity_y = random.random() * 40
        asts.append(new_asteroid)
    return asts


def player_lives(num_icons, batch=None):
    lives = []
    for i in range(num_icons):
        new_sprite = pyglet.sprite.Sprite(img=resources.player_image,
                                          x=785 - i * 30, y=585, batch=batch)
        new_sprite.scale = 0.5
        lives.append(new_sprite)
    return lives
