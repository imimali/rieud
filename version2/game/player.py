'''
    created on 05 April 2019
    
    @author: Gergely
'''
import math

from pyglet.window import key

from version2.game import physicalobject, resources


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.thrust = 500.0
        self.rotate_speed = 200.0
        self.keys = dict(left=False, right=False, up=False, down=False)

    def on_key_press(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = True
        elif symbol == key.LEFT:
            self.keys['left'] = True
        elif symbol == key.RIGHT:
            self.keys['right'] = True
        elif symbol == key.DOWN:
            self.keys['down'] = True
        elif symbol == key.SPACE:
            print("secret key pressed")
            self.velocity_x = 0
            self.velocity_y = 0

    def on_key_release(self, symbol, modifiers):
        if symbol == key.UP:
            self.keys['up'] = False
        elif symbol == key.LEFT:
            self.keys['left'] = False
        elif symbol == key.RIGHT:
            self.keys['right'] = False
        elif symbol == key.DOWN:
            self.keys['down'] = False

    def update(self, dt):
        super(Player, self).update(dt)

        if self.keys['left']:
            self.rotation -= self.rotate_speed * dt
        if self.keys['right']:
            self.rotation += self.rotate_speed * dt

        if self.keys['up']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y

        if self.keys['down']:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x -= force_x
            self.velocity_y -= force_y
