from datetime import datetime, timedelta
import discord
import requests
import termcolor
from discord import app_commands
from discord.ext import commands
from utilities.helper import Helper
from typing import Literal, Optional

city_dict = {"Mosbach": "MOS", "Bad Mergentheim": "MGH"}


class Classes(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @staticmethod
    def get_embed(location) -> discord.Embed:
        timedelta_add = 1
        # if it should be the schedule for the net day add: + timedelta(days=1)
        day = datetime.now()  # + timedelta(days=1)
        day = day.strftime("%d-%m-%Y")

        headers = {
            "authority": "api.stuv.app",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "cache-control": "max-age=0",
            "sec-ch-ua": '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "document",
            "sec-fetch-mode": "navigate",
            "sec-fetch-site": "none",
            "sec-fetch-user": "?1",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
        }
        s = requests.Session()

        # TINF23A
        response = s.get(
            f"https://api.stuv.app/rapla/courses",
            headers=headers,
        )

        classes = response.json()
        embed = discord.Embed(title=f"All classes", color=0x38B6F1)
        classes_str = ""
        i = 0
        for cls in classes:
            if location != None:
                # check if Mosbach or Bad Mergentheim
                if city_dict[location] in cls:
                    classes_str += f"{cls}\n"
                    i += 1
            else:
                classes_str += f"{cls}\n"
                i += 1

            if i == 50:
                embed.add_field(name="Classes", value=classes_str, inline=True)
                i = 0
                classes_str = ""
        if classes_str != "":
            embed.add_field(name="Classes", value=classes_str, inline=True)

        embed.set_footer(text="made by luis | TINF23A")

        return embed

    @app_commands.command(name="classes", description="Returns all classes")
    async def my_cmd_classes(
        self,
        interaction: discord.Interaction,
        location: Optional[Literal["Mosbach", "Bad Mergentheim"]],
    ):
        Helper.colored_text(text=__name__, color="white")

        embed = Classes.get_embed(location=location)
        # get data from api

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """
    Async Function for adding this command to the bot

    :param bot: the current discord bot
    :type bot: commands.Bot
    """

    await bot.add_cog(Classes(bot))
