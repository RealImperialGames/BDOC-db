@echo off
SET NAME=ImperialGames Black Desert Online server
SET HOST=192.168.99.100:27018/admin
SET USR=root
SET PWD=1bdo@admin.2
: Connect portable client to MongoDB started database server
::bdodb-connect
TITLE %NAME%
REM COLOR C
set mod=%1
..\data\client\mongo.exe %HOST% -u %USR% -p %PWD%