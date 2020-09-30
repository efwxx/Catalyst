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
    },
    {
        "formal_name" : "Parry Gripp - Guinea Pig Bridge",
        "beatmap_id" : 2102292,
        "beatmapset_id" : 1004468,
        "allowed_names" : [
            "guinea pig bridge"
        ],
        "difficulty" : 1
    },
    {
        "formal_name" : "Golec uOrkiestra - Slodycze",
        "beatmap_id" : 1869633,
        "beatmapset_id" : 894714,
        "allowed_names" : [
            "slodycze",
            "słodycze"
        ],
        "difficulty" : 3
    },
    {
        "formal_name" : "Ayaka Ohashi - Wagamama MIRROR HEART",
        "beatmap_id" : 1174467,
        "beatmapset_id" : 554626,
        "allowed_names" : [
            "mirror heart",
            "wagamama mirror heart"
        ],
        "difficulty" : 2
    },
    {
        "formal_name" : "Elmo and Cookie Monster - Cookie-Butter-Choco-Cookie",
        "beatmap_id" : 1373950,
        "beatmapset_id" : 542081,
        "allowed_names" : [
            "cookie butter choco cookie",
            "cbcc",
            "cookie-butter-choco-cookie"
        ],
        "difficulty" : 1
    },
    {
        "formal_name" : "S3RL - Bass Slut (Original Mix)",
        "beatmap_id" : 2118443,
        "beatmapset_id" : 983911,
        "allowed_names" : [
            "bass slut"
        ],
        "difficulty" : 1
    },
    {
        "formal_name" : "toby fox - Last Goodbye",
        "beatmap_id" : 1955170,
        "beatmapset_id" : 744772,
        "allowed_names" : [
            "last goodbye"
        ],
        "difficulty" : 1
    },
    {
        "formal_name" : "ryu5150 - Louder than steel",
        "beatmap_id" : 1808605,
        "beatmapset_id" : 864869,
        "allowed_names" : [
            "louder than steel"
        ],
        "difficulty" : 2
    },
    {
        "formal_name" : "Will Stetson - Harumachi Clover (Swing Arrangement)",
        "beatmap_id" : 1797548,
        "beatmapset_id" : 859783,
        "allowed_names" : [
            "harumachi clover",
            "harumachi clover swing arrangement",
            "harumachi clover (swing arrangement)"
        ],
        "difficulty" : 1
    },
    {
        "formal_name" : "DragonForce - Symphony of the Night",
        "beatmap_id" : 985141,
        "beatmapset_id" : 459901,
        "allowed_names" : [
            "symphony of the night"
        ],
        "difficulty" : 2
    },
    {
        "formal_name" : "KASAI HARCORES - Cycle Hit",
        "beatmap_id" : 1351114,
        "beatmapset_id" : 636839,
        "allowed_names" : [
            "cycle hit"
        ],
        "difficulty" : 2
    }
]

class OsuCog(commands.Cog):
    """osu! Good game!!!"""
    def __init__(self, bot):
        self.bot = bot
    
    @commands.command(name='maptrivia', description='an osu! map minigame')
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
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.message.author.avatar_url)
        embed.set_image(url = f"https://assets.ppy.sh/beatmaps/{curr_map['beatmapset_id']}/covers/cover.jpg")
        await ctx.send(embed=embed)

        msg = await self.bot.wait_for('message', check=check)
        if msg.content.lower() in curr_map["allowed_names"]:
            embed = discord.Embed(title=f"[Correct!] {curr_map['formal_name']}", colour=colours["GREEN"], url=f"https://ussr.pl/b/{curr_map['beatmap_id']}")
            embed.set_image(url = f"https://assets.ppy.sh/beatmaps/{curr_map['beatmapset_id']}/covers/cover.jpg")
            embed.set_footer(text=f"Guessed correctly by {ctx.author}", icon_url=ctx.message.author.avatar_url)
            await ctx.send(embed=embed)
        else:
            await ctx.send("Incorrect, shame on you!")

def setup(bot):
    bot.add_cog(OsuCog(bot))
