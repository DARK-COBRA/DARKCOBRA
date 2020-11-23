import os
import re
import urllib.request
import PIL.ImageOps
import requests
from PIL import Image, ImageDraw, ImageFont
from validators.url import url

async def moditweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=narendramodi"
    ).json()
    dc = r.get("message")
    cobra = url(dc)
    if not cobra:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(dc).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"


async def sunnytweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=sunnyleone"
    ).json()
    dc = r.get("message")
    cobra = url(dc)
    if not cobra:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(dc).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def johnnytweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=johnnysins"
    ).json()
    dc = r.get("message")
    cobra = url(dc)
    if not cobra:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(dc).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def kimtweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=_Kim_Jongun"
    ).json()
    dc = r.get("message")
    cobra = url(dc)
    if not cobra:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(dc).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

async def bhautweet(text):
    r = requests.get(
        f"https://nekobot.xyz/api/imagegen?type=tweet&text={text}&username=hindustanibhau"
    ).json()
    dc = r.get("message")
    cobra = url(dc)
    if not cobra:
        return "check syntax once more"
    with open("hehe.png", "wb") as f:
        f.write(requests.get(dc).content)
    img = Image.open("hehe.png").convert("RGB")
    img.save("hehe.webp", "webp")
    return "hehe.webp"

