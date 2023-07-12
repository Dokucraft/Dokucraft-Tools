@echo off
:loop
if "%~1"=="" goto continue
 magick mogrify -channel a -fx "(a>0.5?141:24)/255" "%~1"
shift
goto loop
:continue