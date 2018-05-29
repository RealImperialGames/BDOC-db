@echo off
SET NAME= Black Desert Online Community server
: Create docker machine to up mongodb database server
::bdodb-connect
TITLE %NAME%
REM COLOR C
set mod=%1
cd ..\data\docker\
docker-compose up