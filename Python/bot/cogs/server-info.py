import asyncio
import datetime
from utilities.helper import Helper
import discord
import termcolor
from discord import app_commands
from discord.ext import commands
from threading import Thread


class ServerInfo(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @app_commands.command(name="server-info", description="Get server info")
    async def my_cmd(self, interaction: discord.Interaction):
        await interaction.response.defer()
        Helper.colored_text(text=__name__, color="white")

        server = interaction.guild
        owner = server.owner_id
        owner = await self.bot.fetch_user(owner)

        embed = discord.Embed(
            title=f"Server Information - {server.name}",
            color=0x38B6F1,
        )
        try:
            embed.set_thumbnail(url=str(server.icon.url))
        except:
            pass
        embed.add_field(name="Owner", value=f"{owner.name}", inline=False)
        embed.add_field(name="Members", value=server.member_count)
        embed.add_field(name="Roles", value=len(server.roles))
        embed.add_field(name="\u200b", value="\u200b")

        embed.add_field(name="Text Channels", value=len(server.text_channels))
        embed.add_field(name="Voice Channels", value=len(server.voice_channels))
        embed.add_field(
            name="Created On",
            value=f"<t:{int(server.created_at.timestamp())}:R>",
            inline=False,
        )

        embed.add_field(
            name="Boosters", value=server.premium_subscription_count, inline=False
        )
        embed.set_footer(text="made by luis | TINF23A")

        await interaction.followup.send(embed=embed)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(ServerInfo(bot))
