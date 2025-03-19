
from collections import namedtuple

AnnahmenTab = namedtuple("Annahmen",["title","series","axis_title"])

annahmen_new = [
    AnnahmenTab(
        title="Zinssatz der EZB für Hauptrefinanzierungsgeschäfte am Quartalsende %",
        series="QE1_ZINSK0",
        axis_title="in % (Ende des Quartals)",
    ),
    AnnahmenTab(
        title="Geldmarktsätze / EURIBOR Dreimonatsgeld / Monatsdurchschnitt % P.A.",
        series="QE1_ZINSK",
        axis_title="in %",
    ),
    AnnahmenTab(
        title="Euro area 10-year Government Benchmark bond yield - Yield Euro area",
        series="QE1_ZINSL",
        axis_title="in %",
    ),
    AnnahmenTab(
        title="Deutschland 9-10-Jahre Area",
        series="QGE_ZINSL1",
        axis_title="in %",
    ),
    # AnnahmenTab(
    #     title="USD/EUR Referenzkurs",
    #     series="QE1_WEKUD1",
    #     axis_title="USD/EUR",
    # ),
    AnnahmenTab(
        title="Indikator der preislichen Wettbewerbsfähigkeit der d. Wirtschaft geg. 56 Handelspartnern",
        series="QGE_WEKUB56C",
        axis_title="PW 56 H.partner (1999=100)",
    ),
    AnnahmenTab(
        title="Tarifverdienste, Gesamtwirtschaft, Monatsbasis, Deutschland 2020=100",
        series="QGE_TLGMAM_R",
        axis_title="Tariflöhne in %",
    ),
    AnnahmenTab(
        title="Verbraucherpreisindex / Deutschland / Ursprungswerte",
        series="QGE_PCPL_R",
        axis_title="Veränderung zum Vorjahresquartal, in %",
    ),
    AnnahmenTab(
        title="Harmonisierter Verbraucherpreisindex (HVPI)",
        series="QE1_PCPLH_r",
        axis_title="Veränderung zum Vorjahresquartal, in %",
    ),
    AnnahmenTab(
        title="Europe Brent Spot Price FOB (Dollars per Barrel)",
        series="QW0_PEXOIL_BR",
        axis_title="Brent in USD/Barrel",
    ),
    AnnahmenTab(
        title="Welt-Bruttoinlandsprodukt (% gg. Vorquartal, gewichtet mit den Anteilen an der deutschen Ausfuhr )",
        series="QW0_BIPDEX_ksqq",
        axis_title="Veränderung zum Vorjahr, in %",
    ),
    AnnahmenTab(
        title="Welthandel, Jahreswerte, Vorjahresvergleich in %",
        series="AW0_IM",
        axis_title="Veränderung zum Vorjahr, in %",
    ),
    AnnahmenTab(
        title="Welt-Bruttoinlandsprodukt, Jahreswerte, Vorjahresvergleich in %",
        series="AW0_BIPDEX",
        axis_title="Veränderung zum Vorjahr, in %",
    )
]

