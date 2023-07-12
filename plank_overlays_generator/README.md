# Plank overlays generator
This tool generates the CTM overlays for planks next to other types of planks.

## Requirements
- [Python 3.10+](https://www.python.org/)
- [Pillow](https://pypi.org/project/Pillow/)

## How to use
1. Replace the files in `in/planks` with planks from the `block` folder.
2. Replace the files in `in/ctm` with the center horizontal CTM texture (`1.png`) from the `optifine/ctm/planks` folders with one for each type of wood.
3. Run `py run.py` in this folder.
4. The output ends up in the `out` folder.
