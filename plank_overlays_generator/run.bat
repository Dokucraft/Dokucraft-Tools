@echo off
for %%i in (a\*.png) do for %%j in (b\*.png) do if NOT %%~ni == %%~nj (
  echo out\%%~nj\%%~nj_on_%%~ni
  md out\%%~nj\%%~nj_on_%%~ni
  magick %%i %%j -composite -compose CopyOpacity ^( +clone l.png -composite ^) ^( -clone 0 r.png -composite ^) "out\%%~nj\%%~nj_on_%%~ni\%%01d.png"
  echo matchBlocks=%%~ni_planks > out\%%~nj\%%~nj_on_%%~ni\%%~nj_on_%%~ni.properties
  echo method=overlay >> out\%%~nj\%%~nj_on_%%~ni\%%~nj_on_%%~ni.properties
  echo tiles=^<skip^> ^<skip^> ^<skip^> 0 1 2 1 2 0 1 2 1 2 0 ^<skip^> ^<skip^> ^<skip^> >> out\%%~nj\%%~nj_on_%%~ni\%%~nj_on_%%~ni.properties
  echo connect=block >> out\%%~nj\%%~nj_on_%%~ni\%%~nj_on_%%~ni.properties
  echo connectBlocks=%%~nj_planks >> out\%%~nj\%%~nj_on_%%~ni\%%~nj_on_%%~ni.properties
  echo layer=cutout >> out\%%~nj\%%~nj_on_%%~ni\%%~nj_on_%%~ni.properties
)
