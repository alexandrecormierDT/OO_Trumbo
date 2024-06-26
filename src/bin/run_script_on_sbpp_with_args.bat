set SBPMANAGER_VAR='%1'
set executable="C:/Program Files (x86)/Toon Boom Animation/Toon Boom Storyboard Pro 22/win64/bin/StoryboardPro.exe"
set project=%2
set script=%3

%executable% -scene %project% -batch -compile %script%

set RETRY="no"
IF %ERRORLEVEL%==-1073741819 SET RETRY="yes"
IF %ERRORLEVEL%==9009 SET RETRY="yes"
IF %ERRORLEVEL%==12 SET RETRY="yes"
IF %RETRY%=="yes" (
    %executable% -scene %project% -batch -compile %script%
)

set RETRY="no"
IF %ERRORLEVEL%==-1073741819 SET RETRY="yes"
IF %ERRORLEVEL%==9009 SET RETRY="yes"
IF %ERRORLEVEL%==12 SET RETRY="yes"
IF %RETRY%=="yes" (
    %executable% -scene %project% -batch -compile %script%
)

set RETRY="no"
IF %ERRORLEVEL%==-1073741819 SET RETRY="yes"
IF %ERRORLEVEL%==9009 SET RETRY="yes"
IF %ERRORLEVEL%==12 SET RETRY="yes"
IF %RETRY%=="yes" (
    %executable% -scene %project% -batch -compile %script%
)

set RETRY="no"
IF %ERRORLEVEL%==-1073741819 SET RETRY="yes"
IF %ERRORLEVEL%==9009 SET RETRY="yes"
IF %ERRORLEVEL%==12 SET RETRY="yes"
IF %RETRY%=="yes" (
    %executable% -scene %project% -batch -compile %script%
)

IF %ERRORLEVEL%==100 SET ERRORLEVEL=0
IF %ERRORLEVEL%==12 SET ERRORLEVEL=0
exit %ERRORLEVEL%