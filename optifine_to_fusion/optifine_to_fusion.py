from PIL import Image
from os import path
import os, shutil

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'

if path.exists('out') == 1:
  shutil.rmtree('out')

def convertCompactCTM(blockName, folderName):
  tempTextureOutput = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
  ctmImg0 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/0.png').convert('RGBA')
  ctmImg1 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/1.png').convert('RGBA')
  ctmImg2 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/2.png').convert('RGBA')
  ctmImg3 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/3.png').convert('RGBA')
  ctmImg4 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/4.png').convert('RGBA')

  topLeft0 = ctmImg0.crop((0, 0, 16, 16))
  topRight0 = ctmImg0.crop((16, 0, 32, 16))
  bottomLeft0 = ctmImg0.crop((0, 16, 16, 32))
  bottomRight0 = ctmImg0.crop((16, 16, 32, 32))

  topLeft1 = ctmImg1.crop((0, 0, 16, 16))
  topRight1 = ctmImg1.crop((16, 0, 32, 16))
  bottomLeft1 = ctmImg1.crop((0, 16, 16, 32))
  bottomRight1 = ctmImg1.crop((16, 16, 32, 32))

  topLeft2 = ctmImg2.crop((0, 0, 16, 16))
  topRight2 = ctmImg2.crop((16, 0, 32, 16))
  bottomLeft2 = ctmImg2.crop((0, 16, 16, 32))
  bottomRight2 = ctmImg2.crop((16, 16, 32, 32))

  topLeft3 = ctmImg3.crop((0, 0, 16, 16))
  topRight3 = ctmImg3.crop((16, 0, 32, 16))
  bottomLeft3 = ctmImg3.crop((0, 16, 16, 32))
  bottomRight3 = ctmImg3.crop((16, 16, 32, 32))

  topLeft4 = ctmImg4.crop((0, 0, 16, 16))
  topRight4 = ctmImg4.crop((16, 0, 32, 16))
  bottomLeft4 = ctmImg4.crop((0, 16, 16, 32))
  bottomRight4 = ctmImg4.crop((16, 16, 32, 32))

# ┏━┓
# ┗━┛
  tempTextureOutput.paste(ctmImg0, (0, 0))
# ┏━━
# ┗━━
  tempTextureOutput.paste(topLeft0, (32, 0))
  tempTextureOutput.paste(topRight3, (48, 0))
  tempTextureOutput.paste(bottomLeft0, (32, 16))
  tempTextureOutput.paste(bottomRight3, (48, 16))
# ━━━
# ━━━
  tempTextureOutput.paste(ctmImg3, (64, 0))
# ━━┓
# ━━┛
  tempTextureOutput.paste(topLeft3, (96, 0))
  tempTextureOutput.paste(topRight0, (112, 0))
  tempTextureOutput.paste(bottomLeft3, (96, 16))
  tempTextureOutput.paste(bottomRight0, (112, 16))
# ┏━━
# ┃ ┏
  tempTextureOutput.paste(topLeft0, (128, 0))
  tempTextureOutput.paste(topRight3, (144, 0))
  tempTextureOutput.paste(bottomLeft2, (128, 16))
  tempTextureOutput.paste(bottomRight4, (144, 16))
# ━━┓
# ┓ ┃
  tempTextureOutput.paste(topLeft3, (160, 0))
  tempTextureOutput.paste(topRight0, (176, 0))
  tempTextureOutput.paste(bottomLeft4, (160, 16))
  tempTextureOutput.paste(bottomRight2, (176, 16))
# ┃ ┗
# ┃ ┏
  tempTextureOutput.paste(topLeft2, (192, 0))
  tempTextureOutput.paste(topRight4, (208, 0))
  tempTextureOutput.paste(bottomLeft2, (192, 16))
  tempTextureOutput.paste(bottomRight4, (208, 16))
# ━━━
# ┓ ┏
  tempTextureOutput.paste(topLeft3, (224, 0))
  tempTextureOutput.paste(topRight3, (240, 0))
  tempTextureOutput.paste(bottomLeft4, (224, 16))
  tempTextureOutput.paste(bottomRight4, (240, 16))

# -----------------------

