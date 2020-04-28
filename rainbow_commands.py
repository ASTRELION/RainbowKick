import discord
from discord.ext import commands
import typing

class Rainbow_Commands(commands.Cog, name = "Rainbow Commands"):
    """General commands"""

    def __init__(self, client):

        super().__init__()
        self.client = client


    @commands.command("ping")
    async def ping(self, ctx):

        latency = self.client.latency
        await ctx.send("Pong! *{}ms*".format(round(latency * 1000)))


    @commands.command("kick")
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.User, *, reason: typing.Optional[str] = None):
        """Kick a user from the server"""
        guild = ctx.guild
        await guild.kick(user, reason = reason)


    @commands.group("set")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def setCmd(self, ctx):

        if (not ctx.invoked_subcommand):
            await ctx.send("`set` requires a subcommand.")


    @setCmd.command("kickmsg")
    async def kickmsg(self, ctx, *, message: str):

        self.client.write_config(data = {
            "kick_msg": message
        })

    
    @setCmd.command("system")
    async def system(self, ctx, channel: typing.Optional[discord.TextChannel] = None):

        if (not channel):
            channel = ctx.guild.system_channel

        self.client.write_config(data = {
            "system_channel": channel.id
        })


    @setCmd.command("welcome")
    async def welcome(self, ctx, channel: typing.Optional[discord.TextChannel] = None):

        if (not channel):
            channel = ctx.guild.system_channel

        self.client.write_config(data = {
            "welcome_channel": channel.id
        })


    @setCmd.command("timeout")
    async def timeout(self, ctx, timeout: int):

        self.client.write_config(data = {
            "timeout": timeout
        })


    @setCmd.command("role")
    async def role(self, ctx, role: discord.Role):

        self.client.write_config(data = {
            "role": role.id
        })


def setup(client):

    client.add_cog(Rainbow_Commands(client))