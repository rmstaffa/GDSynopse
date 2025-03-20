#%% import packages

import sys
import io
import sys
import io

# core packages
import pandas as pd
import datetime as dt
import asyncio
import os
import re
from pathlib import Path

# third party
from jinja2 import Environment, FileSystemLoader
from loguru import logger

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
else:
    logger.warning("Warning: Running in an environment without sys.stdout.buffer. Skipping encoding override.")

# custom packages
from utils.synopse_data import SynopseData
from utils import utils,html_utils
from slides.obj import SlideT1, SlideT2

# import editable part
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
from setup import settings
from setup.pages.kurzfrist import verwendung, arbeitsmarkt


#%% Set up

# change directory to main file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# create logger file
logger.add("logging/logfile.log")
program = re.compile(r"([A-Za-z_]+)\.py").findall(__file__)[0]
logger.info(f"Starting program: '{program}.py'")

#%% load data

if settings.settings["produce_vintages"]:
    folder = "vintages"
else: 
    folder = "synopse"
    
path = str(BASE_DIR / f"_data_inputs/{folder}" ) + "/"

synopse = SynopseData(
    path = path 
)
synopse.load_data()

#%%

# Verwendungsaggregate
verwendung_graph_and_tables_list = []
for p in verwendung:
    logger.info(f"Creating page {p.title}")
    lst = utils.create_verwendung(p,synopse,settings)
    verwendung_graph_and_tables_list.append(lst)
    
arbeitsmarkt_graph_and_tables_list = []
for p in arbeitsmarkt:
    
    logger.info(f"Creating page {p.title}")
    lst = utils.create_arbeitsmarkt(p,synopse,settings)
    arbeitsmarkt_graph_and_tables_list.append(lst)
    

#%%

slides_t1 = []

for p in verwendung_graph_and_tables_list:
    
    slide = SlideT1(title=p[0], report="kurzfrist")
    slide.plot = p[1]
    slide.table1 = p[2][0]
    slide.table2 = p[2][1]
    slide.table3 = p[2][2]
    slide.table4 = p[2][3]
    slide.table5 = p[2][4]
    slide.table6 = p[2][5]
    
    slides_t1.append(slide)
    
slides_t2 = []
    
for p in arbeitsmarkt_graph_and_tables_list:
    
    slide = SlideT2(title=p[0], report="kurzfrist")
    slide.plot = p[1]
    slide.table1 = p[2][0]
    slide.table2 = p[2][1]
    slide.table3 = p[2][2]
    
    slides_t2.append(slide)
    
#%%

# Set up the Jinja environment
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('slide_template_kurzfrist.html')

# Render the template with the Pandas table and Plotly graphs
rendered_html = template.render(
    title=f"Gemeinschaftsdiagnose {settings.settings['GD']} ({settings.settings['Gastgeber:in']})",
    slides_t1=slides_t1,
    slides_t2=slides_t2,
)

# Save the output to an HTML file
with open(str(BASE_DIR)+f"/_reports_outputs/{folder}/{program}.html", 'w') as f:
    f.write(rendered_html)
    
logger.success("HTML slide with multiple slides has been generated.")


#%%

# Run the async function
input_path = str(BASE_DIR)+f"/_reports_outputs/{folder}/{program}.html"
output_path = str(BASE_DIR)+f"/_reports_outputs/{folder}/{program}.pdf"

try:
    asyncio.run(html_utils.html_to_pdf(
        input_path = input_path,
        output_path = output_path
    ))
except Exception as e:
    logger.warning(f"pypeteer error (likely non-fatal): {e}")

logger.success(f"PDF file created at: {output_path}")

# store csv
synopse.data_to_csv(csv_path=str(BASE_DIR)+f"/_reports_outputs/{folder}")
logger.success("CSV file created")
