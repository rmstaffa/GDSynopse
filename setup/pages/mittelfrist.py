
from collections import OrderedDict, namedtuple

Mittelfrist = namedtuple("Mittelfrist", ["title", "yaxis1", "yaxis2", "annual_series"])

mittelfrist = [
    Mittelfrist(
        title = "Bevölkerung in erwerbsfähigem Alter (15-74)",
        yaxis1 = "1000 Personen",
        yaxis2 = "Veränderung rel. VJ in %",
        annual_series = "AGE_POPW_C_X"
    ),
    Mittelfrist(
        title = "Produktionspotenzial (MODEM)",
        yaxis1 = "in Mrd. Euro",
        yaxis2 = "Veränderung rel. VJ in %",
        annual_series = "AGE_YPOT_C_X"
    ),
    Mittelfrist(
        title = "BIP",
        yaxis1 = "in Mrd. Euro",
        yaxis2 = "Veränderung rel. VJ in %",
        annual_series = "AGE_BIP_V_X"
    ),
    Mittelfrist(
        title = "Produktionslücke (MODEM)",
        yaxis1 = "in % des Potenzials",
        yaxis2 = "in Mrd. Euro",
        annual_series = "AGE_YGAP"
    ),
    Mittelfrist(
        title = "NAWRU Erwerbslosenquote",
        yaxis1 = "in %",
        yaxis2 = "Veränderung re. VJ in PP",
        annual_series = "AGE_NAWRU"
    ),
    Mittelfrist(
        title = "Arbeitsstunden (Trend)",
        yaxis1 = "in Stunden",
        yaxis2 = "Veränderung rel. VJ in %",
        annual_series = "AGE_HOURST_C_X"
    ),
    Mittelfrist(
        title = "Partizipationsquote",
        yaxis1 = "in %",
        yaxis2 = "Veränderung re. VJ in PP",
        annual_series = "AGE_PARTS_C_X"
    ),
    Mittelfrist(
        title = "Erwerbspersonen",
        yaxis1 = "1000 Personen",
        yaxis2 = "Veränderung rel. VJ in %",
        annual_series = "AGE_EWP_C_X"
    ),
    Mittelfrist(
        title = "Totale Faktorproduktivität (TFP)",
        yaxis1 = "in %",
        yaxis2 = "Vorjahresvergleich in %",
        annual_series = "AGE_SRT_C_X"
    ),
    Mittelfrist(
        title = "Terms of Trade",
        yaxis1 = "Index",
        yaxis2 = "Veränderung rel. VJ in %",
        annual_series = "AGE_TERMTRADE"
    ),
] 

