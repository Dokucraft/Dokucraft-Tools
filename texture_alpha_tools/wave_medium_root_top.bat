@echo off
:loop
if "%~1"=="" goto continue
 magick mogrify -channel a -fx "(j%%w)!=0?(a>0.5?253:18)/255:a>0.5" "%~1"
shift
goto loop
:continue