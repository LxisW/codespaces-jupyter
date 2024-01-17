from datetime import datetime, timedelta
import discord
import requests
import termcolor
from discord import app_commands
from discord.ext import commands
from utilities.helper import Helper
from typing import Literal, Optional

city_dict = {"Mosbach": "MOS", "Bad Mergentheim": "MGH"}


class Joke(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @staticmethod
    def get_embed() -> discord.Embed:
        headers = {
            "authority": "api.api-ninjas.com",
            "accept": "*/*",
            "accept-language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
            "origin": "https://api-ninjas.com",
            "referer": "https://api-ninjas.com/",
            "sec-ch-ua": '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": '"macOS"',
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-site",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
        }

        response = requests.get(
            "https://api.api-ninjas.com/v1/jokes?limit=1", headers=headers
        )

        joke = response.json()[0]["joke"]
        embed = discord.Embed(title=f"Joke", color=0x38B6F1, description=joke)

        embed.set_footer(text="made by luis | TINF23A")

        return embed

    @app_commands.command(name="joke", description="Tells a random joke")
    async def my_cmd_classes(
        self,
        interaction: discord.Interaction,
    ):
        Helper.colored_text(text=__name__, color="white")

        embed = Joke.get_embed()

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """
    Async Function for adding this command to the bot

    :param bot: the current discord bot
    :type bot: commands.Bot
    """

    await bot.add_cog(Joke(bot))
