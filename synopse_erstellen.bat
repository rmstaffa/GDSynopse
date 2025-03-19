chcp 65001 > nul
set PYTHONUTF8=1
call C:\ProgramData\Anaconda3\Scripts\activate.bat 
:: first activate general conda "console"
call conda activate GDSynopse
:: activate specific environment
call python program/clean.py
call python program/kurzfrist.py
call python program/bws.py
call python program/mittelfrist.py
call python program/annahmen_new.py
:: run script
call conda deactivate
:: deactivate specific environment
exit