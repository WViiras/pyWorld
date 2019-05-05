import components
from world import World
from .system import System


class Movement(System):
    def __init__(self, world: World):
        required = {
            components.Position,
            components.Velocity
        }
        super().__init__(world, required)

    def update_entity(self, entity_id, entity_components):
        position: components.Position = entity_components[components.Position]
        velocity: components.Velocity = entity_components[components.Velocity]

        new_x, new_y = position[0] + velocity[0], position[1] + velocity[1]
        new_vx, new_vy = velocity[0], velocity[1]

        max_x, max_y = self.world.surface.get_size()

        if new_x > max_x:
            new_x = max_x
            new_vx = -new_vx
        elif new_x < 0:
            new_x = 0
            new_vx = -new_vx

        if new_y > max_y:
            new_y = max_y
            new_vy = -new_vy
        elif new_y < 0:
            new_y = 0
            new_vy = -new_vy

        position.set_position((new_x, new_y))
        velocity.set_velocity((new_vx, new_vy))