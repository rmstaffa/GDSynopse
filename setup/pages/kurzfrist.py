from collections import namedtuple

Verwendung = namedtuple("Verwendung",
                        ["title","quarterly_series","annual_series"])
Arbeitsmarkt = namedtuple("Arbeitsmarkt",
                        ["title","series","axis_title"])

# -- Verwendungsaggregate
verwendung = [
    Verwendung(
        title = "Reales Bruttoinlandsprodukt",
        quarterly_series = "QGE_BIP_V_A",
        annual_series = "AGE_BIP_V_X"),
    Verwendung(
        title = "Reale Private Konsumausgaben",
        quarterly_series = "QGE_CP_V_A",
        annual_series = "AGE_CP_V_X"),
    Verwendung(
        title = "Reale Konsumausgaben des Staates",
        quarterly_series = "QGE_CST_V_A",
        annual_series = "AGE_CST_V_X"),
    Verwendung(
        title = "Reale Ausrüstungsinvestitionen",
        quarterly_series = "QGE_IAU_V_A",
        annual_series = "AGE_IAU_V_X"),
    Verwendung(
        title = "Reale Bauinvestitionen",
        quarterly_series = "QGE_IB_V_A",
        annual_series = "AGE_IB_V_X"),
    Verwendung(
        title = "Reale Wohnungsbauinvestitionen",
        quarterly_series = "QGE_IBWO_V_A",
        annual_series = "AGE_IBWO_V_X"),
    Verwendung(
        title = "Reale Investitionen im gewerbl. Nichtwohnungsbau",
        quarterly_series = "QGE_IBGE_V_A",
        annual_series = "AGE_IBGE_V_X"),
    Verwendung(
        title = "Reale Sonstige Anlageinvestitionen",
        quarterly_series = "QGE_ISO_V_A",
        annual_series = "AGE_ISO_V_X"),
    Verwendung(
        title = "Reale Exporte",
        quarterly_series = "QGE_EX_V_A",
        annual_series = "AGE_EX_V_X"),
    Verwendung(
        title = "Reale Warenexporte",
        quarterly_series = "QGE_EXW_V_A",
        annual_series = "AGE_EXW_V_X"),
    Verwendung(
        title = "Reale Dienstleistungsexporte",
        quarterly_series = "QGE_EXD_V_A",
        annual_series = "AGE_EXD_V_X"),
    Verwendung(
        title = "Reale Importe",
        quarterly_series = "QGE_IM_V_A",
        annual_series = "AGE_IM_V_X"),
    Verwendung(
        title = "Reale Warenimporte",
        quarterly_series = "QGE_IMW_V_A",
        annual_series = "AGE_IMW_V_X"),
    Verwendung(
        title = "Reale Dienstleistungsimporte",
        quarterly_series = "QGE_IMD_V_A",
        annual_series = "AGE_IMD_V_X"),
]

arbeitsmarkt = [
    Arbeitsmarkt(
        title = "Erwerbstätige",
        series = "AGE_EW_X_X",
        axis_title = "in 1000 Personen"),
    Arbeitsmarkt(
        title = "Arbeitsvolumen",
        series = "AGE_AV_X_X",
        axis_title = "in Millionen Stunden"),
    Arbeitsmarkt(
        title = "Arbeitslose",
        series = "AGE_ALB_X_X",
        axis_title = "in 1000 Personen"),
    Arbeitsmarkt(
        title = "Bruttolöhne und -gehälter",
        series = "AGE_BLGL_C_X",
        axis_title = "in Mrd. Euro"),
    Arbeitsmarkt(
        title = "Reale Stundenproduktivität",
        series = "AGE_PRODH_X_X",
        axis_title = "in Eur pro Stunde"),
]