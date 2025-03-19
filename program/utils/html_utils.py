#%% Packages

import asyncio
import nest_asyncio

from pyppeteer import launch

#%% Functions

nest_asyncio.apply()

async def html_to_pdf(input_path, output_path):
    # Launch Chrome in non-headless mode for debugging
    browser = await launch(
        executablePath="utils/chrlauncher-win64-stable-codecs-sync/bin/chrome.exe",
        headless=True
    )
    page = await browser.newPage()

    # Reveal.js `?print-pdf` mode
    reveal_url = f'file:///{input_path}?print-pdf'

    # Navigate to the URL
    await page.goto(reveal_url, {'waitUntil': 'networkidle0'})

    # Set viewport size to match Reveal.js dimensions
    await page.setViewport({
        "width": 1500,  # Match Reveal.js width
        "height": 700,  # Match Reveal.js height
        "deviceScaleFactor":1   # Scale factor (for high-DPI screens, use >1)
    })

    # Export the page to PDF
    await page.pdf({
        'path': output_path,
        'width': '1500px',  # Set PDF width to match Reveal.js
        'height': '700px',  # Set PDF height to match Reveal.js
        'printBackground': True,  # Preserve background colors
        'scale': 1,  # Ensure no additional scaling
        'landscape': True,  # Match Reveal.js slide orientation
        'margin': {
            'top': '0px',     # No margins
            'right': '0px',
            'bottom': '0px',
            'left': '0px'
        }
    })

    await browser.close()




