from PIL import Image
from os import path
import os, sys, shutil

fileDir = os.getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'

ctmFiles = os.listdir(fileDir + 'in/ctm/')
planksFiles = os.listdir(fileDir + 'in/planks/')

if path.exists('out') == 1:
  shutil.rmtree('out')

os.mkdir('out')

def createImage0(ctmFile, planksFile):
  tempTextureOutput = Image.new('RGBA', (32, 32), (255, 255, 255, 0))
  ctmImg = Image.open(ctmFile).convert('RGBA')
  planksImg = Image.open(planksFile).convert('RGBA')
  
  tempTexture1 = planksImg.crop((7, 0, 11, 8))
  tempTexture1 = tempTexture1.transpose(Image.FLIP_LEFT_RIGHT)
  tempTextureOutput.paste(tempTexture1, (0, 0))
  
  tempTexture2 = planksImg.crop((13, 16, 17, 24))
  tempTextureOutput.paste(tempTexture2, (0, 16))
  
  tempTexture3 = planksImg.crop((18, 8, 22, 16))
  tempTexture3 = tempTexture3.transpose(Image.FLIP_LEFT_RIGHT)
  tempTextureOutput.paste(tempTexture3, (28, 8))
  
  tempTexture4 = planksImg.crop((18, 24, 22, 32))
  tempTextureOutput.paste(tempTexture4, (28, 24))
  
  tempTexture5 = ctmImg.crop((0, 8, 8, 16))
  tempTextureOutput.paste(tempTexture5, (0, 8))
  
  tempTexture6 = ctmImg.crop((0, 24, 10, 32))
  tempTextureOutput.paste(tempTexture6, (0, 24))
  
  tempTexture7 = ctmImg.crop((21, 0, 32, 8))
  tempTextureOutput.paste(tempTexture7, (21, 0))
  
  tempTexture8 = ctmImg.crop((24, 16, 32, 24))
  tempTextureOutput.paste(tempTexture8, (24, 16))
  
  return tempTextureOutput

def createImage1(ctmFile, planksFile):
  tempTextureOutput = Image.new('RGBA', (32, 32), (255, 255, 255, 0))
  ctmImg = Image.open(ctmFile).convert('RGBA')
  planksImg = Image.open(planksFile).convert('RGBA')

  tempTexture1 = planksImg.crop((7, 0, 11, 8))
  tempTexture1 = tempTexture1.transpose(Image.FLIP_LEFT_RIGHT)
  tempTextureOutput.paste(tempTexture1, (0, 0))
  
  tempTexture2 = planksImg.crop((13, 16, 17, 24))
  tempTextureOutput.paste(tempTexture2, (0, 16))
  
  tempTexture3 = ctmImg.crop((0, 8, 8, 16))
  tempTextureOutput.paste(tempTexture3, (0, 8))
  
  tempTexture4 = ctmImg.crop((0, 24, 10, 32))
  tempTextureOutput.paste(tempTexture4, (0, 24))
  
  return tempTextureOutput

def createImage2(ctmFile, planksFile):
  tempTextureOutput = Image.new('RGBA', (32, 32), (255, 255, 255, 0))
  ctmImg = Image.open(ctmFile).convert('RGBA')
  planksImg = Image.open(planksFile).convert('RGBA')
  
  tempTexture1 = planksImg.crop((18, 8, 22, 16))
  tempTexture1 = tempTexture1.transpose(Image.FLIP_LEFT_RIGHT)
  tempTextureOutput.paste(tempTexture1, (28, 8))
  
  tempTexture2 = planksImg.crop((18, 24, 22, 32))
  tempTextureOutput.paste(tempTexture2, (28, 24))
  
  tempTexture3 = ctmImg.crop((21, 0, 32, 8))
  tempTextureOutput.paste(tempTexture3, (21, 0))
  
  tempTexture4 = ctmImg.crop((24, 16, 32, 24))
  tempTextureOutput.paste(tempTexture4, (24, 16))
  
  return tempTextureOutput

def createProperties(primaryPlank, secondaryPlank):
  if path.exists('out/' + primaryPlank + '_planks') != 1:
    os.mkdir('out/' + primaryPlank + '_planks')
  if path.exists('out/' + primaryPlank + '_planks' + '/' + primaryPlank + '_on_' + secondaryPlank) != 1:
    os.mkdir('out/' + primaryPlank + '_planks' + '/' + primaryPlank + '_on_' + secondaryPlank)
  
  outputDir = 'out/' + primaryPlank + '_planks' + '/' + primaryPlank + '_on_' + secondaryPlank + '/'
  
  f = open('out/' + primaryPlank + '_planks' + '/' + primaryPlank + '_on_' + secondaryPlank+ '/' + primaryPlank + '_on_' + secondaryPlank + ".properties", "w")
  f.write('matchBlocks=' + secondaryPlank + '_planks\n')
  f.write('method=overlay\n')
  f.write('tiles=<skip> <skip> <skip> 0 1 2 1 2 0 1 2 1 2 0 <skip> <skip> <skip> \n')
  f.write('connect=block\n')
  f.write('connectBlocks=' + primaryPlank + '_planks\n')
  f.write('layer=cutout\n')
  f.close()
  
  image0 = createImage0(fileDir + 'in/ctm/' + primaryPlank + '_planks.png', fileDir + 'in/planks/' + secondaryPlank + '_planks.png')
  image1 = createImage1(fileDir + 'in/ctm/' + primaryPlank + '_planks.png', fileDir + 'in/planks/' + secondaryPlank + '_planks.png')
  image2 = createImage2(fileDir + 'in/ctm/' + primaryPlank + '_planks.png', fileDir + 'in/planks/' + secondaryPlank + '_planks.png')
  
  image0.save(outputDir + '0.png')
  image1.save(outputDir + '1.png')
  image2.save(outputDir + '2.png')

for x in range(0, len(ctmFiles)):
  for y in range(0, len(planksFiles)):
    if x != y:
      createProperties(ctmFiles[x].split('_planks')[0], planksFiles[y].split('_planks')[0])