# ┏━┓
# ┃ ┃
  tempTextureOutput.paste(topLeft0, (0, 32))
  tempTextureOutput.paste(topRight0, (16, 32))
  tempTextureOutput.paste(bottomLeft2, (0, 48))
  tempTextureOutput.paste(bottomRight2, (16, 48))
# ┏━━
# ┃
  tempTextureOutput.paste(topLeft0, (32, 32))
  tempTextureOutput.paste(topRight3, (48, 32))
  tempTextureOutput.paste(bottomLeft2, (32, 48))
  tempTextureOutput.paste(bottomRight1, (48, 48))
# ━━━
#
  tempTextureOutput.paste(topLeft3, (64, 32))
  tempTextureOutput.paste(topRight3, (80, 32))
  tempTextureOutput.paste(bottomLeft1, (64, 48))
  tempTextureOutput.paste(bottomRight1, (80, 48))
# ━━┓
#   ┃
  tempTextureOutput.paste(topLeft3, (96, 32))
  tempTextureOutput.paste(topRight0, (112, 32))
  tempTextureOutput.paste(bottomLeft1, (96, 48))
  tempTextureOutput.paste(bottomRight2, (112, 48))
# ┃ ┗
# ┗━━
  tempTextureOutput.paste(topLeft2, (128, 32))
  tempTextureOutput.paste(topRight4, (144, 32))
  tempTextureOutput.paste(bottomLeft0, (128, 48))
  tempTextureOutput.paste(bottomRight3, (144, 48))
# ┛ ┃
# ━━┛
  tempTextureOutput.paste(topLeft4, (160, 32))
  tempTextureOutput.paste(topRight2, (176, 32))
  tempTextureOutput.paste(bottomLeft3, (160, 48))
  tempTextureOutput.paste(bottomRight0, (176, 48))
# ┛ ┗
# ━━━
  tempTextureOutput.paste(topLeft4, (192, 32))
  tempTextureOutput.paste(topRight4, (208, 32))
  tempTextureOutput.paste(bottomLeft3, (192, 48))
  tempTextureOutput.paste(bottomRight3, (208, 48))
# ┛ ┃
# ┓ ┃
  tempTextureOutput.paste(topLeft4, (224, 32))
  tempTextureOutput.paste(topRight2, (240, 32))
  tempTextureOutput.paste(bottomLeft4, (224, 48))
  tempTextureOutput.paste(bottomRight2, (240, 48))

# -----------------------

# ┃ ┃
# ┃ ┃
  tempTextureOutput.paste(ctmImg2, (0, 64))
# ┃
# ┃
  tempTextureOutput.paste(topLeft2, (32, 64))
  tempTextureOutput.paste(topRight1, (48, 64))
  tempTextureOutput.paste(bottomLeft2, (32, 80))
  tempTextureOutput.paste(bottomRight1, (48, 80))
# ╳
  tempTextureOutput.paste(ctmImg1, (64, 64))
#   ┃
#   ┃
  tempTextureOutput.paste(topLeft1, (96, 64))
  tempTextureOutput.paste(topRight2, (112, 64))
  tempTextureOutput.paste(bottomLeft1, (96, 80))
  tempTextureOutput.paste(bottomRight2, (112, 80))
# ┃
# ┃ ┏
  tempTextureOutput.paste(topLeft2, (128, 64))
  tempTextureOutput.paste(topRight1, (144, 64))
  tempTextureOutput.paste(bottomLeft2, (128, 80))
  tempTextureOutput.paste(bottomRight4, (144, 80))
# ━━━
# ┓
  tempTextureOutput.paste(topLeft3, (160, 64))
  tempTextureOutput.paste(topRight3, (176, 64))
  tempTextureOutput.paste(bottomLeft4, (160, 80))
  tempTextureOutput.paste(bottomRight1, (176, 80))
# ┃ ┗
# ┃
  tempTextureOutput.paste(topLeft2, (192, 64))
  tempTextureOutput.paste(topRight4, (208, 64))
  tempTextureOutput.paste(bottomLeft2, (192, 80))
  tempTextureOutput.paste(bottomRight1, (208, 80))
