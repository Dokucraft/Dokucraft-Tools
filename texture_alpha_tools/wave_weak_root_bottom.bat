@echo off
:loop
if "%~1"=="" goto continue
magick mogrify -alpha on -channel a -fx "j!=h-1?(a>0.5?254:20)/255:a>0.5" "%~1"
shift
goto loop
:continue
