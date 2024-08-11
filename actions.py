from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from engine import Engine
    from entity import Entity

class Action:
    def perform(self, engine: Engine, entity: Entity):
        """Perform this action with the objects needed to determine its scope

        `engine` is the scope this action is being performed in.

        `entity` is the entity performing the action.

        This method must be overridden by the subclasses.
        """
        return NotImplementedError()


class EscapeAction(Action):
    def perform(self, engine: Engine, entity: Entity):
        raise SystemExit()


class MovementAction(Action):

    def __init__(self, dx, dy):
        super().__init__()
        self.dx = dx
        self.dy = dy

    def perform(self, engine: Engine, entity: Entity):
        dest_x = entity.x + self.dx
        dest_y = entity.y + self.dy

        if not engine.game_map.in_bounds(dest_x, dest_y):
            return  # Destination is outside map boundaries
        if not engine.game_map.tiles["walkable"][dest_x, dest_y]:
            return  # Destination tile is not walkable // Path is blocked

        entity.move(self.dx, self.dy)
