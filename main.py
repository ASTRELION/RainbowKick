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

        self.load_extension("rainbow_commands")


    def read_config(self):
        """Read config.json to Python object"""
        try:
            with open("config.json") as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print("Configuration file not found. Please create config.json.")

    def write_config(self, data):
        
        for key in data:
            self.config[key] = data[key]

        """Write data to config.json file"""
        with open("config.json", "w", encoding = "utf-8") as json_file:
            json.dump(self.config, json_file, indent = 4)


# Run client
client = RainbowClient()
client.run(client.config["token"])