from endstone.plugin import Plugin
from endstone.event import event_handler, PlayerJoinEvent
from endstone import ColorFormat

class MyPlugin(Plugin):
    api_version: "0.4"
    def on_load(self) -> None:
        self.logger.info("on_load")
    def on_player_join(self, event: PlayerJoinEvent):
        player = event.player
        self.logger.info(
            ColorFormat.YELLOW + f"{player.name}/[{player.address}:{player.port}] joined the game with UUID {player.unique_id}"
        )