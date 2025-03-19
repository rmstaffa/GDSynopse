call C:\ProgramData\Anaconda3\Scripts\activate.bat 
:: first activate general conda "console"
call conda activate quickFCnew
:: activate specific environment
call python program/fc_mfp_potential.py
:: run script
call conda deactivate
:: deactivate specific environment
exit