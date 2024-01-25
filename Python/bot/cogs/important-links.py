import asyncio
import datetime
from utilities.helper import Helper
import discord
import termcolor
from discord import app_commands
from discord.ext import commands
from threading import Thread


class ImportantLinks(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(
        name="important-links", description="Get important links for university"
    )
    async def important_links(self, interaction: discord.Interaction):
        await interaction.response.defer()
        Helper.colored_text(text=__name__, color="white")
        embed = discord.Embed(
            title=f"Important Links for University",
            color=0x38B6F1,
            description=f"[**E-Mail**](https://webmail.lehre.mosbach.dhbw.de/)\n[**Moodle**](https://moodle.mosbach.dhbw.de/my/courses.php)",
        )
        try:
            embed.set_thumbnail(
                url="https://upload.wikimedia.org/wikipedia/de/thumb/1/1d/DHBW-Logo.svg/1200px-DHBW-Logo.svg.png"
            )
        except:
            pass

        embed.set_footer(text="made by luis | TINF23A")

        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ImportantLinks(bot))
