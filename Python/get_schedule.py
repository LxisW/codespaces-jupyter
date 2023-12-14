import requests
import time
import pytz
from datetime import datetime, timedelta
from discord_webhook import DiscordEmbed, DiscordWebhook
import schedule

timedelta_add = 1


def get_schedule():
    # Sends the schedule of the current day via discord webhook
    wehook_url = "YOURWEBHOOKURL"

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

    # print(response.text)
    data = response.json()["lectures"]
    schedule = {}
    for lecture in data:
        try:
            # print(lecture)
            day = lecture["date"]

            # print(day)
            day = datetime.strptime(
                day, "%Y-%m-%dT%H:%M:%S.000Z") + timedelta(hours=timedelta_add)

            # Format the datetime object to a string representing the date in 'day-month-year' format
            day_string = day.strftime('%d-%m-%Y')

            schedule.setdefault(day_string, []).append(
                lecture)

        except Exception as e:
            print(e)
    # print(schedule)
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
        print("Day not found...")


start_time = "13:08"

schedule.every().day.at(start_time).do(get_schedule)
print(f"Sending schedule every day at {start_time}...")
while True:
    schedule.run_pending()
    time.sleep(1)
