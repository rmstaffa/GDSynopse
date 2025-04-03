# Gemeinschaftsdiagnose Synopse Tool


## Set-Up

- install conda environment, when using anaconda you can use the Anaconda Prompt (Anaconda3) as follows

1. Start Anaconda Prompt (Anaconda3)
```
(base) C:\>
```
2. Navigate to the project folder (where GDSynopse.yml resides)
```
(base) C:\>cd "PFAD\ZU\PROJEKT"
```
3. Install conda environment
```
(base) C:\PFAD\ZU\PROJEKT\>conda env create -f GDSynopse.yml
```
... wait until fully installed (can take a while)

4. Download the chrome launcher (chrlauncher-win64-stable-codecs-sync)
- in case of doubt, reach out to repo owner and ask 
- must be installed and put in program/utils/

## Manual / Usage

There are three main use cases: 

> Produce Synopse Reports

- Associated batch file: 'synopse_erstellen.bat'
- **with averages**: 
  - exchange data files from institutes must be stored in _data_inputs/synopse
  - adjust settings in setup/settings.py (show_mean = True; Prognose = False)
- **without averages**: 
  - exchange data files from institutes must be stored in _data_inputs/synopse
  - adjust settings in setup/settings.py (show_mean = False; Prognose = False)
- **with forecast**: 
  - exchange data files from institutes must be stored in _data_inputs/synopse
  - forecast must be stored in same folder as 'GD.xlsx'
  - adjust settings in setup/settings.py (show_mean = False; Prognose = True)
- double-click on batch file and wait until program finishes
- results are available in _reports_outputs/synopse/

> Produce Comparison of Different Stages within Joint Forecast

- Associated batch file: 'vintages_erstellen.bat'
- Put files of different stages of the joint forecast in _data_inputs/vintages
- double-click on batch file and wait until program finishes
- results are available in _reports_outputs/vintages/

> Produce Comparison Sheet for Medium Term Forecast

- Associated batch file: 'mfp_erstellen.bat'
- Put file MFP_input.xlsx in folder _data_inputs/mfp (possibly change the name of the file in 'setup/setting.py')

```
settings_mfp = {
    "data_path_mittelfrist":str(BASE_DIR / "_data_inputs") + "/mfp/MFP_Input_3RR.xlsx", # Pfad zur Mittelfristprognose Excel
```

- double-click on batch file and wait until program finishes
- results are available in _reports_outputs/mfp

*Anmerkungen:*

* Reports will be produced as dynamic HTML slides and PDF files 

FAQ:

1. Wie kann eine neue Grafik hinzugefügt werden?
2. ...
