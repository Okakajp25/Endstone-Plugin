from endstone.plugin import Plugin
from endstone.event import event_handler, EventPriority, PlayerJoinEvent, PlayerQuitEvent, ServerListPingEvent
from endstone import ColorFormat

class MyPlugin(Plugin):
    api_version: "0."
    def on_load(self) -> None:
        self.logger.info("on_load")

    @event_handler(priority=EventPriority)
    def on_player_join(self, event: PlayerJoinEvent):
        player = event.player
        self.logger.info(
            ColorFormat.YELLOW + f"{player.name}/[{player.address}:{player.port}] joined the game with UUID {player.unique_id}"
        )

    @event_handler
    def on_player_quit(self, event: PlayerQuitEvent):
        player = event.player
        self._plugin.logger.info(ColorFormat.YELLOW + f"{player.name}[/{player.address}] left the game.")