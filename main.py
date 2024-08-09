#!/usr/bin/env python3
import tcod

from typing import Tuple
from entity import Entity
from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
from engine import Engine

def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    event_handler = EventHandler()

    player = Entity(screen_width // 2, screen_height // 2, "@", (255, 255, 255))
    npc = Entity((screen_width // 2) - 5, screen_height // 2, "@", (255, 255, 0))
    entities = {player, npc}

    engine = Engine(entities=entities, event_handler=event_handler, player=player)

    with tcod.context.new_terminal(
        screen_width,
        screen_height,
        tileset=tileset,
        title="Yet another generic roguelike",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(screen_width, screen_height, order="F")
        while True:

            engine.render(console=root_console, context=context)
            events = tcod.event.wait()
            engine.handle_events(events)

if __name__ == '__main__':
    main()
