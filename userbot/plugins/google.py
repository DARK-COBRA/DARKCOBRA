""" Powered by @Google
Available Commands:
.gs <query>

.grs"""



import requests
from bs4 import BeautifulSoup
from datetime import datetime
from google_images_download import google_images_download
from userbot.utils import admin_cmd
from search_engine_parser import GoogleSearch
        

def progress(current, total):
    logger.info("Downloaded {} of {}\nCompleted {}".format(current, total, (current / total) * 100))


@borg.on(admin_cmd(pattern="gs ?(.*)"))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("searching")
    input_str = event.pattern_match.group(1)
    if not input_str:
        return await event.edit("Give something to search")
    gs = GoogleSearch()
    res = await gs.async_search(f"{input_str}")
    output_str = ""
    for i in range(len(res["links"])):
        text = res["titles"][i]
        url = res["links"][i]
        output_str += " 👉🏻  [{}]({}) \n\n".format(text, url)
    await event.edit("**Google: {}\n{}**".format(input_str, output_str), link_preview=False)





@borg.on(admin_cmd(pattern="grs"))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    BASE_URL = "http://www.google.com"
    OUTPUT_STR = "Reply to an image to do Google Reverse Search"
    if event.reply_to_msg_id:
        await event.edit("Pre Processing Media")
        previous_message = await event.get_reply_message()
        previous_message_text = previous_message.message
        if previous_message.media:
            downloaded_file_name = await borg.download_media(
                previous_message,
                Config.TMP_DOWNLOAD_DIRECTORY
            )
            SEARCH_URL = "{}/searchbyimage/upload".format(BASE_URL)
            multipart = {
                "encoded_image": (downloaded_file_name, open(downloaded_file_name, "rb")),
                "image_content": ""
            }
            # https://stackoverflow.com/a/28792943/4723940
            google_rs_response = requests.post(SEARCH_URL, files=multipart, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
            os.remove(downloaded_file_name)
        else:
            previous_message_text = previous_message.message
            SEARCH_URL = "{}/searchbyimage?image_url={}"
            request_url = SEARCH_URL.format(BASE_URL, previous_message_text)
            google_rs_response = requests.get(request_url, allow_redirects=False)
            the_location = google_rs_response.headers.get("Location")
        await event.edit("Found Google Result")
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0"
        }
        response = requests.get(the_location, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        # document.getElementsByClassName("r5a77d"): PRS
        prs_div = soup.find_all("div", {"class": "r5a77d"})[0]
        prs_anchor_element = prs_div.find("a")
        prs_url = BASE_URL + prs_anchor_element.get("href")
        prs_text = prs_anchor_element.text
        # document.getElementById("jHnbRc")
        img_size_div = soup.find(id="jHnbRc")
        img_size = img_size_div.find_all("div")
        end = datetime.now()
        ms = (end - start).seconds
        OUTPUT_STR = """{img_size}
*Possible Related Search*: <a href="{prs_url}">{prs_text}</a>

More Info: Open this <a href="{the_location}">LINK</a> in {ms} seconds""".format(**locals())
    await event.edit(OUTPUT_STR, parse_mode="HTML", link_preview=False)


 
