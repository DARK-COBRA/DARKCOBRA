import os
import time
import math
import asyncio
from youtube_dl import YoutubeDL
from youtube_dl.utils import (DownloadError, ContentTooShortError,
                              ExtractorError, GeoRestrictedError,
                              MaxDownloadsReached, PostProcessingError,
                              UnavailableVideoError, XAttrMetadataError)
from asyncio import sleep
from telethon.tl.types import DocumentAttributeAudio
from uniborg.util import admin_cmd


try:
   from youtubesearchpython import SearchVideos 
except:
	os.system("pip install pip install youtube-search-python")
	from youtubesearchpython import SearchVideos 


@borg.on(admin_cmd(pattern="vsong (.*)"))
async def download_video(v_url):  
    pro = v_url ; sender = await pro.get_sender() ; me = await pro.client.get_me()
    if not sender.id == me.id:
        dc = await pro.reply("`processing...`")
    else:
    	dc = await pro.edit("`processing...`")   
    teamcobra = v_url.pattern_match.group(1)
    if not teamcobra:
         return await dc.edit("`Error \nusage vsong <song name>`")
    search = SearchVideos(url, offset = 1, mode = "json", max_results = 1)
    test = search.result()
    p = json.loads(test)
    q = p.get('search_result')
    try:
       url = q[0]['link']
    except:
    	return await dc.edit("`failed to find your desired song`")
    type = "audio"
    await dc.edit("`Ok downloading your song🤓...`")
    if type == "audio":
        opts = {
            'format':
            'best',
            'addmetadata':
            True,
            'key':
            'FFmpegMetadata',
            'prefer_ffmpeg':
            True,
            'geo_bypass':
            True,
            'nocheckcertificate':
            True,
            'postprocessors': [{
                'key': 'FFmpegVideoConvertor',
                'preferedformat': 'mp4'
            }],
            'outtmpl':
            '%(id)s.mp4',
            'logtostderr':
            False,
            'quiet':
            True
        }
        song = False
        video = True
    try:
        await dc.edit("`Fetching data, please wait..`")
        with YoutubeDL(opts) as darkcobra:
            darkcobra_data = darkcobra.extract_info(url)
    except DownloadError as error:
        await dc.edit(f"`{str(error)}`")
        return
    except ContentTooShortError:
        await dc.edit("`Oof the download content was too short😮🤐.`")
        return
    except GeoRestrictedError:
        await dc.edit(
            "`Video is not available from your geographic location due to geographic restrictions imposed by a website🤔.`"
        )
        return
    except MaxDownloadsReached:
        await dc.edit("`Max-downloads limit has been reached😶.`")
        return
    except PostProcessingError:
        await dc.edit("`There was an error during post processing😐.`")
        return
    except UnavailableVideoError:
        await dc.edit("`sorry, media is not available in the requested format.`")
        return
    except XAttrMetadataError as XAME:
        await dc.edit(f"`{XAME.code}: {XAME.msg}\n{XAME.reason}`")
        return
    except ExtractorError:
        await dc.edit("`There was an error while fetching your query...`")
        return
    except Exception as e:
        await dc.edit(f"{str(type(e)): {str(e)}}")
        return
    c_time = time.time()
    if song:
        await dc.edit(f"`Preparing to upload your video song😎 `\
        \n**{darkcobra_data['title']}**\
        \nby *{darkcobra_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{darkcobra_data['id']}.mp3",
            supports_streaming=True,
            attributes=[
                DocumentAttributeAudio(duration=int(darkcobra_data['duration']),
                                       title=str(darkcobra_data['title']),
                                       performer=str(darkcobra_data['uploader']))
            ],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading your video song😍..",
                         f"{darkcobra_data['title']}.mp3")))
        os.remove(f"{darkcobra_data['id']}.mp3")
        await v_url.delete()
    elif video:
        await dc.edit(f"`Preparing to upload your video song🤗 :`\
        \n**{darkcobra_data['title']}**\
        \nby *{darkcobra_data['uploader']}*")
        await v_url.client.send_file(
            v_url.chat_id,
            f"{darkcobra_data['id']}.mp4",
            supports_streaming=True,
            caption=darkcobra_data['title'],
            progress_callback=lambda d, t: asyncio.get_event_loop(
            ).create_task(
                progress(d, t, v_url, c_time, "Uploading..",
                         f"{darkcobra_data['title']}.mp4")))
        os.remove(f"{darkcobra_data['id']}.mp4")
        await dc.delete()