# ━━━
#   ┏
  tempTextureOutput.paste(topLeft3, (224, 64))
  tempTextureOutput.paste(topRight3, (240, 64))
  tempTextureOutput.paste(bottomLeft1, (224, 80))
  tempTextureOutput.paste(bottomRight4, (240, 80))
# -----------------------
# ┃ ┃
# ┗━┛
  tempTextureOutput.paste(topLeft2, (0, 96))
  tempTextureOutput.paste(topRight2, (16, 96))
  tempTextureOutput.paste(bottomLeft0, (0, 112))
  tempTextureOutput.paste(bottomRight0, (16, 112))
# ┃
# ┗━━
  tempTextureOutput.paste(topLeft2, (32, 96))
  tempTextureOutput.paste(topRight1, (48, 96))
  tempTextureOutput.paste(bottomLeft0, (32, 112))
  tempTextureOutput.paste(bottomRight3, (48, 112))
#
# ━━━
  tempTextureOutput.paste(topLeft1, (64, 96))
  tempTextureOutput.paste(topRight1, (80, 96))
  tempTextureOutput.paste(bottomLeft3, (64, 112))
  tempTextureOutput.paste(bottomRight3, (80, 112))
#   ┃
# ━━┛
  tempTextureOutput.paste(topLeft1, (96, 96))
  tempTextureOutput.paste(topRight2, (112, 96))
  tempTextureOutput.paste(bottomLeft3, (96, 112))
  tempTextureOutput.paste(bottomRight0, (112, 112))
#   ┗
# ━━━
  tempTextureOutput.paste(topLeft1, (128, 96))
  tempTextureOutput.paste(topRight4, (144, 96))
  tempTextureOutput.paste(bottomLeft3, (128, 112))
  tempTextureOutput.paste(bottomRight3, (144, 112))
# ┛ ┃
#   ┃
  tempTextureOutput.paste(topLeft4, (160, 96))
  tempTextureOutput.paste(topRight2, (176, 96))
  tempTextureOutput.paste(bottomLeft1, (160, 112))
  tempTextureOutput.paste(bottomRight2, (176, 112))
# ┛
# ━━━
  tempTextureOutput.paste(topLeft4, (192, 96))
  tempTextureOutput.paste(topRight1, (208, 96))
  tempTextureOutput.paste(bottomLeft3, (192, 112))
  tempTextureOutput.paste(bottomRight3, (208, 112))
#   ┃
# ┓ ┃
  tempTextureOutput.paste(topLeft1, (224, 96))
  tempTextureOutput.paste(topRight2, (240, 96))
  tempTextureOutput.paste(bottomLeft4, (224, 112))
  tempTextureOutput.paste(bottomRight2, (240, 112))
# -----------------------
# ┛
#   ┏
  tempTextureOutput.paste(topLeft4, (0, 128))
  tempTextureOutput.paste(topRight1, (16, 128))
  tempTextureOutput.paste(bottomLeft1, (0, 144))
  tempTextureOutput.paste(bottomRight4, (16, 144))
# ┛ ┗
# ┓ ┏
  tempTextureOutput.paste(topLeft4, (32, 128))
  tempTextureOutput.paste(topRight4, (48, 128))
  tempTextureOutput.paste(bottomLeft4, (32, 144))
  tempTextureOutput.paste(bottomRight4, (48, 144))
# ┛
# ┓
  tempTextureOutput.paste(topLeft4, (64, 128))
  tempTextureOutput.paste(topRight1, (80, 128))
  tempTextureOutput.paste(bottomLeft4, (64, 144))
  tempTextureOutput.paste(bottomRight1, (80, 144))
# ┛ ┗
#
  tempTextureOutput.paste(topLeft4, (96, 128))
  tempTextureOutput.paste(topRight4, (112, 128))
  tempTextureOutput.paste(bottomLeft1, (96, 144))
  tempTextureOutput.paste(bottomRight1, (112, 144))
# ┛ ┗
# ┓
  tempTextureOutput.paste(topLeft4, (128, 128))
  tempTextureOutput.paste(topRight4, (144, 128))
  tempTextureOutput.paste(bottomLeft4, (128, 144))
  tempTextureOutput.paste(bottomRight1, (144, 144))
