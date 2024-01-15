from datetime import datetime, timedelta
import discord
import requests
import termcolor
from discord import app_commands
from discord.ext import commands
from utilities.helper import Helper


class Schedule(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        super().__init__()

    @staticmethod
    def get_embed(class_name) -> discord.Embed:
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
            f"https://api.stuv.app/rapla/lectures/events/{class_name}",
            headers=headers,
        )
        data = response.json()["lectures"]
        if len(data) == 0:
            # class not found
            Helper.colored_text(text="Class not found...", color="red")
            embed = discord.Embed(title=f"Schedule {day}", color=0x38B6F1)
            embed.add_field(name="Class Name", value=class_name, inline=False)
            embed.add_field(name="Info", value=f"Unknown class!")
            embed.set_footer(text="made by luis | TINF23A")
            return embed
        schedule = {}
        for lecture in data:
            try:
                date = lecture["date"]

                date = datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(
                    hours=timedelta_add
                )

                # Format the datetime object to a string representing the date in 'day-month-year' format
                day_string = date.strftime("%d-%m-%Y")

                schedule.setdefault(day_string, []).append(lecture)

            except Exception as e:
                print("error:", e)

        if day in schedule.keys():
            data = schedule[day]
            embed = discord.Embed(title=f"Schedule {day}", color=0x38B6F1)
            embed.add_field(name="Class Name", value=class_name, inline=False)
            i = 1
            for lesson in data:
                try:
                    start_time = lesson["startTime"]
                    start_time = datetime.strptime(
                        start_time, "%Y-%m-%dT%H:%M:%S.000Z"
                    ) + timedelta(hours=timedelta_add)
                    start_time = int(start_time.timestamp())
                    start_time = f"<t:{start_time}:R>"
                except:
                    start_time = ""
                try:
                    end_time = lesson["endTime"]
                    end_time = datetime.strptime(
                        end_time, "%Y-%m-%dT%H:%M:%S.000Z"
                    ) + timedelta(hours=timedelta_add)
                    end_time = int(end_time.timestamp())
                    end_time = f"<t:{end_time}:R>"
                except:
                    end_time = ""
                rooms = "\n".join(lesson["rooms"])
                name = lesson["name"]
                type = lesson["type"]
                dozent = lesson["lecturer"]
                embed.add_field(
                    name=f"{i}. {name}",
                    value=f"**Start:** {start_time}\n**Ende:** {end_time}\n**Dozent:** {dozent}\n**Typ:** {type}\n**Raum:** \n{rooms}",
                    inline=False,
                )
                i += 1
            embed.set_footer(text="made by luis | TINF23A")

        else:
            # day is weekend etc
            Helper.colored_text(text="Day not found...", color="red")
            embed = discord.Embed(title=f"Schedule {day}", color=0x38B6F1)
            embed.add_field(name="Class Name", value=class_name, inline=False)
            embed.add_field(
                name="Info", value=f"No schedule found for the current day!"
            )
            embed.set_footer(text="made by luis | TINF23A")

        return embed

    @app_commands.command(
        name="schedule", description="Returns the schedule of the current day"
    )
    @app_commands.describe(class_name="Enter the class name")
    async def my_cmd_srvy(self, interaction: discord.Interaction, class_name: str):
        Helper.colored_text(text=__name__, color="white")

        embed = Schedule.get_embed(class_name=class_name)
        # get data from api

        await interaction.response.send_message(embed=embed)


async def setup(bot: commands.Bot) -> None:
    """
    Async Function for adding this command to the bot

    :param bot: the current discord bot
    :type bot: commands.Bot
    """

    await bot.add_cog(Schedule(bot))
