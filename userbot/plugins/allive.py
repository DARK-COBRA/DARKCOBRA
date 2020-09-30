#Functions

def get_readable_time(seconds: int) -> str:

    count = 0

    ping_time = ""

    time_list = []

    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:

        count += 1

        if count < 3:

            remainder, result = divmod(seconds, 60)

        else:

            remainder, result = divmod(seconds, 24)

        if seconds == 0 and remainder == 0:

            break

        time_list.append(int(result))

        seconds = int(remainder)

    for x in range(len(time_list)):

        time_list[x] = str(time_list[x]) + time_suffix_list[x]

    if len(time_list) == 4:

        ping_time += time_list.pop() + ", "

    time_list.reverse()

    ping_time += ":".join(time_list)

    return ping_time

uptime = get_readable_time((time.time() - Lastupdate))

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "Unknown"

PM_IMG = "https://telegra.ph/file/6ea2e0728fb5a7fd73c5f.jpg"

pm_caption = "➥ **GODZILLA IS:** `ONLINE`\n\n"

pm_caption += "➥ **SYSTEMS STATS**\n"

pm_caption += "➥ **Telethon Version:** `1.15.0` \n"

pm_caption += "➥ **Python:** `3.7.4` \n"

pm_caption += f"➥ **Uptime** : `{uptime}` \n"

pm_caption += "➥ **Database Status:**  `Functional`\n"

pm_caption += "➥ **Current Branch** : `master`\n"

pm_caption += f"➥ **Version** : `{currentversion}`\n"

pm_caption += f"➥ **My Boss** : {DEFAULTUSER} \n"

pm_caption += "➥ **Heroku Database** : `AWS - Working Properly`\n\n"