# ┛ ┗
#   ┏
  tempTextureOutput.paste(topLeft4, (160, 128))
  tempTextureOutput.paste(topRight4, (176, 128))
  tempTextureOutput.paste(bottomLeft1, (160, 144))
  tempTextureOutput.paste(bottomRight4, (176, 144))
#
#   ┏
  tempTextureOutput.paste(topLeft1, (192, 128))
  tempTextureOutput.paste(topRight1, (208, 128))
  tempTextureOutput.paste(bottomLeft1, (192, 144))
  tempTextureOutput.paste(bottomRight4, (208, 144))
#
# ┓
  tempTextureOutput.paste(topLeft1, (224, 128))
  tempTextureOutput.paste(topRight1, (240, 128))
  tempTextureOutput.paste(bottomLeft4, (224, 144))
  tempTextureOutput.paste(bottomRight1, (240, 144))
# -----------------------
#   ┗
# ┓
  tempTextureOutput.paste(topLeft1, (0, 160))
  tempTextureOutput.paste(topRight4, (16, 160))
  tempTextureOutput.paste(bottomLeft4, (0, 176))
  tempTextureOutput.paste(bottomRight1, (16, 176))
# BLANK
#
#
# ┓ ┏
  tempTextureOutput.paste(topLeft1, (64, 160))
  tempTextureOutput.paste(topRight1, (80, 160))
  tempTextureOutput.paste(bottomLeft4, (64, 176))
  tempTextureOutput.paste(bottomRight4, (80, 176))
#   ┗
#   ┏
  tempTextureOutput.paste(topLeft1, (96, 160))
  tempTextureOutput.paste(topRight4, (112, 160))
  tempTextureOutput.paste(bottomLeft1, (96, 176))
  tempTextureOutput.paste(bottomRight4, (112, 176))
# ┛
# ┓ ┏
  tempTextureOutput.paste(topLeft4, (128, 160))
  tempTextureOutput.paste(topRight1, (144, 160))
  tempTextureOutput.paste(bottomLeft4, (128, 176))
  tempTextureOutput.paste(bottomRight4, (144, 176))
#   ┗
# ┓ ┏
  tempTextureOutput.paste(topLeft1, (160, 160))
  tempTextureOutput.paste(topRight4, (176, 160))
  tempTextureOutput.paste(bottomLeft4, (160, 176))
  tempTextureOutput.paste(bottomRight4, (176, 176))
#   ┗
#
  tempTextureOutput.paste(topLeft1, (192, 160))
  tempTextureOutput.paste(topRight4, (208, 160))
  tempTextureOutput.paste(bottomLeft1, (192, 176))
  tempTextureOutput.paste(bottomRight1, (208, 176))
# ┛
#
  tempTextureOutput.paste(topLeft4, (224, 160))
  tempTextureOutput.paste(topRight1, (240, 160))
  tempTextureOutput.paste(bottomLeft1, (224, 176))
  tempTextureOutput.paste(bottomRight1, (240, 176))

  ctmImg0.close()
  ctmImg1.close()
  ctmImg2.close()
  ctmImg3.close()
  ctmImg4.close()

  if folderName == '':
    folderName = blockName

  tempTextureOutput.save(fileDir + 'out/textures/block/ctm/' + blockName + '/' + folderName + '.png')

