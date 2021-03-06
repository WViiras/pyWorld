from components import component
from core import World
from systems import System


class Movement(System):
    def __init__(self, world: World):
        required_components = {
            component.Position,
            component.Velocity
        }
        super().__init__(world, required_components)

    def update_entity(self, entity_id, entity_components):
        position = entity_components[component.Position]
        velocity = entity_components[component.Velocity]

        speed_delta = self._world.delta_time * 0.15
        # speed_delta = 1
        self._world.log_text(entity_id, "speed_delta", speed_delta)
        new_x = position.x + (velocity.unit_vector.x * speed_delta)
        new_y = position.y + (velocity.unit_vector.y * speed_delta)

        max_x, max_y = self._world.surface.get_size()

        if new_x > max_x:
            new_x = max_x
        elif new_x < 0:
            new_x = 0

        if new_y > max_y:
            new_y = max_y
        elif new_y < 0:
            new_y = 0

        position.x, position.y = new_x, new_y

        self._world.log_text(entity_id, "position", position.point.int_str())
