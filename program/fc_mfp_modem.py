#%% import packages

# core packages
import pandas as pd
import re
import numpy as np
import datetime as dt
import asyncio
import os
import io

# third party
from jinja2 import Environment, FileSystemLoader
import nest_asyncio
from pyppeteer import launch
from loguru import logger

# custom packages
import sys
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE_DIR))
from setup import settings
from setup.pages.fc_mfp_modem import mfp_pot
from utils import synopse_data_mf, utils, html_utils
from slides.obj import SlideT1

if hasattr(sys.stdout, 'buffer'):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')
else:
    logger.warning("Warning: Running in an environment without sys.stdout.buffer. Skipping encoding override.")

#%% Set up

# change directory to main file
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# create logger file
logger.add("logging/logfile.log")
program = re.compile(r"([A-Za-z_]+)\.py").findall(__file__)[0]
logger.info(f"Starting program: '{program}.py'")

# get absolute path to main file
abspath = "/".join(os.path.abspath(__file__).split("\\")[:-2]) + "/"
logger.info(f"{abspath}")

#%% load data

synopse = synopse_data_mf.SynopseData(
    path = settings.settings["data_path_mittelfrist"]
)
synopse.load_data()

#%%
import copy
mfp_pot_graph_and_tables_list = []

for p in mfp_pot:
    
    logger.info(f"Creating page {p.title}")
    lst = utils.create_mfp_pot(copy.deepcopy(p),synopse,settings)
    mfp_pot_graph_and_tables_list.append(lst)
    
slides_t1 = []

for p in mfp_pot_graph_and_tables_list:
    
    slide = SlideT1(title=p[0], report="mittelfrist")
    slide.plot = p[1]
    slide.table1 = p[2][0]
    slide.table1_title = f"{p[0].title1} ({p[0].yaxis_title1})"
    slide.table2 = p[2][1]
    slide.table2_title = f"{p[0].title2} ({p[0].yaxis_title2})"
    slides_t1.append(slide)
    
#%%
    
    
# Set up Jinja2 environment
env = Environment(loader=FileSystemLoader('templates'))
# template = env.get_template('templ_mfp_pot.html')
template = env.get_template('slide_template_mittelfrist.html')

# Render the template with the Pandas table and Plotly graphs
rendered_html = template.render(
    title=f"Gemeinschaftsdiagnose {settings.settings['GD']} ({settings.settings['Gastgeber:in']})",
    slides_t1=slides_t1,
    slides_t2=[],
    row_number=settings.settings["row_number"],

)

# Save the output to an HTML file
with open(str(BASE_DIR)+f"/_reports_outputs/mfp/{program}.html", 'w') as f:
    f.write(rendered_html)
    
logger.success("HTML slide with multiple slides has been generated.")

#%%

# Run the async function
input_path = str(BASE_DIR)+f"/_reports_outputs/mfp/{program}.html"
output_path = str(BASE_DIR)+f"/_reports_outputs/mfp/{program}.pdf"

try:
    asyncio.run(html_utils.html_to_pdf(
        input_path = input_path,
        output_path = output_path
    ))
except Exception as e:
    logger.warning(f"pypeteer error (likely non-fatal): {e}")

logger.success(f"PDF file created at: {output_path}")