def convertFullCTM(blockName, folderName):
  tempTextureOutput = Image.new('RGBA', (256, 256), (255, 255, 255, 0))
  ctmImg0 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/0.png').convert('RGBA')
  ctmImg1 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/1.png').convert('RGBA')
  ctmImg2 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/2.png').convert('RGBA')
  ctmImg3 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/3.png').convert('RGBA')
  ctmImg4 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/4.png').convert('RGBA')
  ctmImg5 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/5.png').convert('RGBA')
  ctmImg6 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/6.png').convert('RGBA')
  ctmImg7 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/7.png').convert('RGBA')
  ctmImg43 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/8.png').convert('RGBA')
  ctmImg36 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/9.png').convert('RGBA')
  ctmImg42 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/10.png').convert('RGBA')
  ctmImg41 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/11.png').convert('RGBA')
  ctmImg8 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/12.png').convert('RGBA')
  ctmImg9 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/13.png').convert('RGBA')
  ctmImg10 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/14.png').convert('RGBA')
  ctmImg11 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/15.png').convert('RGBA')
  ctmImg12 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/16.png').convert('RGBA')
  ctmImg13 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/17.png').convert('RGBA')
  ctmImg14 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/18.png').convert('RGBA')
  ctmImg15 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/19.png').convert('RGBA')
  ctmImg44 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/20.png').convert('RGBA')
  ctmImg37 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/21.png').convert('RGBA')
  ctmImg35 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/22.png').convert('RGBA')
  ctmImg34 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/23.png').convert('RGBA')
  ctmImg16 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/24.png').convert('RGBA')
  ctmImg17 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/25.png').convert('RGBA')
  ctmImg18 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/26.png').convert('RGBA')
  ctmImg19 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/27.png').convert('RGBA')
  ctmImg22 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/28.png').convert('RGBA')
  ctmImg23 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/29.png').convert('RGBA')
  ctmImg20 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/30.png').convert('RGBA')
  ctmImg21 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/31.png').convert('RGBA')
  ctmImg38 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/32.png').convert('RGBA')
  ctmImg39 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/33.png').convert('RGBA')
  ctmImg32 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/34.png').convert('RGBA')
  ctmImg40 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/35.png').convert('RGBA')
  ctmImg24 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/36.png').convert('RGBA')
  ctmImg25 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/37.png').convert('RGBA')
  ctmImg26 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/38.png').convert('RGBA')
  ctmImg27 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/39.png').convert('RGBA')
  ctmImg30 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/40.png').convert('RGBA')
  ctmImg31 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/41.png').convert('RGBA')
  ctmImg28 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/42.png').convert('RGBA')
  ctmImg29 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/43.png').convert('RGBA')
  ctmImg45 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/44.png').convert('RGBA')
  ctmImg46 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/45.png').convert('RGBA')
  ctmImg33 = Image.open(fileDir + 'in/' + blockName + '/' + folderName + '/46.png').convert('RGBA')

  tempTextureOutput.paste(ctmImg0, (0, 0))
  tempTextureOutput.paste(ctmImg1, (32, 0))
  tempTextureOutput.paste(ctmImg2, (64, 0))
  tempTextureOutput.paste(ctmImg3, (96, 0))
  tempTextureOutput.paste(ctmImg4, (128, 0))
  tempTextureOutput.paste(ctmImg5, (160, 0))
  tempTextureOutput.paste(ctmImg6, (192, 0))
  tempTextureOutput.paste(ctmImg7, (224, 0))
  tempTextureOutput.paste(ctmImg8, (0, 32))
  tempTextureOutput.paste(ctmImg9, (32, 32))
  tempTextureOutput.paste(ctmImg10, (64, 32))
  tempTextureOutput.paste(ctmImg11, (96, 32))
  tempTextureOutput.paste(ctmImg12, (128, 32))
  tempTextureOutput.paste(ctmImg13, (160, 32))
  tempTextureOutput.paste(ctmImg14, (192, 32))
  tempTextureOutput.paste(ctmImg15, (224, 32))
  tempTextureOutput.paste(ctmImg16, (0, 64))
  tempTextureOutput.paste(ctmImg17, (32, 64))
  tempTextureOutput.paste(ctmImg18, (64, 64))
  tempTextureOutput.paste(ctmImg19, (96, 64))
  tempTextureOutput.paste(ctmImg20, (128, 64))
  tempTextureOutput.paste(ctmImg21, (160, 64))
  tempTextureOutput.paste(ctmImg22, (192, 64))
  tempTextureOutput.paste(ctmImg23, (224, 64))
  tempTextureOutput.paste(ctmImg24, (0, 96))
  tempTextureOutput.paste(ctmImg25, (32, 96))
  tempTextureOutput.paste(ctmImg26, (64, 96))
  tempTextureOutput.paste(ctmImg27, (96, 96))
  tempTextureOutput.paste(ctmImg28, (128, 96))
  tempTextureOutput.paste(ctmImg29, (160, 96))
  tempTextureOutput.paste(ctmImg30, (192, 96))
  tempTextureOutput.paste(ctmImg31, (224, 96))
  tempTextureOutput.paste(ctmImg32, (0, 128))
  tempTextureOutput.paste(ctmImg33, (32, 128))
  tempTextureOutput.paste(ctmImg34, (64, 128))
  tempTextureOutput.paste(ctmImg35, (96, 128))
  tempTextureOutput.paste(ctmImg36, (128, 128))
  tempTextureOutput.paste(ctmImg37, (160, 128))
  tempTextureOutput.paste(ctmImg38, (192, 128))
  tempTextureOutput.paste(ctmImg39, (224, 128))
  tempTextureOutput.paste(ctmImg40, (0, 160))
  tempTextureOutput.paste(ctmImg41, (64, 160))
  tempTextureOutput.paste(ctmImg42, (96, 160))
  tempTextureOutput.paste(ctmImg43, (128, 160))
  tempTextureOutput.paste(ctmImg44, (160, 160))
  tempTextureOutput.paste(ctmImg45, (192, 160))
  tempTextureOutput.paste(ctmImg46, (224, 160))

  ctmImg0.close()
  ctmImg1.close()
  ctmImg2.close()
  ctmImg3.close()
  ctmImg4.close()
  ctmImg5.close()
  ctmImg6.close()
  ctmImg7.close()
  ctmImg8.close()
  ctmImg9.close()
  ctmImg10.close()
  ctmImg11.close()
  ctmImg12.close()
  ctmImg13.close()
  ctmImg14.close()
  ctmImg15.close()
  ctmImg16.close()
  ctmImg17.close()
  ctmImg18.close()
  ctmImg19.close()
  ctmImg20.close()
  ctmImg21.close()
  ctmImg22.close()
  ctmImg23.close()
  ctmImg24.close()
  ctmImg25.close()
  ctmImg26.close()
  ctmImg27.close()
  ctmImg28.close()
  ctmImg29.close()
  ctmImg30.close()
  ctmImg31.close()
  ctmImg32.close()
  ctmImg33.close()
  ctmImg34.close()
  ctmImg35.close()
  ctmImg36.close()
  ctmImg37.close()
  ctmImg38.close()
  ctmImg39.close()
  ctmImg40.close()
  ctmImg41.close()
  ctmImg42.close()
  ctmImg43.close()
  ctmImg44.close()
  ctmImg45.close()
  ctmImg46.close()

  print(folderName)
  print(blockName)
  print(fileDir + 'out/textures/block/ctm/' + blockName + '/' + folderName + '.png')

  if folderName == '':
    folderName = blockName

  print(fileDir + 'out/textures/block/ctm/' + blockName + '/' + folderName + '.png')

  tempTextureOutput.save(fileDir + 'out/textures/block/ctm/' + blockName + '/' + folderName + '.png')

