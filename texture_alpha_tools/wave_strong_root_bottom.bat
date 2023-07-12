@echo off
:loop
if "%~1"=="" goto continue
 magick mogrify -channel a -fx "j!=h-1?(a>0.5?252:19)/255:a>0.5" "%~1"
shift
goto loop
:continue