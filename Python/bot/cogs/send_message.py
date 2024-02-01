from datetime import datetime, timedelta
import discord
import requests
import termcolor
from discord import app_commands
from discord.ext import commands
from utilities.helper import Helper
from typing import Literal, Optional


class SendMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.describe(
        title="The title of the embed",
        fields="Embed fields seperated by ';' (name(string), value(string): str, inline(bool))",
    )
    @app_commands.command(
        name="send-message", description="Sends a message embed in a specific channel"
    )
    async def my_cmd_classes(
        self,
        interaction: discord.Interaction,
        channel: discord.TextChannel,
        title: str,
        fields: str,
    ):
        Helper.colored_text(text=__name__, color="white")

        embed = discord.Embed(title=title)
        data = fields.split(";")
        for embed_data in data:
            try:
                temp_data = embed_data.split(",")
                name = temp_data[0]
                value = temp_data[1]
                inline = temp_data[2]
                if inline.lower() == "true":
                    inline = True
                else:
                    inline = False
                embed.add_field(name=name, value=value, inline=inline)
            except:
                pass

        embed.set_footer(text="made by luis | TINF23A")
        await channel.send(embed=embed)

        await interaction.response.send_message(
            content=f"Successfully sent embed in https://discord.com/channels/{interaction.guild.id}/{channel.id}",
            ephemeral=True,
        )


async def setup(bot: commands.Bot) -> None:
    """
    Async Function for adding this command to the bot

    :param bot: the current discord bot
    :type bot: commands.Bot
    """

    await bot.add_cog(SendMessage(bot))
