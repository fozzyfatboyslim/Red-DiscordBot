import json
import urllib.request
import bisect
from discord.ext import commands


class daoc:

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def daoc(self, switch, *name):
        levels = [
                    '1L1',
                    '1L2',
                    '1L3',
                    '1L4',
                    '1L5',
                    '1L6',
                    '1L7',
                    '1L8',
                    '1L9',
                    '2L0',
                    '2L1',
                    '2L2',
                    '2L3',
                    '2L4',
                    '2L5',
                    '2L6',
                    '2L7',
                    '2L8',
                    '2L9',
                    '3L0',
                    '3L1',
                    '3L2',
                    '3L3',
                    '3L4',
                    '3L5',
                    '3L6',
                    '3L7',
                    '3L8',
                    '3L9',
                    '4L0',
                    '4L1',
                    '4L2',
                    '4L3',
                    '4L4',
                    '4L5',
                    '4L6',
                    '4L7',
                    '4L8',
                    '4L9',
                    '5L0',
                    '5L1',
                    '5L2',
                    '5L3',
                    '5L4',
                    '5L5',
                    '5L6',
                    '5L7',
                    '5L8',
                    '5L9',
                    '6L0',
                    '6L1',
                    '6L2',
                    '6L3',
                    '6L4',
                    '6L5',
                    '6L6',
                    '6L7',
                    '6L8',
                    '6L9',
                    '7L0',
                    '7L1',
                    '7L2',
                    '7L3',
                    '7L4',
                    '7L5',
                    '7L6',
                    '7L7',
                    '7L8',
                    '7L9',
                    '8L0',
                    '8L1',
                    '8L2',
                    '8L3',
                    '8L4',
                    '8L5',
                    '8L6',
                    '8L7',
                    '8L8',
                    '8L9',
                    '9L0',
                    '9L1',
                    '9L2',
                    '9L3',
                    '9L4',
                    '9L5',
                    '9L6',
                    '9L7',
                    '9L8',
                    '9L9',
                    '10L0',
                    '10L1',
                    '10L2',
                    '10L3',
                    '10L4',
                    '10L5',
                    '10L6',
                    '10L7',
                    '10L8',
                    '10L9',
                    '11L0',
                    '11L1',
                    '11L2',
                    '11L3',
                    '11L4',
                    '11L5',
                    '11L6',
                    '11L7',
                    '11L8',
                    '11L9',
                    '12L0',
                    '12L1',
                    '12L2',
                    '12L3',
                    '12L4',
                    '12L5',
                    '12L6',
                    '12L7',
                    '12L8',
                    '12L9',
                    '13L0',
                    '13L1',
                    '13L2',
                    '13L3',
                    '13L4',
                    '13L5',
                    '13L6',
                    '13L7',
                    '13L8',
                    '13L9',
                    '14L0'
                    ]
        realm_points = [
                    0,
                    25,
                    125,
                    350,
                    750,
                    1375,
                    2275,
                    3500,
                    5100,
                    7125,
                    9625,
                    12650,
                    16250,
                    20475,
                    25375,
                    31000,
                    37400,
                    44625,
                    52725,
                    61750,
                    71750,
                    82775,
                    94875,
                    108100,
                    122500,
                    138125,
                    155025,
                    173250,
                    192850,
                    213875,
                    236375,
                    260400,
                    286000,
                    313225,
                    342125,
                    372750,
                    405150,
                    439375,
                    475475,
                    513500,
                    553500,
                    595525,
                    639625,
                    685850,
                    734250,
                    784875,
                    837775,
                    893000,
                    950600,
                    1010625,
                    1073125,
                    1138150,
                    1205750,
                    1275975,
                    1348875,
                    1424500,
                    1502900,
                    1584125,
                    1668225,
                    1755250,
                    1845250,
                    1938275,
                    2034375,
                    2133600,
                    2236000,
                    2341625,
                    2450525,
                    2562750,
                    2678350,
                    2797375,
                    2919875,
                    3045900,
                    3175500,
                    3308725,
                    3445625,
                    3586250,
                    3730650,
                    3878875,
                    4030975,
                    4187000,
                    4347000,
                    4511025,
                    4679125,
                    4851350,
                    5027750,
                    5208375,
                    5393275,
                    5582500,
                    5776100,
                    5974125,
                    6176625,
                    6383650,
                    6595250,
                    6811475,
                    7032375,
                    7258000,
                    7488400,
                    7723625,
                    7963725,
                    8208750,
                    9111713,
                    10114001,
                    11226541,
                    12461460,
                    13832221,
                    15353765,
                    17042680,
                    18917374,
                    20998286,
                    23308097,
                    25871988,
                    28717906,
                    31876876,
                    35383333,
                    39275499,
                    43595804,
                    48391343,
                    53714390,
                    59622973,
                    66181501,
                    73461466,
                    81542227,
                    90511872,
                    100468178,
                    111519678,
                    123786843,
                    137403395,
                    152517769,
                    169294723,
                    187917143
                    ]

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

        if name != json_data['results'][0]['name'] and name != full_name[0]:
            output2 = "Characters found: "
            for x in range(len(json_data['results'])):
                output2 = output2 + json_data['results'][x]['name'] + " "

            output = "Exact match not found, {} matches found".format(len(json_data['results']))
            await self.bot.say(output)
            await self.bot.say(output2)
        else:
            if 'guild_info' in json_data['results'][0]:
                guild = "A member of " + json_data['results'][0]['guild_info']['guild_name']
            else:
                guild = "Not a member of any guild"
            name = json_data['results'][0]['name']
            race = json_data['results'][0]['race']
            # server = json_data['results'][0]['server_name']
            class_name = json_data['results'][0]['class_name']
            level = json_data['results'][0]['level']
            rp = json_data['results'][0]['realm_points']
            rl = bisect.bisect_left(realm_points, rp)

            output = "\n{} the {} {} \n{} \nLevel: {}\
              RP: {}".format(name.title(), race, class_name, guild, level, levels[rl])
            await self.bot.say(output)


def setup(bot):
    bot.add_cog(daoc(bot))
