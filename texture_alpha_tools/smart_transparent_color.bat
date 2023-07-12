@echo off
SET "ddp=%~dp0"
SET "ddp=%ddp:~0,-1%"
:loop
if "%~1"=="" goto continue
 echo %~1
 node "%ddp%/stc/smart_transparent_color.mjs" "%~1"
shift
goto loop
:continue
