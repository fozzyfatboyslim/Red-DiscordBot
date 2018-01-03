import json
import urllib.request
import discord
from discord.ext import commands


class uthgard:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uthgard(self, switch, *name):
        name = " ".join(name)
        switch = "player"
        url = "https://www2.uthgard.net/herald/api/{0}/{1}"\
            .format(switch, name)
        uthUrl = urllib.request.urlopen(url)
        mybytes = uthUrl.read()
        urlstring = mybytes.decode("utf8")
        uthUrl.close()

        json_data = json.loads(urlstring)
        guild = json_data['Guild']
        race = json_data['Race']
        prof = json_data['Class']
        level = json_data['Level']
        preSplitRR = str(json_data['RealmRank'])
        rr = preSplitRR[0] + "L" + preSplitRR[1]

        output = "\n  {0} the {1} {2} \nA member of {3} \nLevel: {4}  RR: {5}"\
            .format(name.capitalize(), race, prof, guild, level, rr)

        await self.bot.say(output)


def setup(bot):
    bot.add_cog(uthgard(bot))


# if keywords:
#             keywords = "+".join(keywords)
#         else:
#             await self.bot.send_cmd_help(ctx)
#             return
#
#         url = ("http://api.giphy.com/v1/gifs/search?&api_key={}&q={}"
#                "".format(GIPHY_API_KEY
