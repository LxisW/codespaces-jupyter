import requests
import time
import pytz
from datetime import datetime, timedelta
from discord_webhook import DiscordEmbed, DiscordWebhook
import schedule
from colorama import init, Fore
import re


# timedelta for fixing timezones
timedelta_add = 1

# initalizes the colored text
init()


# available colors
color_dict = {
    "red": Fore.RED,
    "green": Fore.GREEN,
    "blue": Fore.BLUE,
    "yellow": Fore.YELLOW,
    "magenta": Fore.MAGENTA,
    "cyan": Fore.CYAN,
    "white": Fore.WHITE,
    "orange": "\033[38;2;255;165;0m",  # RGB for orange
    "reset": Fore.RESET
}

# colored output


def output(text, color) -> None:

    selected_color = color_dict.get(color.lower(), Fore.RESET)

    # Print the colored text
    print(
        f"{selected_color}[{datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {text}{Fore.RESET}")

# colored input


def colored_input(prompt, color):
    selected_color = color_dict.get(color.lower(), Fore.RESET)
    return input(f"{selected_color}{prompt}{Fore.RESET}")


def get_schedule():
    # Sends the schedule of the current day via discord webhook
    wehook_url = "https://discord.com/api/webhooks/1183777158695489577/av34T0DTKaxfXr41IEiMWgmgNH-xJOeiNVpY6YSTx0m1k_PG5TNVqzCTtFXxx2zpzXuU"

    headers = {
        'authority': 'api.stuv.app',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'cache-control': 'max-age=0',
        'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"macOS"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'none',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    }
    s = requests.Session()
    response = s.get(
        'https://api.stuv.app/rapla/lectures/events/MOS-TINF23A',  headers=headers)

    data = response.json()["lectures"]
    schedule = {}
    for lecture in data:
        try:
            day = lecture["date"]

            day = datetime.strptime(
                day, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=timedelta_add)

            # Format the datetime object to a string representing the date in 'day-month-year' format
            day_string = day.strftime('%d-%m-%Y')

            schedule.setdefault(day_string, []).append(
                lecture)

        except Exception as e:
            output(e, color="red")

    # if it should be the schedule for the net day add: + timedelta(days=1)
    day = datetime.now()
    day = day.strftime('%d-%m-%Y')
    if day in schedule.keys():
        data = schedule[day]
        webhook = DiscordWebhook(url=wehook_url, username="TINF 23-A")
        embed = DiscordEmbed(title=f"Schedule {day}", color="38b6f1")
        i = 1
        for lesson in data:
            try:
                start_time = lesson["startTime"]
                start_time = datetime.strptime(
                    start_time, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=timedelta_add)
                start_time = int(start_time.timestamp())
                start_time = f"<t:{start_time}:R>"
            except:
                start_time = ""
            try:
                end_time = lesson["endTime"]
                end_time = datetime.strptime(
                    end_time, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=timedelta_add)
                end_time = int(end_time.timestamp())
                end_time = f"<t:{end_time}:R>"
            except:
                end_time = ""
            rooms = "\n".join(lesson["rooms"])
            name = lesson["name"]
            type = lesson["type"]
            dozent = lesson["lecturer"]
            embed.add_embed_field(
                name=f"{i}. {name}", value=f"**Start:** {start_time}\n**Ende:** {end_time}\n**Dozent:** {dozent}\n**Typ:** {type}\n**Raum:** \n{rooms}", inline=False)
            i += 1
        embed.set_footer(text="made by luis | TINF23A")
        webhook.add_embed(embed)
        webhook.execute()
    else:
        output(text="Day not found...", color="red")

# checks the input


def get_valid_time_input(prompt):
    # checks the input with regex
    time_pattern = re.compile(r"^(?:[01]\d|2[0-3]):[0-5]\d$|^now$")

    while True:
        user_input = colored_input(prompt=prompt, color="cyan")
        if time_pattern.match(user_input.lower()):
            return user_input
        else:
            output(
                text="Invalid input. Please enter a time in HH:MM format or 'now'.", color="red")


start_time = get_valid_time_input(
    "Enter the time you want the daily webhook to be sent (in 24-hour format, e.g., 18:20), or type 'now' to send it immediately:\n"
)

if start_time == "now":
    output(text="Sending the webhook...", color="orange")
    get_schedule()
    output(text="Sent webhook...", color="green")

else:

    schedule.every().day.at(start_time).do(get_schedule)

    output(
        text=f"Sending schedule every day at {start_time}...", color="yellow")
    while True:
        schedule.run_pending()
        time.sleep(1)
