'''
    created on 05 April 2019
    
    @author: Gergely
'''
import math

from pyglet.window import key

from version3.game import physicalobject, resources, bullet


class Player(physicalobject.PhysicalObject):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.thrust = 500.0
        self.rotate_speed = 200.0
        self.keys = dict(left=False, right=False, up=False, down=False)
        self.key_handler = key.KeyStateHandler()
        del kwargs['img']  # daaamn
        self.engine_sprite = physicalobject.PhysicalObject(img=resources.engine_image, *args, **kwargs)
        self.engine_sprite.visible = False
        self.bullet_speed = 700.0
        self.is_bullet = False
        self.reacts_to_bullets = False

    def update(self, dt):
        super(Player, self).update(dt)
        if not self.key_handler[key.UP]:
            self.engine_sprite.visible = False

        if self.key_handler[key.LEFT]:
            self.engine_sprite.visible = False
            self.rotation -= self.rotate_speed * dt
        if self.key_handler[key.RIGHT]:
            self.engine_sprite.visible = False
            self.rotation += self.rotate_speed * dt

        if self.key_handler[key.UP]:
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x += force_x
            self.velocity_y += force_y
            self.velocity_x = min(self.velocity_x, 150)
            self.velocity_y = min(self.velocity_y, 150)
            self.engine_sprite.rotation = self.rotation
            self.engine_sprite.x = self.x
            self.engine_sprite.y = self.y

            self.engine_sprite.visible = True

        if self.key_handler[key.DOWN]:
            self.engine_sprite.visible = False
            angle_radians = -math.radians(self.rotation)
            force_x = math.cos(angle_radians) * self.thrust * dt
            force_y = math.sin(angle_radians) * self.thrust * dt
            self.velocity_x -= force_x
            self.velocity_y -= force_y

        if self.key_handler[key.ENTER]:
            self.engine_sprite.visible = False
            self.velocity_y = 0
            self.velocity_x = 0
        if self.key_handler[key.SPACE]:
            self.fire()

    def delete(self):
        self.engine_sprite.delete()
        super(Player, self).delete()

    def fire(self):
        angle_radians = -math.radians(self.rotation)
        ship_radius = self.image.width / 2
        bullet_x = self.x + math.cos(angle_radians) * ship_radius
        bullet_y = self.y + math.sin(angle_radians) * ship_radius
        new_bullet = bullet.Bullet(bullet_x, bullet_y, batch=self.batch)
        bullet_vx = (self.velocity_x + math.cos(angle_radians) * self.bullet_speed)
        bullet_vy = (self.velocity_y + math.sin(angle_radians) * self.bullet_speed)
        new_bullet.velocity_x = bullet_vx
        new_bullet.velocity_y = bullet_vy
        self.new_objects.append(new_bullet)
