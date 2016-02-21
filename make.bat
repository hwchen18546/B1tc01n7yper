SET PWD=%cd%
cd /d %cd%\pyobfuscate
python pyobfuscate.py ..\B!tc01n7yper.py > ..\ObB!tc01n7yper.py

cd /d ..
python setup.py install
python setup.py py2exe

cd /d %cd%\dist
mkdir captcha
xcopy ..\log0 log /i
xcopy ..\img img /i
del ..\ObB!tc01n7yper.py
rd /s /q ..\build
rename ObB!tc01n7yper.exe B!tc01n7yper.exe
cd /d ..
rename dist exe
pause