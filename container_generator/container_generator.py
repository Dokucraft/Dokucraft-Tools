from PIL import Image
from io import BytesIO
from os import getcwd
from base64 import b64decode

fileDir = getcwd()
fileDir = fileDir.replace('\\', '/')
fileDir = fileDir + '/'

# Define Images

backgroundImageData = b'iVBORw0KGgoAAAANSUhEUgAAABgAAAAYCAMAAADXqc3KAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAB+UExURf7+/fT18uLj4M/Qzr6/u7W3sqaonv39/CIiHQwMCxYWE3J0bPv79xoUDx8YE3N1bqSklyAgHB0WEikfGE1OSBUVElpcVCYdFzY2MTg4MzM1L1dYUScoJGJiW42Qhfr69RYWEmBhWvz8+RoaFpqalMXGw9zd2vLz8SMkHQAAAOVb8e0AAAAqdFJOU///////////////////////////////////////////////////////ADKo8FwAAAAJcEhZcwAADr8AAA6/ATgFUyQAAACDSURBVChT7dK5EsIwDARQcSZrsAkJIlwh3LD//4NgxsMYp6PmddJ20gpJ6fUHw1Fk7JdkliNhJj6Y5rDuG8yMUsxRVokSC5UlbB3mj9quVNbqwhhxPwWbfxBzW5Vd0z17ZfcqME33Ue0BQphj+trTGb4Mr+QS6uFdb/cH3i1h6EaE5BNlWimQMiLNWwAAAABJRU5ErkJggg=='
slotImageData = b'iVBORw0KGgoAAAANSUhEUgAAAAwAAAANBAMAAABvB5JxAAAAAXNSR0IArs4c6QAAAARnQU1BAACxjwv8YQUAAAAVUExURSkfGBENChwVESEZFBUQDCwhGjUoH3AIWiEAAAAJcEhZcwAADsEAAA7BAbiRa+0AAAAzSURBVBjTY2AQBAIGBkYlIBBgEDIGAkUGZxBlwqAMooyIoYJAlCoDG8iUBAaGtLS0NAYAJWINrxD23noAAAAASUVORK5CYII='

backgroundImage = Image.open(BytesIO(b64decode(backgroundImageData)))
slotImage = Image.open(BytesIO(b64decode(slotImageData)))

topLeftCornerImage = backgroundImage.crop((0, 0, 8, 8))
topRightCornerImage = backgroundImage.crop((16, 0, 24, 8))
bottomLeftCornerImage = backgroundImage.crop((0, 16, 8, 24))
bottomRightCornerImage = backgroundImage.crop((16, 16, 24, 24))

topImage = backgroundImage.crop((8, 0, 16, 8))
bottomImage = backgroundImage.crop((8, 16, 16, 24))
leftSideImage = backgroundImage.crop((0, 8, 8, 16))
rightSideImage = backgroundImage.crop((16, 8, 24, 16))

#topLeftCornerImage.save(fileDir + 'top_left.png')
#topRightCornerImage.save(fileDir + 'top_right.png')
#bottomLeftCornerImage.save(fileDir + 'bottom_left.png')
#bottomRightCornerImage.save(fileDir + 'bottom_right.png')
#topImage.save(fileDir + 'top.png')
#bottomImage.save(fileDir + 'bottom.png')
#leftSideImage.save(fileDir + 'left.png')
#rightSideImage.save(fileDir + 'right.png')

# Create Background Image

try:
  slotColumns = int(input('Number of Columns: '))
except ValueError:
  print('Input must be a Number')
try:
  slotRows = int(input('Number of Rows: '))
except ValueError:
  print('Input must be a Number')

backgroundSizeX = 20 + (slotColumns * 18) - 18
backgroundSizeY = 21 + (slotRows * 18) - 18

backgroundImageFull = Image.new('RGBA', (backgroundSizeX, backgroundSizeY), '#291F18')

for px in range(8, backgroundSizeX - 8, 8):
  backgroundImageFull.paste(topImage, (px, 0))
  backgroundImageFull.paste(bottomImage, (px, backgroundSizeY - 8))
  
for px in range(8, backgroundSizeY - 8, 8):
  backgroundImageFull.paste(leftSideImage, (0, px))
  backgroundImageFull.paste(rightSideImage, (backgroundSizeX - 8, px))

backgroundImageFull.paste(topLeftCornerImage, (0, 0))
backgroundImageFull.paste(topRightCornerImage, (backgroundSizeX - 8, 0))
backgroundImageFull.paste(bottomLeftCornerImage, (0, backgroundSizeY - 8))
backgroundImageFull.paste(bottomRightCornerImage, (backgroundSizeX - 8, backgroundSizeY - 8))

# backgroundImageFull.save(fileDir + 'background.png')

# Add Slots to the Background Image

backgroundImageSlots = backgroundImageFull.copy()

if slotColumns > 1:
  for px in range(4, backgroundSizeX, 18):
    if slotRows > 1:
      for py in range(4, backgroundSizeY, 18):
        backgroundImageSlots.paste(slotImage, (px, py))
    elif slotRows == 1:
      backgroundImageSlots.paste(slotImage, (px, 4))
    else:
      print('Invalid Number of Rows:', slotRows)
elif slotColumns == 1:
  if slotRows > 1:
    for py in range(4, backgroundSizeY, 18):
      backgroundImageSlots.paste(slotImage, (4, py))
  elif slotRows == 1:
    backgroundImageSlots.paste(slotImage, (4, 4))
  else:
    print('Invalid Number of Rows:', slotRows)
else:
  print('Invalid Number of Columns:', slotColumns)

backgroundImageSlots.save(fileDir + 'output.png')