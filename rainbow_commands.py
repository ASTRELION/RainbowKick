import discord
from discord.ext import commands
import typing

class Rainbow_Commands(commands.Cog, name = "Rainbow Commands"):
    """General commands"""

    def __init__(self, client):

        super().__init__()
        self.client = client


    @commands.command("kick")
    @commands.guild_only()
    @commands.bot_has_permissions(kick_members = True)
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.User, *, reason: typing.Optional[str] = None):
        """Kick a user from the server"""
        guild = ctx.guild
        await guild.kick(user, reason = reason)


    @commands.command("setsystem")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def set_system(self, ctx, channel: typing.Optional[discord.TextChannel] = None):
        """Set the system channel to display messages in"""
        if (not channel):
            channel = ctx.guild.system_channel
            

    @commands.command("setwelcome")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def set_welcome(self, ctx, channel: typing.Optional[discord.TextChannel] = None):
        """Set the server welcome channel"""
        

    @commands.command("settimeout")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def set_timeout(self, ctx, timeout: typing.Optional[int] = None):
        """Set the time it takes in minutes before kicking an inactive user"""


    @commands.command("setrole")
    @commands.guild_only()
    @commands.has_permissions(administrator = True)
    async def set_member_role(self, ctx, member_role: typing.Optional[discord.Role] = None):
        """Set the role to look for"""



def setup(client):

    client.add_cog(Rainbow_Commands(client))