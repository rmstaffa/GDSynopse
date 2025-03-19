
from collections import namedtuple

AnnahmenTab = namedtuple("Annahmen",["title","series"])

annahmen_tab = [
    AnnahmenTab(
        title="Zinssatz der EZB für Hauptrefinanzierungsgeschäfte am Quartalsende %",
        series="QE1_ZINSK0"
    ),
    AnnahmenTab(
        title="Geldmarktsätze / EURIBOR Dreimonatsgeld / Monatsdurchschnitt % P.A.",
        series="QE1_ZINSK"
    ),
    AnnahmenTab(
        title="Euro area 10-year Government Benchmark bond yield - Yield Euro area",
        series="QE1_ZINSL"
    ),
    AnnahmenTab(
        title="USD/EUR Referenzkurs",
        series="QE1_WEKUD1"
    ),
    AnnahmenTab(
        title="Indikator der preislichen Wettbewerbsfähigkeit der d. Wirtschaft geg. 56 Handelspartnern",
        series="QGE_WEKUB56C"
    ),
    AnnahmenTab(
        title="Tarifverdienste, Gesamtwirtschaft, Monatsbasis, Deutschland 2020=100",
        series="QGE_TLGMAM_R"
    ),
    AnnahmenTab(
        title="Verbraucherpreisindex / Deutschland / Ursprungswerte",
        series="QGE_PCPL_R"
    ),
    AnnahmenTab(
        title="Harmonisierter Verbraucherpreisindex (HVPI)",
        series="QE1_PCPLH_r"
    ),
    AnnahmenTab(
        title="Europe Brent Spot Price FOB (Dollars per Barrel)",
        series="QW0_PEXOIL_BR"
    ),
    AnnahmenTab(
        title="Welt-Bruttoinlandsprodukt (% gg. Vorquartal, gewichtet mit den Anteilen an der deutschen Ausfuhr )",
        series="QW0_BIPDEX_ksqq"
    ),
    AnnahmenTab(
        title="Welthandel, Jahreswerte, Vorjahresvergleich in %",
        series="AW0_IM"
    ),
    AnnahmenTab(
        title="Welt-Bruttoinlandsprodukt, Jahreswerte, Vorjahresvergleich in %",
        series="AW0_BIPDEX"
    )
]

