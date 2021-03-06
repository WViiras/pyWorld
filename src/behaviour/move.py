import pygame

import physics
from components import component
from core.world import World
from .routine import Routine


class Move(Routine):

    def __init__(self, entity_id, world: World):
        super().__init__(entity_id, world)
        self.target: physics.Point = None

    def reset(self):
        pass

    def act(self):
        if not self.target:
            self.fail()
        entity_components = self._world.ec_manager.get_entity_components(self.entity_id)
        position = entity_components[component.Position]
        velocity = entity_components[component.Velocity]
        boundary = entity_components[component.Boundary]

        self._world.log_line(self.entity_id,
                             "target_position",
                             pygame.color.THECOLORS['orange'],
                             position.point.as_int_tuple(),
                             self.target.as_int_tuple())

        vector_to_target = position.point.to_vector2(self.target)

        self.log(f"distance_to:{self.target}", int(vector_to_target.magnitude))

        if vector_to_target.magnitude < boundary.radius:
            self.succeed()
            return

        velocity.vector = vector_to_target
