'''
    created on 06 April 2019
    
    @author: Gergely
'''
import random

from version3.game import physicalobject, resources


class Asteroid(physicalobject.PhysicalObject):
    def __init__(self, *args, **kwargs):
        if kwargs is not None and 'img' in kwargs.keys():
            kwargs.pop('img')
        super(Asteroid, self).__init__(resources.asteroid_image, *args, **kwargs)
        self.rotate_speed = random.random() * 100.0 - 50.0

    def handle_collision_with(self, other_object):
        super(Asteroid, self).handle_collision_with(other_object)
        if self.dead and self.scale > 0.35:
            num_asteroids = random.randint(1, 2)
            for i in range(num_asteroids):
                new_asteroid = Asteroid(x=self.x, y=self.y, batch=self.batch)
                new_asteroid.rotation = random.randint(0, 360)
                new_asteroid.scale = self.scale * 0.8
                new_asteroid.velocity_x = (2 * self.velocity_x * (0.5 + random.random()) - self.velocity_x)
                new_asteroid.velocity_y = (2 * self.velocity_y * (0.5 + random.random()) - self.velocity_y)
                self.new_objects.append(new_asteroid)

    def update(self, dt):
        super(Asteroid, self).update(dt)
        self.rotation += self.rotate_speed * dt
