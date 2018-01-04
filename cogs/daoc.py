import json
import urllib.request
from discord.ext import commands


class daoc:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daoc(self, switch, *name):
        name = " ".join(name)
        if name == "":
            name = switch
            switch = "player"

        name = name.capitalize()
        url = "http://api.camelotherald.com/character/search?name={}&cluster=Ywain".format(name)
        liveUrl = urllib.request.urlopen(url)
        mybytes = liveUrl.read()
        urlstring = mybytes.decode("utf8")
        liveUrl.close()

        json_data = json.loads(urlstring)
        if not json_data['results']:
            output = "Unable to locate character. Check your spelling."
            await self.bot.say(output)
        else:
            full_name = json_data['results'][0]['name'].split(" ")

        if name != json_data['results'][0]['name'] or name != full_name[0]:
            output3 = "name is ..{}.. testing against  ..{}..".format(name, full_name[0])
            output2 = "Characters found: "
            for x in range(len(json_data['results'])):
                output2 = output2 + json_data['results'][x]['name'] + " "

            output = "Exact match not found, {} matches found".format(len(json_data['results']))
            await self.bot.say(output)
            await self.bot.say(output2)
            await self.bot.say(output3)
        else:
            guild = json_data['results'][0]['guild_info']['guild_name']
            name = json_data['results'][0]['name']
            race = json_data['results'][0]['race']
            # server = json_data['results'][0]['server_name']
            class_name = json_data['results'][0]['class_name']
            level = json_data['results'][0]['level']
            rp = json_data['results'][0]['realm_points']

            output = "\n{0} the {1} {2} \nA member of {3} \nLevel: {4}\
              RP: {5}".format(name.capitalize(), race, class_name, guild,
                              level, rp)
            await self.bot.say(output)


def setup(bot):
    bot.add_cog(daoc(bot))
