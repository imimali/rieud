'''
    created on 05 April 2019
    
    @author: Gergely
'''
import pyglet

from version3.game import resources, load, player

game_window = pyglet.window.Window(800, 600)
main_batch = pyglet.graphics.Batch()
score_label = pyglet.text.Label(text="Score: 0", x=10, y=575, batch=main_batch)
level_label = pyglet.text.Label(text="My Amazing Game",
                                x=400, y=575, anchor_x='center', batch=main_batch)

player_ship = player.Player(img=resources.player_image, x=400, y=300, batch=main_batch)

asteroids = load.asteroids(53, player_ship.position, batch=main_batch)

player_lives = load.player_lives(3, batch=main_batch)

game_objects = [player_ship] + asteroids


def update(dt):
    for obj in game_objects:
        obj.update(dt)


@game_window.event
def on_draw():
    game_window.clear()
    main_batch.draw()


@game_window.event
def on_mouse_press(x, y, button, modifiers):
    print('mouse button was pressed at {} {}'.format(x, y))


if __name__ == '__main__':
    game_window.push_handlers(player_ship)
    pyglet.clock.schedule_interval(update, 1 / 120.0)
    pyglet.app.run()
