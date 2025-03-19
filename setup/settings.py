import numpy as np
import datetime as dt
from collections import OrderedDict
import glob
import re
import plotly.colors as pc
from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))

settings_allgemein = {
    "title":"Synopse der Gemeinschaftsdiagnose",
    "fc_start":"2024-07", # erster monat des ersten Prognosequartals
    "GD":"Frühjahr 2025", # aktuelle GD
    "GD(t-1)":"Herbst 2024", # vorherige GD
    "Gastgeber:in":"Berlin", # gastgebendes Institut
    "tickformat":",.2f", # format for plots,
}

settings_synopse = {
    "show_mean":False, # Durchschnitt anzeigen in Tabellen
    "Prognose":True, # Prognose mit anzeigen (Excel mit Namen GD.xlsx)
    "prognose_style_line":dict(color="black",dash="dash", width=3), # style for the prognose line
    "prognose_style_marker":dict(color="white",pattern_shape="\\",line_color="black"), # style for the prognose marker
    # NOTE: adjust according to the institute names (excel file names)
    "colors":OrderedDict({
        "RWI":"blue",
        "DIW":"#00a799",
        "ifo":"red",
        "IfW":"yellow",
        "IWH":"darkviolet",
        "GD":"black",
    }),
}

settings_vintages = {
    "produce_vintages":True,
    "colorscale":"viridis_r", # colorscale for the vintages
}

settings_mfp = {
    "data_path_mittelfrist":str(BASE_DIR / "mfp") + "/MFP_Input.xlsx", # Pfad zur Mittelfristprognose Excel
    "window_kf":slice("2023","2026"), # window to be displayed (if data available)
    "window_mf":slice("2016","2029"), # window to be displayed (if data available)
}

# combine settings
settings = {**settings_allgemein,
            **settings_synopse,
            **settings_vintages,
            **settings_mfp}



# NOTE: don't change the following settings
settings["row_number"] = np.where(dt.date.today().year < np.arange(int(settings["window_mf"].start),int(settings["window_mf"].stop)))[0][0]

if settings["produce_vintages"]:
    
    # overwrite colors if necessary
    pat = re.compile(r"([A-Za-z0-9 _]+)\.xlsx")
    file_paths = glob.glob(str(BASE_DIR / "vintages") + "\*.xlsx")
    vintages = [pat.findall(f)[0] for f in file_paths]
    colors = pc.sample_colorscale(settings["colorscale"], [i / (len(vintages) - 1) for i in range(len(vintages))])
    
    colors = dict(zip(vintages,colors))
    
    settings["colors"] = colors
    settings["show_mean"] = False