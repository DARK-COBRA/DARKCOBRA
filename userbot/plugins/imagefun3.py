   # originally made by @danish_00 
   # Team dc
   # For cobra

from PIL import Image
import numpy as np
import os, shutil, sys ,cv2, asyncio, scipy, random
from telegraph import upload_file
from telethon.tl.types import MessageMediaPhoto
from userbot.utils import admin_cmd
from userbot import bot , CMD_HELP

path = "./dcobra/"
if not os.path.isdir(path):
    os.makedirs(path)


# Originally Created by @danish_00 
# All Basics opencv just , the .rtoon was little challenging


@bot.on(admin_cmd("rtoon"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    image = await bot.download_media(reply.media, path)
    await event.edit("`Processing... takes time`")
    img = cv2.VideoCapture(image) 
    ret, frame = img.read() 
    height, width, channels = frame.shape
    samples = np.zeros([height*width, 3], dtype = np.float32)
    count = 0
    for x in range(height):
        for y in range(width):
           samples[count] = frame[x][y] 
           count += 1
    compactness, labels, centers = cv2.kmeans(samples,
                                        13, 
                                        None,
                                        (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 10000, 0.0001), 
                                        5, 
                                        cv2.KMEANS_PP_CENTERS)
    centers = np.uint8(centers)
    res = centers[labels.flatten()]
    nikal = res.reshape((frame.shape))
    cv2.imwrite("danish.jpg", nikal)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")


    # opencv basics 

@bot.on(admin_cmd("ctoon"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()  
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 5) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 13, 400, 400)
    cartoon = cv2.bitwise_and(color, color, mask=edges) 
    cv2.imwrite("danish.jpg", cartoon)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, caption = "To Know How this works type .howctoon",reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")



@bot.on(admin_cmd("danger"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    dark = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cobra = cv2.cvtColor(dark ,cv2.COLOR_HSV2BGR)
    cv2.imwrite("danish.jpg", cobra)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

@bot.on(admin_cmd("vintage"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image,cv2.IMREAD_GRAYSCALE) 
    ret, frame = img.read()
    cobra = cv2.applyColorMap(frame, cv2.COLORMAP_PINK)
    cv2.imwrite("danish.jpg", cobra)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")
    

@bot.on(admin_cmd("random"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image,cv2.IMREAD_GRAYSCALE) 
    ret, frame = img.read()
    x=(random.randrange(1,12))
    if x == 1:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_BONE)
    if x == 2:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_JET)
    if x == 3:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_WINTER)
    if x == 4:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_RAINBOW)
    if x == 5:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_OCEAN)
    if x == 6:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_SUMMER)
    if x == 7:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_SPRING)
    if x == 8:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_COOL)
    if x == 9:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_HSV)
    if x == 10:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_PINK)
    if x == 11:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_HOT)
    if x == 12:
      style = cv2.applyColorMap(frame, cv2.COLORMAP_AUTUMN)
    cv2.imwrite("danish.jpg", style)
    await event.client.send_file(event.chat_id, "danish.jpg", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.jpg")

    
    

@bot.on(admin_cmd("rmbw"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image like this :-.rmbw 01;1.5;9; u can have any value instead")
        return
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    ims=image
    os.system(f'wget https://telegra.ph/file/9974f1b3947f5f97f4075.png')
    lbcn= '9974f1b3947f5f97f4075.png'
    img1 = cv2.VideoCapture(ims) 
    ret, frame = img1.read()
    img2 = cv2.imread(f'{lbcn}')
    achha = cv2.imwrite("cobra.jpg",frame)
    image = Image.open("cobra.jpg")
    shi,vam = image.size
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img1 =cv2.resize(img1,(620,350))
    img2 =cv2.resize(img2,(620,350))
    mix = cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.45,gamma=0)
    mila = cv2.cvtColor(mix, cv2.COLOR_RGB2BGR)
    cv2.imwrite("danish.png", mila)
    shvm = Image.open("danish.png")
    img=shvm.resize((int(shi),int(vam)))
    img.save("danish.png", format="PNG", optimize=True)
    await event.client.send_file(event.chat_id, "danish.png", force_document=False, reply_to=event.reply_to_msg_id)
    await event.delete()
    shutil.rmtree(path)
    os.remove("danish.png")
    os.remove("cobra.jpg")

@bot.on(admin_cmd("howctoon"))
async def howitworks(event):
    if not event.reply_to_msg_id:
        await event.reply("Reply to any Image.")
        returnp
    reply = await event.get_reply_message()
    await event.edit('`Processing...`')
    image = await bot.download_media(reply.media, path)
    img = cv2.VideoCapture(image) 
    ret, frame = img.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    gray = cv2.medianBlur(gray, 5) 
    edges = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 9, 9)
    color = cv2.bilateralFilter(frame, 13, 400, 400)
    cartoon = cv2.bitwise_and(color, color, mask=edges) 
    cv2.imwrite("a.jpg", frame) 
    cv2.imwrite("b.jpg", gray) 
    cv2.imwrite("c.jpg", edges)
    cv2.imwrite("d.jpg", color) 
    cv2.imwrite("e.jpg", cartoon) 
    ori = cv2.imread("a.jpg")
    res = cv2.imread("e.jpg")
    v_img = cv2.vconcat([ori, res])
    h_img = cv2.hconcat([ori, res])
    cv2.imwrite('H.jpg', h_img)
    cv2.imwrite('V.jpg', v_img)
    await event.delete()
    da = await bot.send_file(event.chat.id, "a.jpg", caption = "Original Pic")
    await asyncio.sleep(3)
    ni = await bot.edit_message(event.chat.id, da, file = "b.jpg" )
    hm = await bot.edit_message(event.chat.id, ni,"Stage 1 - Collecting The Gray form.")
    await asyncio.sleep(3.5)
    sh = await bot.edit_message(event.chat.id, hm, file = "c.jpg")
    lo = await bot.edit_message(event.chat.id, sh, "Stage 2 - Collecting The Threshold Edges .")
    await asyncio.sleep(3.5)
    co = await bot.edit_message(event.chat.id, lo, file = "d.jpg")
    he = await bot.edit_message(event.chat.id, co, "Stage 3 - Collecting Smooth Color.")
    await asyncio.sleep(3.5)
    bro = await bot.edit_message(event.chat.id, he, file = "e.jpg")
    danish = await bot.edit_message(event.chat.id, co, "Output - Merged All Stages.")
    await asyncio.sleep(3.5)
    x=(random.randrange(1,2))
    if x == 1:
       await bot.send_file(event.chat.id, file = "V.jpg", caption =
       """ㅤ                                            Check Difference 

                                            ©DARKCOBRA""")
    if x == 2:                    
       await bot.send_file(event.chat.id,file = "H.jpg", caption = 
       """ㅤ                                            Check Difference 
    
                                            ©DARKCOBRA""")
    shutil.rmtree(path)
    os.remove("a.jpg")
    os.remove("b.jpg")
    os.remove("c.jpg")
    os.remove("d.jpg")
    os.remove("e.jpg")
    os.remove("H.jpg")
    os.remove("V.jpg")


    
@bot.on(admin_cmd(pattern = "merge ?(.*)"))
async def hehe(event):
    if not event.reply_to_msg_id:
        await event.edit("Reply to any Image. and give link of other image to mix.")
        return
    if not event.pattern_match.group(1):
        await event.edit("Give a link to which u want to merge")
        return
    await event.edit('`Processing...`')
    linc= event.text
    link=linc[7:]
    pic=linc[31:]
    os.system(f'wget {link}')
    dpath = f"{pic}"
    reply = await event.get_reply_message()
    image = await bot.download_media(reply.media, path)
    ims=image
    image = Image.open(image)
    shi,vam = image.size
    img1 = cv2.VideoCapture(ims) 
    ret, frame = img1.read()
    img2 = cv2.imread(dpath)
    img1 = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    img2 = cv2.cvtColor(img2, cv2.COLOR_BGR2RGB)
    img1 =cv2.resize(img1,(620,350))
    img2 =cv2.resize(img2,(620,350))
    mix = cv2.addWeighted(src1=img1,alpha=0.8,src2=img2,beta=0.5,gamma=0)
    mila = cv2.cvtColor(mix, cv2.COLOR_RGB2BGR)
    cv2.imwrite("danish.png", mila)
    shvm = Image.open("danish.png")
    img=shvm.resize((int(shi),int(vam)))
    img.save("danish.png", format="PNG", optimize=True)
    await event.delete()
    await event.client.send_file(event.chat_id, "danish.png", force_document=False, reply_to=event.reply_to_msg_id)
    shutil.rmtree(path)
    os.remove("danish.png")


CMD_HELP.update(
    {
        "imagefun3": "__**PLUGIN NAME :** Image fun2 _\
    \n\n📌** CMD ★** `.rtoon(reply to media)`\
    \n**USAGE   ★  **Send u can smooth toon like pic \
    \n\n📌** CMD ★** `.ctoon (reply to media)`\
    \n**USAGE   ★  **Send u Cartoon Comics like Output\
    \n\n📌** CMD ★** `.merge(reply to media)(add link of other image on text)`\
    \n**USAGE   ★  **It will Merge The replyed image with the link.\
    \n\n📌** CMD ★** `.vintage(reply to media)`\
    \n**USAGE   ★  **Add cool Old type filter \
    \n\n📌** CMD ★** `.danger(reply to media)`\
    \n**USAGE   ★  **Add Danger looking filter \
    \n\n📌** CMD ★** `.random(reply to media)`\
    \n**USAGE   ★  **Add some random filters \
    \n\n📌** CMD ★** `.rmbw / .howctoon`\
    \ncheck them on ur own 😁😁"
    
      
    }
)
    # Thank U for ur Efforts to check out this

  

 
