# Container Generator
This tool converts Optifine CTM to Fusion CTM.
Currently only Supports `ctm_compact` with tiles `0-4` and `ctm` with tiles `0-46`

## How to use Script

### Requirements
- [Python 3.10+](https://www.python.org/)
- [Pillow](https://pypi.org/project/Pillow/)

1. Place Optifine CTM Files inside of the `in` folder with the Path being either `in/CTM_NAME/Variant/Block.properties` or `in/CTM_NAME/Block.properties`)
2. Run `py optifine_to_fusion.py`.
3. The output ends up in `out`.