def createMCMeta(blockName, folderName):
  if path.exists('out/textures/block/ctm/' + blockName) != 1:
    os.mkdir('out/textures/block/ctm/' + blockName)
  if folderName == '':
    folderName = blockName
  f = open('out/textures/block/ctm/' + blockName + '/' + folderName + ".png.mcmeta", "w")
  f.write('{\n')
  f.write('	"fusion": {\n')
  f.write('		"type": "connecting",\n')
  f.write('		"layout": "full"\n')
  f.write('	}\n')
  f.write('}')
  f.close()

def createBasicModel(blockName, folderName):
  if folderName != '':
    folderName = folderName + '/'
  ctmFiles = os.listdir(fileDir + 'in/' + blockName + '/' + folderName)
  ctmFile = [file for file in ctmFiles if file.split('.')[1] == 'properties']
  ctmPropertiesFile = open(fileDir + 'in/' + blockName + '/' + folderName + ctmFile[0], "r")
  ctmPropertiesFileContents = ctmPropertiesFile.readlines()
  ctmPropertiesFile.close()

  for v in range(0, len(ctmPropertiesFileContents)):
    if len(ctmPropertiesFileContents[v].split('method=')) != 1:
      if ctmPropertiesFileContents[v].split('method=')[1].strip() != 'ctm_compact' and ctmPropertiesFileContents[v].split('method=')[1].strip() != 'ctm':
        method = ctmPropertiesFileContents[v].split('method=')[1].strip()
        return method

  if len(ctmPropertiesFileContents[0].split('matchTiles=')) != 1:
    connectedBlocks = ctmPropertiesFileContents[0].split('matchTiles=')[1]
  elif len(ctmPropertiesFileContents[0].split('matchBlocks=')) != 1:
    connectedBlocks = ctmPropertiesFileContents[0].split('matchBlocks=')[1]

  f = open('out/models/block/' + connectedBlocks.split(' ')[0].strip() + ".json", "w")
  f.write('{\n')
  f.write('	"loader": "fusion:model",\n')
  f.write('	"type": "connecting",\n')
  f.write('	"connections": [\n')

  isConnectionTypeSet = False

  def getConnectionType(isOnlyBlock, connectionTypeSet):
    for w in range(0, len(ctmPropertiesFileContents)):
      if len(ctmPropertiesFileContents[w].split('connect=')) > 1:
        if ctmPropertiesFileContents[w].split('connect=')[1].strip() == 'tile' or ctmPropertiesFileContents[0].split('connect=')[1].strip() == 'block':
          if isOnlyBlock is False and connectionTypeSet is False:
            f.write('		{ "type": "is_same_block" },\n')
            return True
          elif isOnlyBlock is True and connectionTypeSet is False:
            f.write('		{ "type": "is_same_block" }\n')
            return True
      else:
        if w == len(ctmPropertiesFileContents) - 1 and connectionTypeSet is False:
          f.write('		{ "type": "is_same_block" }\n')
          return True

  for z in range(0, len(connectedBlocks.split(' '))):
    if connectedBlocks.split(' ')[z].strip() != connectedBlocks.split(' ')[0].strip():
      isConnectionTypeSet = getConnectionType(False, isConnectionTypeSet)
      if z != len(connectedBlocks.split(' ')) - 1:
        f.write('		{ "type": "match_block", "block": "' + connectedBlocks.split(' ')[z].strip() + '" },\n')
      else:
        f.write('		{ "type": "match_block", "block": "' + connectedBlocks.split(' ')[z].strip() + '" }\n')
    else:
      if len(connectedBlocks.split(' ')) == 1:
        isConnectionTypeSet = getConnectionType(True, isConnectionTypeSet)

  if folderName == '':
    folderName = blockName
  else:
    folderName = folderName.split('/')[0]
  f.write('	],\n')
  f.write('	"parent": "block/cube_all",\n')
  f.write('	"textures": {\n')
  f.write('		"all": "block/ctm/' + blockName + '/' + folderName + '"\n')
  f.write('	}\n')
  f.write('}\n')
  f.close()

  for u in range(0, len(ctmPropertiesFileContents)):
    if len(ctmPropertiesFileContents[u].split('method=')) != 1:
      method = ctmPropertiesFileContents[u].split('method=')[1].strip()
      return method

