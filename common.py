import discord

def error_embed(ctx, error) -> discord.Embed:
    """A simple error embed."""
    embed = discord.Embed(
        title = "There was an error in your command!",
        description=error,
        colour=0xeb4034
    )
    embed.set_footer(
        text=f'Requested by {ctx.message.author.name}',
        icon_url=ctx.author.avatar_url
    )
    return embed
