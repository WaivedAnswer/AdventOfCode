@Echo off
SET /p number="Enter Number:"
SET newDirectory=Day_%number%
if not exist %newDirectory% mkdir %newDirectory%

SET inputFile=%newDirectory%\Input.txt
echo %inputFile%
start notepad++ %inputFile%

SET programFile=%newDirectory%\Program.py
echo %programFile%
start notepad++ %programFile%

start chrome "http://adventofcode.com/2015/day/%number%" "http://adventofcode.com/2015/day/%number%/input"

start cmd /k "cd %newDirectory%"

cp Common.py %newDirectory%
pause
