from datetime import datetime
from typing import Any, Optional, Type
import discord
import os
import ctypes
import asyncpg
import json
from discord.app_commands.tree import CommandTree
from discord.ext import commands
from discord.ext.commands.help import HelpCommand
from utilities.helper import Helper

# path to the token --> update path
token_path = "/Users/luiswagner/Desktop/DHBW - AINF/GitHub/bot_token.txt"
bot_token = open(token_path).read()
app_id = "1187008525457686639"


class Bot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix=".",
            intents=discord.Intents.default(),
            application_id=app_id,
            help_command=None,
        )

    async def on_ready(self) -> None:
        Helper.clear_console()
        Helper.colored_text(
            color="green", text=f"Successfully started bot with name: {self.user.name}"
        )

    async def setup_hook(self) -> None:
        cogs = ["cogs.schedule", "cogs.classes", "cogs.joke"]
        for cog in cogs:
            await self.load_extension(cog)
        await self.tree.sync()


def start_bot():
    bot = Bot()
    bot.run(bot_token)


start_bot()
