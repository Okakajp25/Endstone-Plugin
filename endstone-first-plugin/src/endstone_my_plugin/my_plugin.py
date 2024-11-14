from endstone.plugin import Plugin

class MyPlugin(Plugin):
    api_version: "0.4"
    def on_load(self) -> None:
        self.logger.info("on_load")