ctmBlockFolders = os.listdir(fileDir + 'in/')

os.mkdir('out')
os.mkdir('out/models')
os.mkdir('out/models/block')
os.mkdir('out/textures')
os.mkdir('out/textures/block')
os.mkdir('out/textures/block/ctm')

for x in range(0, len(ctmBlockFolders)):
  ctmFolder = os.listdir(fileDir + 'in/' + ctmBlockFolders[x] + '/')
  os.mkdir('out/textures/block/ctm/' + ctmBlockFolders[x])
  for y in range(0, len(ctmFolder)):
    if len(ctmFolder[y].split('.png')) > 1 or len(ctmFolder[y].split('.properties')) > 1:
      ctmFolderName = ''
    else:
      ctmFolderName = ctmFolder[y]
    if createBasicModel(ctmBlockFolders[x], ctmFolderName) == 'ctm_compact':
      convertCompactCTM(ctmBlockFolders[x], ctmFolderName)
      createMCMeta(ctmBlockFolders[x], ctmFolderName)
    elif createBasicModel(ctmBlockFolders[x], ctmFolderName) == 'ctm':
      convertFullCTM(ctmBlockFolders[x], ctmFolderName)
      createMCMeta(ctmBlockFolders[x], ctmFolderName)
    else:
      print('CTM Method: ' + createBasicModel(ctmBlockFolders[x], ctmFolderName) + ' is not Supported!')
