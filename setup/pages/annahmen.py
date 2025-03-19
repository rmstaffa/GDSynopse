
from collections import namedtuple

Annahmen = namedtuple("Annahmen",
                        ["title","title1","title2","series1","series2","axis_title1","axis_title2"])

annahmen = [Annahmen(
                title="Kurzfristzinsen Eurozone",
                title1="Kurzfristzinsen Eurozone, Euribor",
                title2="EZB-Leitzins",
                series1="QE1_ZINSK",
                series2="QE1_ZINSK0",
                axis_title1="in %",
                axis_title2="in % (Ende des Quartals)"),
            Annahmen(
                title="Kapitalmarktzinsen",
                title1="Kapitalmarktzinsen Eurozone-10-Jahr",
                title2="Deutschland 9-10-Jahre",
                series1="QE1_ZINSL",
                series2="QE1_ZINSL", 
                # series2="QGE_ZINSL1", NOTE: noch klären!
                axis_title1="in %",
                axis_title2="in %"),
            Annahmen(
                title="Wechselkurs, Wettbewerbsfähigkeit",
                title1="Wechselkurs",
                title2="Preisliche Wettbewerbsfähigkeit der. d. Wirtschaft (ggü 60 H.partner)",
                series1="QE1_WEKUD1",
                series2="QGE_WEKUB56C",
                axis_title1="USD/EUR",
                axis_title2="PW 60 H.partner (1999=100)"),
            Annahmen(
                title="Ölpreis, Tariflöhne",
                title1="Ölpreis",
                title2="Tariflöhne",
                series1="QW0_PEXOIL_BR",
                series2="QGE_TLGMAM_R",
                axis_title1="Brent in USD/Barrel",
                axis_title2="Tariflöhne in %"),
            Annahmen(
                title="Inflation (VPI, HVPI)",
                title1="Verbraucherpreisindex (VPI)",
                title2="Harmonisierter Verbraucherpreisindex (HVPI)",
                series1="QGE_PCPL_R",
                series2="QE1_PCPLH_r",
                axis_title1="Veränderung zum Vorjahresquartal, in %",
                axis_title2="Veränderung zum Vorjahresquartal, in %"),
            Annahmen(
                title="Welt-BIP und Welthandel",
                title1="Welt BIP, mit deutschen Exporten gewichtet",
                title2="Welthandel und Welt-BIP (ppp)",
                series1="AW0_BIPDEX",
                series2="AW0_IM",
                axis_title1="Veränderung zum Vorjahr, in %",
                axis_title2="Veränderung zum Vorjahr, in %"),
            ]

