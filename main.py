import discord
from discord.ext import tasks, commands
import json

class RainbowClient(commands.AutoShardedBot):
    """Rainbow client Auto Sharded Bot wrapper"""

    def __init__(self):

        self.config = self.read_config()
        #self.remove_command("help")

        super().__init__(
            command_prefix = self.config["prefix"]
        )


    def read_config(self):

        try:
            with open("config.json") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print("Configuration file not found. Please create config.json.")


# Run client
client = RainbowClient()
client.run(client.config["token"])