# Rainbow Bot
Discord bot for the [**Tabletop Gaymers** discord server](https://tabletopgaymers.org/discord/).

Kicks users without a role after 30 minutes and some additional functionality.

## Installation & Running
1. Clone the repository
2. [Install Python3](https://www.python.org/)
3. [Install discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)
4. [Create & configure config.json](#configuration)
5. Run the bot with `python3 main.py`

### Configuration
*An example configuration file can be found [here](config.json.example)*

`token`: place your bot token from the [developer portal](https://discordapp.com/developers/applications/) here.

`prefix`: command prefix to invoke the bot.

`welcome_channel_id`: the ID of the welcome channel for the server.

`system_channel_id`: the ID of the system channel for the server

`member_role_id`: the role to look for when determining to kick a user

## Usage

### Command List
`kick <user>`  
kick a user from the server

## Bugs
Report any bugs to ASTRELION#4600