# Texture alpha tools
This is a set of simple tools for manipulating the alpha channel of textures.

A lot of things change depending on the alpha value in a texture and the color value of transparent parts in a texture.
- Mipmaps often look wrong if the color values of the transparent pixels in the texture are very different from the colors of the opaque parts. This is due to the color values of the transparent pixels bleeding into the rest of the texture when it is scaled down. The main thing causing this problem is textures being scaled down, so keep this in mind when working on textures that the game might scale down in certain cases.
- The alpha values in textures are often used by the shaders in the resource pack to apply special effects. For example, setting the alpha values of the corner pixels in a texture to 18 or 253 will make a block using that texture wave, as if the wind was pushing it around slightly.
- Having semi-transparent pixels in item textures is bad because it causes the opaque pixels next to the semi-transparent ones to not be 3D when the item is held or on the ground. The pixels should always be fully transparent or fully opaque in textures for items using the `item/generated` model.

## List of alpha tools
| Tool | Description |
|-|-|
| 1-bit_alpha.bat | Forces the alpha of files dragged onto it to be 1-bit, i.e. either fully transparent or fully opaque. This can be used to remove shader effects from textures, or to fix item textures. |
| enable_swinging.bat | Sets the alpha values of all pixels of files dragged onto it to either 24 or 141, deending on if the old value was mostly transparent or mostly opaque. These specific values are used by the shaders in the pack to make the lanterns swing. |
| set_alpha.bat | Sets the alpha values of all pixels of files dragged onto it to a specific value. The tool will ask for two values, an opaque alpha value and a transparent one. The opaque value will be used for any pixels that have more than 50% opacity in the original image, and the transparent one will be used for any pixels with less than 50% opacity. The values should be in the range 0-255. |
| smart_transparent_color.bat | This changes the color of non-opaque pixels in image files dragged onto it so that the color is based on the colors of the opaque pixels in the image and the distance from those pixels. This fixes all issues with mipmaps becoming white or sometimes other unwanted colors. Check out [the help page for this tool](help/smart_transparent_color.md) for more information. |
| wave_medium.bat | Sets the alpha values of all pixels of files dragged onto it to either 18 or 253, depending on if the old value was mostly transparent or mostly opaque. The shaders in the pack will detect corner pixels with these values and enable medium strength waving for blocks with them. |
| wave_medium_root_bottom.bat | Same as wave_medium.bat, but leaves the bottom row of pixels intact, causing the shaders to not move the bottom of the block. |
| wave_medium_root_top.bat | Same as wave_medium.bat, but leaves the top row of pixels intact, causing the shaders to not move the top of the block. |
| wave_strong.bat | Sets the alpha values of all pixels of files dragged onto it to either 19 or 252, depending on if the old value was mostly transparent or mostly opaque. The shaders in the pack will detect corner pixels with these values and enable strong waving for blocks with them. |
| wave_strong_root_bottom.bat | Same as wave_strong.bat, but leaves the bottom row of pixels intact, causing the shaders to not move the bottom of the block. |
| wave_strong_root_top.bat | Same as wave_strong.bat, but leaves the top row of pixels intact, causing the shaders to not move the top of the block. |
| wave_weak.bat | Sets the alpha values of all pixels of files dragged onto it to either 20 or 254, depending on if the old value was mostly transparent or mostly opaque. The shaders in the pack will detect corner pixels with these values and enable weak waving for blocks with them. |
| wave_weak_root_bottom.bat | Same as wave_weak.bat, but leaves the bottom row of pixels intact, causing the shaders to not move the bottom of the block. |
| wave_weak_root_top.bat | Same as wave_weak.bat, but leaves the top row of pixels intact, causing the shaders to not move the top of the block. |
