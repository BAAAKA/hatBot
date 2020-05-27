from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import os
import time
import random

pasteCoordinates = (205, 140)
pasteCoordinatesText = (100, 380)
pasteCoordinatesNameText = (120, 460)

avatarSize = (300, 300)

hatTypes = {}
hatTypes["marisa"] = "image/hat.png", 100, 0
hatTypes["flandre"] = "image/hat_flandre.png", 170, 30
hatTypes["doremy"] = "image/hat_doremy.png", 200, 50
hatTypes["clownpiece"] = "image/hat_clownpiece.png", 110, 0
hatTypes["alice"] = "image/hat_alice.png", 215, 100
hatTypes["keine"] = "image/hat_keine.png", 245, 80
hatTypes["remilia"] = "image/hat_remilia.png", 200, 80
hatTypes["reimu"] = "image/hat_reimu.png", 170, 100
hatTypes["eiki"] = "image/hat_eiki.png", 150, 70
hatTypes["koishi"] = "image/hat_koishi.png", 150, 70
hatTypes["tenshi"] = "image/hat_tenshi.png", 150, 70
hatTypes["patchouli"] = "image/hat_patchouli.png", 150, 70
hatTypes["zun"] = "image/hat_zun.png", 180, 110
hatTypes["mokou"] = "image/hat_mokou.png", 170, 70
hatTypes["rin"] = "image/hat_rin.png", 180, 110
hatTypes["yuyuko"] = "image/hat_yuyuko.png", 180, 110

backgrounds = []
backgrounds.append("image/background.jpg")
backgrounds.append("image/background2.jpg")
backgrounds.append("image/background3.jpg")
backgrounds.append("image/background4.jpg")



def getImage(url, user, hatType, yOffset, xOffset, scale):
    print("[INFO] New Request!")

    #Get User Avater
    avatarImg = getAvatarImage(url)
    avatarImg = avatarImg.resize(avatarSize, Image.ANTIALIAS)
    avatarImg.save("avatar/avatar.png")

    #Hat and resize of it
    hatImg = Image.open(hatTypes[hatType][0])
    oldX = hatImg.size[0]
    oldY = hatImg.size[1]
    newX = oldX + int(scale)
    newY = oldY + int(scale)
    hatImg = hatImg.resize((newX, newY), Image.ANTIALIAS)
    readjust = int(newX-oldX)/2
    pasteCoordinatesHat = ((hatTypes[hatType][1]-int(readjust))+int(xOffset), hatTypes[hatType][2]-int(yOffset))

    #Other Images
    BGImg = Image.open(getBackground())
    circleImg = Image.open('image/circle_2.png')
    textImg = Image.open('image/hat4u_pink.png')

    #Paste
    BGImg.paste(avatarImg, pasteCoordinates, mask=circleImg)
    BGImg.paste(hatImg, pasteCoordinatesHat, mask=hatImg)
    BGImg.paste(textImg, pasteCoordinatesText, mask=textImg)

    #Text
    d = ImageDraw.Draw(BGImg)
    d.text(pasteCoordinatesNameText, user, font=getFont(70), fill=(251, 87, 129))
    print("[INFO] Dont with pasting!")

    #Saving and log
    filename = time.strftime("result_%Y%m%d-%H%M%S.png")
    filePath = "result/{}".format(filename)
    BGImg.save(filePath)
    print("[INFO] Done with Image!")
    print("==============================")
    return filePath


def getAvatarImage(url):
    r = requests.get(url)
    avatarImg = Image.open(BytesIO(r.content))
    return avatarImg


def getFont(size):
    if os.name == "nt":
        print("[INFO] WINDOWS FONT")
        fontPath = r"D:\Programme\pyCharm\jbr\lib\fonts\SourceCodePro-Bold.ttf"
    else:
        print("[INFO] LINUX FONT")
        fontPath = r"/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"
    return ImageFont.truetype(fontPath, size)


def getHatTypes():
    return hatTypes

def getBackground():
    return random.choice(backgrounds)