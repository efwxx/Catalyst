import discord
import datetime
import time
import timeago

def error_embed(ctx, error) -> discord.Embed:
    """A simple error embed."""
    embed = discord.Embed(
        title = "There was an error in your command!",
        description=error,
        colour=0xeb4034
    )
    embed.set_footer(
        text=f'Invoked by {ctx.message.author.name}',
        icon_url=ctx.author.avatar_url
    )
    return embed

def datetime_to_timestamp(obj : datetime.datetime) -> int:
    """Converts a datetime object to a UNIX timestamp."""
    return time.mktime(obj.timetuple())

def timeago_from_now(object : datetime.datetime):
    """Returns a timeago string from now."""
    return timeago.format(object, datetime.datetime.now())
