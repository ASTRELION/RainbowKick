# Rainbow Bot
Discord bot for the [**Tabletop Gaymers** discord server](https://tabletopgaymers.org/discord/).

Kicks users without a role after 30 minutes and some additional functionality.

## Installation & Running
1. Create a discord bot application via the [developer portal](https://discordapp.com/developers/applications/).
2. Clone the repository
3. [Install Python3](https://www.python.org/)
4. [Install discord.py](https://discordpy.readthedocs.io/en/latest/intro.html)
5. [Create & configure config.json](#configuration)
6. Run the bot with `python3 main.py`

### Configuration
*An example configuration file can be found [here](config.json.example).*

`token`: place your bot token from the [developer portal](https://discordapp.com/developers/applications/) here. **DO NOT SHARE** this with anyone.

`prefix`: command prefix to invoke the bot.

`welcome_channel_id`: the ID of the welcome channel for the server.

`system_channel_id`: the ID of the system channel for the server. Kick notifications will be sent here. Defaults to the system channel set in Server Settings > Overview > System Messages Channel.

`member_role_id`: the role to look for when determining to kick a user. Users without this role will be eligible to be kicked.

## Usage

### Command List
*Parameters in `<`, `>` are required, parameters in `[`, `]` are optional*

`enable [time]`  
Enable the bot for a given time in minutes, or indefinitely if empty.

`disable [time]`  
Disable the bot for a given time in minutes, or indefinitely if empty.

`kick <user>`  
Kick the given user from the server.

`set kickmsg <message>`
Set the message to be sent in the system channel when a user is kicked. Use %USER% to reference the user's name.

`set system [channel]`  
Set the system channel to the given channel, or the current channel if left empty.

`set welcome [channel]`  
Set the welcome channel to the given channel, or the current channel if left empty.

`set timeout <time>`  
Set the time it takes to kick a user after joining in minutes.

`set role <role>`  
Set the role to look for when determining to kick a user. Users with this role are effectively immune to being kicked by the bot.

`reset kickmsg`  
Reset the kickmsg to "%USER% has been kicked from the server."

`reset system`  
Reset system channel to the server system channel.

`reset welcome`  
Reset welcome channel to default.

`reset timeout`  
Reset timeout time to 30 minutes.

`reset role`  
Reset role to the server @everyone role, effectively disabling the bot.

`reset all`  
Reset all configuration to default values.

## Bugs
Report any bugs to ASTRELION#4600