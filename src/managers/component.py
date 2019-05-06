from typing import Type

import components
import mappers


class ComponentManager:
    def __init__(self):
        self._components = mappers.EntityComponentMap()

    def add_component_if_not_exist(self, entity_id, component_type: Type[components.C_T],
                                   *args,
                                   **kwargs) -> components.C_T:
        component = self.get_entity_components(entity_id)[component_type]
        if not component:
            component = self.add_component(entity_id, component_type, *args, **kwargs)
        return component

    def add_component(self, entity_id, component_type: Type[components.C_T], *args, **kwargs) -> components.C_T:
        component = component_type(*args, **kwargs)
        self._components[entity_id][component_type] = component
        return component

    def remove_component(self, entity_id, component_type: Type[components.Component]):
        del self._components[entity_id][component_type]

    def get_entity_components(self, entity_id) -> mappers.ComponentMap:
        return self._components[entity_id]
