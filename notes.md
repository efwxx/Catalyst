# NOTES LIST

use this template for command names/description: (name='command name', description='command function', aliases=['alias here'])

add in a changelog command later on. progress on command so far (to be added into basic.py):
```
    @commands.command(name='Changelog', description='Shows the ChangeLog for every update')
    async def changelog(self,ctx):
      print 
```

not working command :<
import requests

@bot.command()
async def getname(ctx, member: discord.Member):

    await ctx.send(f'User name: {member.name}, id: {member.id}')

    with requests.get(member.avatar_url_as(format='png')) as r:
        img_data = r.content
    with open(f'{member.name}.png', 'wb') as f:
        f.write(img_data)