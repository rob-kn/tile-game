import configuration as conf
from time import time

sprites = {}


class Sprite:
    def __init__(self, sprite_id, starting_x, starting_y):
        self.sprite_id = sprite_id
        self.offset = (0, 0)
        self.offset_float = (0.0, 0.0)
        self.x = starting_x
        self.y = starting_y
        self.attack = 0
        self.attack_speed = 10
        self.range = 0
        self.target = None
        self.last_attack_time = time()
        self.map_level = 0
        sprites[self.sprite_id] = self

    def attack_sprite(self, target_sprite_id):
        target_to_remove = None
        current_time = time()
        print(current_time, self.last_attack_time, self.attack_speed)
        if current_time - self.last_attack_time > self.attack_speed:
            for x_change in range(-1, self.range + 1):
                for y_change in range(-1, self.range + 1):
                    if (self.x + x_change == sprites[target_sprite_id].x) and \
                            (self.y + y_change == sprites[target_sprite_id].y):
                        print(sprites[target_sprite_id].health)
                        sprites[target_sprite_id].health -= self.attack
                        if sprites[target_sprite_id].health <= 0:
                            self.target = None
                            target_to_remove = target_sprite_id
            self.last_attack_time = time()
        return target_to_remove

    def reset_offset(self, new_grid_pos, old_grid_pos):
        """Sets the appropriate offset when given an updated position in the grid."""
        new_offset_x = 0
        new_offset_y = 0
        new_offset_x = -conf.GRID_SQUARE_SIZE if new_grid_pos[0] < old_grid_pos[0] else new_offset_x
        new_offset_x = +conf.GRID_SQUARE_SIZE if new_grid_pos[0] > old_grid_pos[0] else new_offset_x
        new_offset_y = -conf.GRID_SQUARE_SIZE if new_grid_pos[1] < old_grid_pos[1] else new_offset_y
        new_offset_y = +conf.GRID_SQUARE_SIZE if new_grid_pos[1] > old_grid_pos[1] else new_offset_y
        self.offset = (new_offset_x, new_offset_y)
        self.offset_float = (float(new_offset_x), float(new_offset_y))

    def reduce_offset(self):
        """
        Converges current offset to zero. Updates a float version to allow for varying speeds.
        If the movement is diagonal, the player moves twice as slow.
        """
        current_offset_x, current_offset_y = self.offset_float
        if -self.speed < current_offset_x < self.speed and -self.speed < current_offset_y < self.speed:
            current_offset_x, current_offset_y = 0.0, 0.0
        change_x, change_y = 0.0, 0.0
        if current_offset_x > 0:
            change_x -= self.speed
        elif current_offset_x < 0:
            change_x += self.speed
        if current_offset_y > 0:
            change_y -= self.speed
        elif current_offset_y < 0:
            change_y += self.speed
        if change_x and change_y:
            change_x /= 2
            change_y /= 2
        self.offset = (int(current_offset_x + change_x), int(current_offset_y + change_y))
        self.offset_float = (current_offset_x + change_x, current_offset_y + change_y)
