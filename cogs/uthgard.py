import json
import urllib.request
import urllib.error
from discord.ext import commands


class uthgard:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def uthgard(self, switch, *name):
        name = " ".join(name)
        if name == "" and switch != "status":
            name = switch
            switch = "player"

        if switch == "player":
            url = "https://www2.uthgard.net/herald/api/player/{0}".format(name)
        elif switch == "status":
            url = "https://www2.uthgard.net/api/serverstatus"
        else:
            url = "Error in switch"

        try:
            uthUrl = urllib.request.urlopen(url)
        except urllib.error.HTTPError as e:
            if e.code == 404:
                output = "Error looking up character {}. Check yo spellin".format(name)
                await self.bot.say(output)
                return
            else:
                output = "Uknown Error. Is Uthgard website online? "
                await self.bot.say(output)
                return

        mybytes = uthUrl.read()
        urlstring = mybytes.decode("utf8")
        uthUrl.close()

        if switch == "player":
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
        elif switch == "status":
            json_data = json.loads(urlstring)
            status = json_data['Status']
            players = json_data['Players']

            output = "\n Server is currently {} \nThere are {} people playing".format(status, players)
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
