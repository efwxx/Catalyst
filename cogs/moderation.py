import discord
from discord.ext import commands

# This prevents staff members from being punished 
class Sinner(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets a member object
        permission = argument.guild_permissions.manage_messages # can change into any permission
        if not permission: # checks if user has the permission
            return argument # returns user object
        else:
            raise commands.BadArgument("You cannot punish other staff members") # tells user that target is a staff member

# Checks if you have a muted role
class Redeemed(commands.Converter):
    async def convert(self, ctx, argument):
        argument = await commands.MemberConverter().convert(ctx, argument) # gets member object
        muted = discord.utils.get(ctx.guild.roles, name="Muted") # gets role object
        if muted in argument.roles: # checks if user has muted role
            return argument # returns member object if there is muted role
        else:
            raise commands.BadArgument("The user was not muted.") # self-explainatory
            
# Checks if there is a muted role on the server and creates one if there isn't
async def mute(ctx, user, reason):
    role = discord.utils.get(ctx.guild.roles, name="Muted") # retrieves muted role returns none if there isn't 
    hell = discord.utils.get(ctx.guild.text_channels, name="muted") # retrieves channel named hell returns none if there isn't
    if not role: # checks if there is muted role
        try: # creates muted role 
            muted = await ctx.guild.create_role(name="Muted", reason="To use for muting")
            for channel in ctx.guild.channels: # removes permission to view and send in the channels 
                await channel.set_permissions(muted, send_messages=False,
                                              read_message_history=False,
                                              read_messages=False)
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make a muted role") # self-explainatory
        await user.add_roles(muted) # adds newly created muted role
        await ctx.send(f"{user.mention} has been muted for {reason}")
    else:
        await user.add_roles(role) # adds already existing muted role
        await ctx.send(f"{user.mention} has been sent to hell for {reason}")
       
    if not muted: # checks if there is a channel named hell
        overwrites = {ctx.guild.default_role: discord.PermissionOverwrite(read_message_history=False),
                      ctx.guild.me: discord.PermissionOverwrite(send_messages=True),
                      muted: discord.PermissionOverwrite(read_message_history=True)} # permissions for the channel
        try: # creates the channel and sends a message
            channel = await ctx.create_channel('muted', overwrites=overwrites)
            await channel.send("You have been muted. You will spend your time here until you get unmuted. Enjoy the silence.")
        except discord.Forbidden:
            return await ctx.send("I have no permissions to make #muted")
            
            
class Moderation(commands.Cog):
    """Commands used to moderate your guild"""
    
    def __init__(self, bot):
        self.bot = bot
    
    async def __error(self, ctx, error):
        if isinstance(error, commands.BadArgument):
            await ctx.send(error)
            
    @commands.command(name='ban', description='bans member from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: Sinner=None, reason=None):
        """Bans a member from the server."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to ban user
            await ctx.guild.ban(user)
            await ctx.send(f"{user.mention} was banned for: {reason}.")
        except discord.Forbidden:
            return await ctx.send("Are you trying to ban someone higher than the bot")

    @commands.command(name='softban', description='Temporarily bans User')
    async def softban(self, ctx, user: Sinner=None, reason=None):
        """Temporarily restricts access to the server."""
        
        if not user: # checks if there is a user
            return await ctx.send("You must specify a user")
        
        try: # Tries to soft-ban user
            await ctx.guild.ban(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
            await ctx.guild.unban(user, "Temporarily Banned")
        except discord.Forbidden:
            return await ctx.send("Are you trying to soft-ban someone higher than the bot?")
    
    @commands.command(name='mute', description='Mutes User')
    async def mute(self, ctx, user: Sinner, reason=None):
        """Mutes User."""
        await mute(ctx, user, reason) # uses the mute function
    
    @commands.command(name='kick', description='Kicks a user')
    async def kick(self, ctx, user: Sinner=None, reason=None):
        if not user: # checks if there is a user 
            return await ctx.send("You must specify a user")
        
        try: # tries to kick user
            await ctx.guild.kick(user, f"By {ctx.author} for {reason}" or f"By {ctx.author} for None Specified") 
        except discord.Forbidden:
            return await ctx.send("Are you trying to kick someone higher than the bot?")

    @commands.command(name='purge', description='bulk deletes messages in a channel')
    async def purge(self, ctx, limit: int):
        """Bulk deletes messages"""
        
        await ctx.purge(limit=limit + 1) # also deletes your own message
        await ctx.send(f"Bulk deleted `{limit}` messages") 
    
    @commands.command(name='unmute', description='Unmutes a member', aliases=[''])
    async def unmute(self, ctx, user: Redeemed):
        """Unmutes a muted user"""
        await user.remove_roles(discord.utils.get(ctx.guild.roles, name="Muted")) # removes muted role
        await ctx.send(f"{user.mention} has been unmuted")

    @commands.command(name='block', description='Prevents a User from chatting in a specific channel.')
    async def block(self, ctx, user: Sinner=None):
        """
        Blocks a user from chatting in current channel.
           
        Similar to mute but instead of restricting access
        to all channels it restricts in current channel.
        """
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
                                
        await ctx.set_permissions(user, send_messages=False) # sets permissions for current channel
    
    @commands.command(name='unblock', description='unblocks a user from chatting in a specific channel')
    async def unblock(self, ctx, user: Sinner=None):
        """Unblocks a user from current channel"""
                                
        if not user: # checks if there is user
            return await ctx.send("You must specify a user")
        
        await ctx.set_permissions(user, send_messages=True) # gives back send messages permissions

@commands.command(name='slowmode', description='limits the amount of messages sent in a specific timeframe')
async def slowmode(ctx, seconds: int):
    await ctx.channel.edit(slowmode_delay=seconds)
    await ctx.send(
        f"Set the slowmode delay in this channel to {seconds} seconds!")                  
                                
def setup(bot):
    bot.add_cog(Moderation(bot))