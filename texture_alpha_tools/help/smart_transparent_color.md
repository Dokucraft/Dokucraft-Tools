## smart_transparent_color.bat
This changes the color of non-opaque pixels in image files dragged onto it so that the color is based on the colors of the opaque pixels in the image and the distance from those pixels. This fixes all issues with mipmaps becoming white or sometimes other unwanted colors.

## Requirements
- [NodeJS](https://nodejs.org/en)

## How to use
1. To use this tool, its dependencies must first be installed. To do this, open the `texture_alpha_tools/stc` folder in cmd or PowerShell and run this command: `npm i`
2. Once the dependencies are installed, the tool can be used by simply dragging image files onto `smart_transparent_color.bat`. It can handle any number of image files at once, so you can drag multiple files onto to process them all.
