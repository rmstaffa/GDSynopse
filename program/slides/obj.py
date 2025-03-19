from dataclasses import dataclass
from pathlib import Path
import sys
BASE_DIR = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(BASE_DIR))
from setup import settings

header = f"Gemeinschaftsdiagnose {settings.settings['GD']} ({settings.settings['Gastgeber:in']})"

@dataclass
class SlideT1:
    
    title: str
    report: str
    header: str = header
    
    table1_title: str = "Verkettete Volumenangaben (ksb); Mrd. EUR"
    table2_title: str = "Q-Q laufende Rate"
    table3_title: str = "Jahresrate Ursprung"
    table4_title: str = "Jahresrate, ksb"
    table5_title: str = "Statistischer Überhang"
    table6_title: str = "Q4-Q4 Jahresverlaufsrate"
    
@dataclass
class SlideT2:
    
    title: str
    report: str
    header: str = header
    
    table1_title: str = "Level Werte"
    table2_title: str = "Veränderung in %"
    table3_title: str = "Absolute Veränderung"
    
@dataclass
class SlideT3:
    
    title: str
    report: str
    header: str = header
    
    table1_title: str = "Level Werte"
    table2_title: str = "Veränderung in %"
    table3_title: str = "Absolute Veränderung"
    
@dataclass
class SlideT4:
    
    title: str
    report: str
    header: str = header
    
