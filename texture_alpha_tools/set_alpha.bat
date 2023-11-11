@echo off
set /p "oalpha=Opaque alpha value: "
set /p "talpha=Transparent alpha value: "
:loop
if "%~1"=="" goto continue
magick mogrify -alpha on -channel a -fx "(a>0.5?%oalpha%:%talpha%)/255" "%~1"
shift
goto loop
:continue
