import json
import urllib.request
import discord
from discord.ext import commands


class daoc:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daoc(self, switch, *name):
        try:
            name
        except NameError:
            name = switch
            switch = "player"
            
        name = " ".join(name)
        #http://api.camelotherald.com/character/search?name=frohyo&cluster=Ywain
        url = "http://api.camelotherald.com/character/search?name={}&cluster=Ywain".format(name)
        liveUrl = urllib.request.urlopen(url)
        mybytes = liveUrl.read()
        urlstring = mybytes.decode("utf8")
        liveUrl.close()

        json_data = json.loads(urlstring)
        # guild = json_data['results'][guild_info]

        guild = json_data['results'][0]['guild_info']['guild_name']
        name = json_data['results'][0]['name']
        race = json_data['results'][0]['race']
        server = json_data['results'][0]['server_name']
        class_name = json_data['results'][0]['class_name']
        level = json_data['results'][0]['level']
        rp = json_data['results'][0]['realm_points']

        output = "\n  {0} the {1} {2} \nA member of {3} \nLevel: {4}  RP: {5}".\
            format(name.capitalize(), race, class_name, guild, level, rp)
        await self.bot.say(output)


def setup(bot):
    bot.add_cog(daoc(bot))
