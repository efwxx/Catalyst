#from objects.funobjs import OsuMap
import discord
from discord.ext import commands
import random
from .embed import colours
# The constant things
OSU_QUESTIONS = [
    {
        "formal_name" : "Nashimoto Ui - AaAaAaAAaAaAAa",
        "beatmap_id" : 2129143,
        "beatmapset_id" : 1017271,
        "allowed_names" : [
            "aaaaaaaa",
            "aaaaaaaaaaaaaa"
        ],
        "difficulty" : 2
    },
    {
        "formal_name" : "Aitsuki Nakuru - Monochrome Butterfly",
        "beatmap_id" : 1619555,
        "beatmapset_id" : 770300,
        "allowed_names" : [
            "monochrome butterfly"
        ],
        "difficulty" : 1
    },
    {
        "formal_name" : "Nogizaka46 - Yubi Bouenkyou (TV Size)",
        "beatmap_id" : 2469345,
        "beatmapset_id" : 1178935,
        "allowed_names" : [
            "yubi bouenkyou",
            "yubi boukenyu",
            "anime ban"
        ],
        "difficulty" : 1
    }
]

class OsuCog(commands.Cog):
    """osu! Good game!!!"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name="maptrvivia")
    async def map_trivia_command(self, ctx):
        """osu! guess the beatmap!"""
        def check(ms): # Sorry electro i stole this from your cog lmfao
            # Look for the message sent in the same channel where the command was used
            # As well as by the user who used the command.
            return ms.channel == ctx.message.channel and ms.author == ctx.message.author
        curr_map = random.choice(OSU_QUESTIONS)
        # Making the embed for the beatmap.
        colour = {
            1 : colours["GREEN"],
            2 : colours["ORANGE"],
            3 : colours["RED"]
        }.get(curr_map["difficulty"])

        embed = discord.Embed(title="Guess this osu! map!", colour=colour)
        embed.set_footer(text="RealistikDash was here.")
        embed.set_image(url = f"https://assets.ppy.sh/beatmaps/{curr_map['beatmapset_id']}/covers/cover.jpg")
        await ctx.send(embed=embed)

        msg = await self.bot.wait_for('message', check=check)
        if msg.content.lower() in curr_map["allowed_names"]:
            await ctx.send("That's correct!")
        else:
            await ctx.send("Incorrect, shame on you!")

def setup(bot):
    bot.add_cog(OsuCog(bot))
