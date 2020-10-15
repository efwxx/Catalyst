from discord.ext import commands
import discord
from datetime import datetime as d
from .embed import colours


class Basic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Define a new command
    @commands.command(
        name='ping', description='The ping command!\n')
    async def ping_command(self, ctx):
        start = d.timestamp(d.now())
        # Gets the timestamp when the command was used

        msg = await ctx.send(content='Pinging')
        # Sends a message to the user in the channel the message with the command was received.
        # Notifies the user that pinging has started

        await msg.edit(
            content=
            f'Pong!\nOne message round-trip took {round((d.timestamp(d.now())-start) * 1000, 2)}ms.'
        )
        # Ping completed and round-trip duration show in ms
        # Since it takes a while to send the messages, it will calculate how much time it takes to edit an message.
        # It depends usually on your internet connection speed

        return
    
    @commands.command(name="invite", description="Sends an invite to the bot.")
    async def invite_command(self, ctx):
        # YA
        embed = discord.Embed(
            title = "Invite Catalyst!",
            description="""**About Catalyst**
Catalyst is a Discord bot made with love for every community, our goal is for Catalyst to fit into almost every community here on Discord. The bot was developed by AlphaZero, ElectroSonic, RealistikDash and Vultra using Phyton.

**Invite the Discord bot to your own server(s) using this link provided below:**
https://bit.ly/30dc0Es""",
            colour=colours["BLUE"]
        )
        embed.set_thumbnail(url = self.bot.user.avatar_url)
        embed.set_footer(icon_url =ctx.author.avatar_url, text=f"Requested by {ctx.author.name}")
        await ctx.send(embed = embed)
#the code for some reason doesnt have bot defined
  #  @commands.command(
  #      name='say [text]',
  #      description='The say command\n',
  #      usage='<text>')
  #  async def say_command(self, ctx):
        # The 'usage' only needs to show the parameters
        # As the rest of the format is generated automatically

        # Lets see what the parameters are: -
        # The self is just a regular reference to the class
        # ctx - is the Context related to the command
        # For more reference - https://discordpy.readthedocs.io/en/rewrite/ext/commands/api.html#context

        # Next we get the message with the command in it.
  #      msg = ctx.message.content

        # Extracting the text sent by the user
        # ctx.invoked_with gives the alias used
        # ctx.prefix gives the prefix used while invoking the command
#        prefix_used = ctx.prefix
#        alias_used = ctx.invoked_with
#        text = msg[len(prefix_used) + len(alias_used):]

        # Next, we check if the user actually passed some text
#        if text == '':
#            # User didn't specify the text
#
#            await ctx.send(content='You need to specify the text!')

#            pass
#        else:
#            # User specified the text.
#
#            await ctx.send(content=f'{text}')

#            pass

#        return



def setup(bot):
    bot.add_cog(Basic(bot))
    # Adds the Basic commands to the bot
    # Note: The "setup" function has to be there in every cog file
