from collections import namedtuple

Halbjahre = namedtuple("Halbjahre",["title","quarterly_series","annual_series","yaxis","page","page_title","tickformat","scaling"])

halbjahre_p1 = [
    Halbjahre(
        title = "Erwerbstätige im Inland",
        quarterly_series = "SGE_EW",
        annual_series = "AGE_EW",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Arbeitslose (BA) Differenz in 1000",
        quarterly_series = "SGE_ALB",
        annual_series = "AGE_ALB",
        yaxis = "Differenz in 1000 Personen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.0f",
        scaling = None
    ),
    Halbjahre(
        title = "Arbeitszeit je Erwerbstätige",
        quarterly_series = "SGE_WTEMPL",
        annual_series = "AGE_WTEMPL",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Arbeitsvolumen, geleistet (Mill.Std)",
        quarterly_series = "SGE_AV",
        annual_series = "AGE_AV",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Produktivität (EUR/Std)",
        quarterly_series = "SGE_PRODH",
        annual_series = "AGE_PRODH",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttoinlands-produkt, preisbereinigt",
        quarterly_series = "SGE_BIP_9",
        annual_series = "AGE_BIP_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    )
]

halbjahre_p2 = [
    Halbjahre(
        title = "Erwerbstätige im Inland",
        quarterly_series = "SGE_EW",
        annual_series = "AGE_EW",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = ",.0f",
        scaling = None
    ),
    Halbjahre(
        title = "Arbeitslose (BA) in 1000",
        quarterly_series = "SGE_ALB",
        annual_series = "AGE_ALB",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.0f",
        scaling = None
    ),
    Halbjahre(
        title = "Arbeitszeit je Erwerbstätige",
        quarterly_series = "SGE_WTEMPL",
        annual_series = "AGE_WTEMPL",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = ",.0f",
        scaling = None
    ),
    Halbjahre(
        title = "Arbeitsvolumen, geleistet (Mill.Std)",
        quarterly_series = "SGE_AV",
        annual_series = "AGE_AV",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = ",.0f",
        scaling = None
    ),
    Halbjahre(
        title = "Produktivität (EUR/Std)",
        quarterly_series = "SGE_PRODH",
        annual_series = "AGE_PRODH",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttoinlands-produkt, preisbereinigt",
        quarterly_series = "SGE_BIP_9",
        annual_series = "AGE_BIP_9",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Saldo Primäreinkommen übrige Welt nominal",
        quarterly_series = "SGE_YEXIM",
        annual_series = "AGE_YEXIM",
        yaxis = "Absolute Zahlen",
        page = 1,
        page_title = "Entstehung des Inlandsprodukts",
        tickformat = "0.2f",
        scaling = None
    )
]

halbjahre_p3 = [
    Halbjahre(
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP",
        annual_series = "AGE_CP",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST",
        annual_series = "AGE_CST",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU",
        annual_series = "AGE_IAU",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Bauten",
        quarterly_series = "SGE_IB",
        annual_series = "AGE_IB",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Vorratsveränderung",
        quarterly_series = "SGE_IL",
        annual_series = "AGE_IL",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI",
        annual_series = "AGE_NI",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Außenbeitrag",
        quarterly_series = "SGE_EXIM",
        annual_series = "AGE_EXIM",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Exporte",
        quarterly_series = "SGE_EX",
        annual_series = "AGE_EX",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Importe",
        quarterly_series = "SGE_IM",
        annual_series = "AGE_IM",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Brutto-inlandsprodukt",
        quarterly_series = "SGE_BIP",
        annual_series = "AGE_BIP",
        yaxis = "in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p4 = [
    Halbjahre(
        title = "Private Konsum-ausgaben",
        quarterly_series = "SGE_CP",
        annual_series = "AGE_CP",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST",
        annual_series = "AGE_CST",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU",
        annual_series = "AGE_IAU",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bauten",
        quarterly_series = "SGE_IB",
        annual_series = "AGE_IB",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Vorratsveränderung Absoluter Unterschied in Mrd. EUR",
        quarterly_series = "SGE_IL",
        annual_series = "AGE_IL",
        yaxis = "Differenz",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI",
        annual_series = "AGE_NI",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Außenbeitrag Absoluter Unterschied in Mrd. EUR",
        quarterly_series = "SGE_EXIM",
        annual_series = "AGE_EXIM",
        yaxis = "Differenz",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Exporte",
        quarterly_series = "SGE_EX",
        annual_series = "AGE_EX",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Importe",
        quarterly_series = "SGE_IM",
        annual_series = "AGE_IM",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Brutto-inlandsprodukt",
        quarterly_series = "SGE_BIP",
        annual_series = "AGE_BIP",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p5 = [
    Halbjahre(
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP_9",
        annual_series = "AGE_CP_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST_9",
        annual_series = "AGE_CST_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttoanlage-investitionen",
        quarterly_series = "SGE_IAN_9",
        annual_series = "AGE_IAN_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_9",
        annual_series = "AGE_IAU_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Bauten",
        quarterly_series = "SGE_IB_9",
        annual_series = "AGE_IB_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_9",
        annual_series = "AGE_ISO_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI_9",
        annual_series = "AGE_NI_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Exporte",
        quarterly_series = "SGE_EX_9",
        annual_series = "AGE_EX_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Importe",
        quarterly_series = "SGE_IM_9",
        annual_series = "AGE_IM_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Brutto-inlandsprodukt",
        quarterly_series = "SGE_BIP_9",
        annual_series = "AGE_BIP_9",
        yaxis = "Verkettete Volumina in Mrd. Euro",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p6 = [
    Halbjahre(
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP_9",
        annual_series = "AGE_CP_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST_9",
        annual_series = "AGE_CST_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttoanlageinvestitionen",
        quarterly_series = "SGE_IAN_9",
        annual_series = "AGE_IAN_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_9",
        annual_series = "AGE_IAU_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bauten",
        quarterly_series = "SGE_IB_9",
        annual_series = "AGE_IB_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_9",
        annual_series = "AGE_ISO_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI_9",
        annual_series = "AGE_NI_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Exporte",
        quarterly_series = "SGE_EX_9",
        annual_series = "AGE_EX_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Importe",
        quarterly_series = "SGE_IM_9",
        annual_series = "AGE_IM_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttoinlandsprodukt",
        quarterly_series = "SGE_BIP_9",
        annual_series = "AGE_BIP_9",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p7 = [
    Halbjahre(
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP_P15",
        annual_series = "AGE_CP_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST_P15",
        annual_series = "AGE_CST_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_P15",
        annual_series = "AGE_IAU_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Bauten",
        quarterly_series = "SGE_IB_P15",
        annual_series = "AGE_IB_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI_P15",
        annual_series = "AGE_NI_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Terms of Trade",
        quarterly_series = "SGE_TT",
        annual_series = "AGE_TT",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Exporte",
        quarterly_series = "SGE_EX_P15",
        annual_series = "AGE_EX_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Importe",
        quarterly_series = "SGE_IM_P15",
        annual_series = "AGE_IM_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre(
        title = "Bruttoinlandsprodukt",
        quarterly_series = "SGE_BIP_P15",
        annual_series = "AGE_BIP_P15",
        yaxis = "2015=100",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
]

halbjahre_p8 = [
    Halbjahre(
        title = "Verbraucher-preisindex (Inflation VPI/CPI)",
        quarterly_series = "SGE_PCPL_R",
        annual_series = "AGE_PCPL_R",
        yaxis = "Vergleich zum Vorjahr in %", # should not trigger Vorjahresvergleich <> change within function because already in changes
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP_P15",
        annual_series = "AGE_CP_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST_P15",
        annual_series = "AGE_CST_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_P15",
        annual_series = "AGE_IAU_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bauten",
        quarterly_series = "SGE_IB_P15",
        annual_series = "AGE_IB_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI_P15",
        annual_series = "AGE_NI_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Terms of Trade",
        quarterly_series = "SGE_TT",
        annual_series = "AGE_TT",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Exporte",
        quarterly_series = "SGE_EX_P15",
        annual_series = "AGE_EX_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Importe",
        quarterly_series = "SGE_IM_P15",
        annual_series = "AGE_IM_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Brutto-inlandsprodukt",
        quarterly_series = "SGE_BIP_P15",
        annual_series = "AGE_BIP_P15",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verwendung des Inlandsprodukts: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
]
    
halbjahre_p9 = [
    Halbjahre(
        title = "Bruttonationaleinkommen",
        quarterly_series = "SGE_BNEK",
        annual_series = "AGE_BNEK",
        yaxis = "Mrd.EUR", # 
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Abschreibungen",
        quarterly_series = "SGE_AB",
        annual_series = "AGE_AB",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Nettonationaleinkommen",
        quarterly_series = "SGE_NNEK",
        annual_series = "AGE_NNEK",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    # Primäreinkommen der privaten Haushalte
    # 861: SGE_SVGAG + SGE_BLGL
    # 1047: 
    # -- sge_verfek - SGE_GVT + SGE_TYTLMS - sge_nlg - SGE_YTLMSEPH
    # Nettolöhne- und Gehälter
    Halbjahre(
        title = "Primäreinkommen der privaten Haushalte",
        quarterly_series = "SGE_PEKPHH",
        annual_series = "AGE_PEKPHH",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Primäreinkommen der übrigen Sektoren",
        quarterly_series = "SGE_PEKUSEK",
        annual_series = "AGE_PEKUSEK",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Produktions und Importabgaben ./. Subventionen",
        quarterly_series = "SGE_TINDMSUB",
        annual_series = "AGE_TINDMSUB",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Volkseinkommen",
        quarterly_series = "SGE_VEK",
        annual_series = "AGE_VEK",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Unternehmens und Vermögenseinkommen",
        quarterly_series = "SGE_UVEK",
        annual_series = "AGE_UVEK",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( # =(N931/N1255)/(N111/N71)*100
        title = "Lohnstückkosten",
        quarterly_series = "SGE_LUCOST",
        annual_series = "AGE_LUCOST",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = 100
    ), 
    Halbjahre(
        title = "Lohnstückkosten auf Stundenbasis",
        quarterly_series = "SGE_LUCOSTSTD",
        annual_series = "AGE_LUCOSTSTD",
        yaxis = "Mrd.EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = 100
    ),
]

halbjahre_p10 = [
    Halbjahre(
        title = "Bruttonationaleinkommen",
        quarterly_series = "SGE_BNEK",
        annual_series = "AGE_BNEK",
        yaxis = "Vorjahresvergleich in %", # 
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Abschreibungen",
        quarterly_series = "SGE_AB",
        annual_series = "AGE_AB",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Nettonationaleinkommen",
        quarterly_series = "SGE_NNEK",
        annual_series = "AGE_NNEK",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Primäreinkommen der privaten Haushalte",
        quarterly_series = "SGE_PEKPHH",
        annual_series = "AGE_PEKPHH",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Primäreinkommen der übrigen Sektoren",
        quarterly_series = "SGE_PEKUSEK",
        annual_series = "AGE_PEKUSEK",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Produktions und Importabgaben ./. Subventionen",
        quarterly_series = "SGE_TINDMSUB",
        annual_series = "AGE_TINDMSUB",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Volkseinkommen",
        quarterly_series = "SGE_VEK",
        annual_series = "AGE_VEK",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Unternehmens und Vermögenseinkommen",
        quarterly_series = "SGE_UVEK",
        annual_series = "AGE_UVEK",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Lohnstückkosten",
        quarterly_series = "SGE_LUCOST",
        annual_series = "AGE_LUCOST",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ), 
    Halbjahre(
        title = "Lohnstückkosten auf Stundenbasis",
        quarterly_series = "SGE_LUCOSTSTD",
        annual_series = "AGE_LUCOSTSTD",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p11 = [
    Halbjahre(
        title = "Arbeitnehmerentgelt",
        quarterly_series = "SGE_ANEG",
        annual_series = "AGE_ANEG",
        yaxis = "Mrd. EUR", # 
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Sozialbeiträge der Arbeitgeber",
        quarterly_series = "SGE_SVGAG",
        annual_series = "AGE_SVGAG",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttolöhne und -gehälter",
        quarterly_series = "SGE_BLGL",
        annual_series = "AGE_BLGL",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Abzüge",
        quarterly_series = "SGE_ABZUEGE",
        annual_series = "AGE_ABZUEGE",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Sozialbeiträge der Arbeitnehmer",
        quarterly_series = "SGE_SVGAN",
        annual_series = "AGE_SVGAN",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Lohnsteuer",
        quarterly_series = "SGE_TAN",
        annual_series = "AGE_TAN",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Nettolöhne und -gehälter",
        quarterly_series = "SGE_NLG",
        annual_series = "AGE_NLG",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre(
        title = "Saldo",
        quarterly_series = "SGE_SALDO",
        annual_series = "AGE_SALDO",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Arbeitnehmerentgelt im Inland",
        quarterly_series = "SGE_BYAN",
        annual_series = "AGE_BYAN",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = None
    ), 
    Halbjahre( # =byan/ava/bip_p15
        title = "Reale Arbeitskosten je Stunde",
        quarterly_series = "SGE_RAK",
        annual_series = "AGE_RAK",
        yaxis = "Mrd. EUR",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.2f",
        scaling = 1000
    ),
]

halbjahre_p12 = [
    Halbjahre(
        title = "Arbeitnehmerentgelt",
        quarterly_series = "SGE_ANEG",
        annual_series = "AGE_ANEG",
        yaxis = "Vorjahresvergleich in %", # 
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Sozialbeiträge der Arbeitgeber",
        quarterly_series = "SGE_SVGAG",
        annual_series = "AGE_SVGAG",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Bruttolöhne und -gehälter",
        quarterly_series = "SGE_BLGL",
        annual_series = "AGE_BLGL",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Abzüge",
        quarterly_series = "SGE_ABZUEGE",
        annual_series = "AGE_ABZUEGE",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Sozialbeiträge der Arbeitnehmer",
        quarterly_series = "SGE_SVGAN",
        annual_series = "AGE_SVGAN",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Lohnsteuer",
        quarterly_series = "SGE_TAN",
        annual_series = "AGE_TAN",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre(
        title = "Nettolöhne und -gehälter",
        quarterly_series = "SGE_NLG",
        annual_series = "AGE_NLG",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( # =byan/ava/bip_p15
        title = "Reale Arbeitskosten je Stunde",
        quarterly_series = "SGE_RAK",
        annual_series = "AGE_RAK",
        yaxis = "Vorjahresvergleich in %",
        page = 1,
        page_title = "Verteilung des Nationaleinkommens",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p13 = [
    Halbjahre( 
        title = "Nettolöhne und -gehälter",
        quarterly_series = "SGE_NLG",
        annual_series = "AGE_NLG",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Monetäre Sozialleistungen",
        quarterly_series = "SGE_YTLMSEPH",
        annual_series = "AGE_YTLMSEPH",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Abgaben auf soziale Leistungen, verbrauchsnahe Steuern",
        quarterly_series = "SGE_TYTLMS",
        annual_series = "AGE_TYTLMS",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( # M1064+M1040-M1056-M1024-M1032
        title = "Übrige Primäreinkommen (Entnahmen)",
        quarterly_series = "SGE_UPK",
        annual_series = "AGE_UPK",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Transfers (Saldo)",
        quarterly_series = "SGE_GVT",
        annual_series = "AGE_GVT",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Verfügbares Einkommen",
        quarterly_series = "SGE_VERFEK",
        annual_series = "AGE_VERFEK",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Versorgungsansprüche",
        quarterly_series = "SGE_SYTLPH",
        annual_series = "AGE_SYTLPH",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP",
        annual_series = "AGE_CP",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sparen",
        quarterly_series = "SGE_SP",
        annual_series = "AGE_SP",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( # =M1092/(M1062+M1070)*100
        title = "Sparquote in %",
        quarterly_series = "SGE_SPQ",
        annual_series = "AGE_SPQ",
        yaxis = "Mrd. EUR", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.2f",
        scaling = 100
    ),
]

halbjahre_p14 = [
    Halbjahre( 
        title = "Nettolöhne und -gehälter",
        quarterly_series = "SGE_NLG",
        annual_series = "AGE_NLG",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Monetäre Sozialleistungen",
        quarterly_series = "SGE_YTLMSEPH",
        annual_series = "AGE_YTLMSEPH",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Abgaben auf soziale Leistungen, verbrauchsnahe Steuern",
        quarterly_series = "SGE_TYTLMS",
        annual_series = "AGE_TYTLMS",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( # M1064+M1040-M1056-M1024-M1032
        title = "Übrige Primäreinkommen (Entnahmen)",
        quarterly_series = "SGE_UPK",
        annual_series = "AGE_UPK",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Transfers (Saldo)",
        quarterly_series = "SGE_GVT",
        annual_series = "AGE_GVT",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Verfügbares Einkommen",
        quarterly_series = "SGE_VERFEK",
        annual_series = "AGE_VERFEK",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Versorgungsansprüche",
        quarterly_series = "SGE_SYTLPH",
        annual_series = "AGE_SYTLPH",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP",
        annual_series = "AGE_CP",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sparen",
        quarterly_series = "SGE_SP",
        annual_series = "AGE_SP",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einkommen der privaten Haushalte und seine Verwendung",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p15 = [
    Halbjahre( 
        title = "Arbeitnehmer im Inland (1000)",
        quarterly_series = "SGE_EWA",
        annual_series = "AGE_EWA",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttolohn je Arbeitnehmer (EUR)",
        quarterly_series = "SGE_BLJE",
        annual_series = "AGE_BLJE",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = 1000000
    ),
    Halbjahre( 
        title = "Arbeitszeit je Arbeitnehmer (Std.)",
        quarterly_series = "SGE_AWJE",
        annual_series = "AGE_AWJE",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = 1000
    ),
    Halbjahre( 
        title = "Arbeitsvolumen der Arbeitnehmer (Mill. Std.)",
        quarterly_series = "SGE_AVA",
        annual_series = "AGE_AVA",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Tarifverdienste auf Monatsbasis (2020=100)",
        quarterly_series = "SGE_TLGMAM",
        annual_series = "AGE_TLGMAM",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Effektivverdienste (Bruttolöhne je Kopf im Monat im Inland)",
        quarterly_series = "SGE_EFFVER",
        annual_series = "AGE_EFFVER",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttolöhne und -gehälter im Inland (Mrd. EUR)",
        quarterly_series = "SGE_BLGN",
        annual_series = "AGE_BLGN",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Saldo",
        quarterly_series = "SGE_SALDOAM",
        annual_series = "AGE_SALDOAM",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttolöhne und -gehälter (Mrd. EUR)",
        quarterly_series = "SGE_BLGL",
        annual_series = "AGE_BLGL",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p16 = [
    Halbjahre( 
        title = "Arbeitnehmer im Inland (1000)",
        quarterly_series = "SGE_EWA",
        annual_series = "AGE_EWA",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttolohn je Arbeitnehmer (EUR)",
        quarterly_series = "SGE_BLJE",
        annual_series = "AGE_BLJE",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Arbeitszeit je Arbeitnehmer (Std.)",
        quarterly_series = "SGE_AWJE",
        annual_series = "AGE_AWJE",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Arbeitsvolumen der Arbeitnehmer",
        quarterly_series = "SGE_AVA",
        annual_series = "AGE_AVA",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Tarifverdienste auf Monatsbasis (2020=100)",
        quarterly_series = "SGE_TLGMAM",
        annual_series = "AGE_TLGMAM",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Lohndrift (Raten-differenz)",
        quarterly_series = "SGE_LDRIFT",
        annual_series = "AGE_LDRIFT",
        yaxis = "Absolute Zahlen", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Effektivverdienste (Bruttolöhne je Kopf im Monat im Inland)",
        quarterly_series = "SGE_EFFVER",
        annual_series = "AGE_EFFVER",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttolöhne und -gehälter im Inland (Mrd. EUR)",
        quarterly_series = "SGE_BLGN",
        annual_series = "AGE_BLGN",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttolöhne und -gehälter (Mrd. EUR)",
        quarterly_series = "SGE_BLGL",
        annual_series = "AGE_BLGL",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Komponenten der Lohnentwicklung  ",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p17 = [
    Halbjahre( 
        title = "Steuern",
        quarterly_series = "SGE_TEST",
        annual_series = "AGE_TEST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Nettosozialbeiträge",
        quarterly_series = "SGE_SVEST",
        annual_series = "AGE_SVEST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene Vermögenseinkommen",
        quarterly_series = "SGE_BYUEST",
        annual_series = "AGE_BYUEST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene sonstige  laufende Transfers",
        quarterly_series = "SGE_YTSEST",
        annual_series = "AGE_YTSEST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene Vermögenstransfers",
        quarterly_series = "SGE_YTVEST",
        annual_series = "AGE_YTVEST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Verkäufe",
        quarterly_series = "SGE_YCST",
        annual_series = "AGE_YCST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene sonstige Subventionen",
        quarterly_series = "SGE_SSEST",
        annual_series = "AGE_SSEST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Gesamteinnahmen",
        quarterly_series = "SGE_GESEI",
        annual_series = "AGE_GESEI",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Gesamtausgaben",
        quarterly_series = "SGE_GESAU",
        annual_series = "AGE_GESAU",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Finanzierungssaldo",
        quarterly_series = "SGE_FINSA",
        annual_series = "AGE_FINSA",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p18 = [
    Halbjahre( 
        title = "Steuern",
        quarterly_series = "SGE_TEST",
        annual_series = "AGE_TEST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Nettosozialbeiträge",
        quarterly_series = "SGE_SVEST",
        annual_series = "AGE_SVEST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene Vermögenseinkommen",
        quarterly_series = "SGE_BYUEST",
        annual_series = "AGE_BYUEST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene sonstige  laufende Transfers",
        quarterly_series = "SGE_YTSEST",
        annual_series = "AGE_YTSEST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene Vermögenstransfers",
        quarterly_series = "SGE_YTVEST",
        annual_series = "AGE_YTVEST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Verkäufe",
        quarterly_series = "SGE_YCST",
        annual_series = "AGE_YCST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Empfangene sonstige Subventionen",
        quarterly_series = "SGE_SSEST",
        annual_series = "AGE_SSEST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Gesamteinnahmen",
        quarterly_series = "SGE_GESEI",
        annual_series = "AGE_GESEI",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Gesamtausgaben",
        quarterly_series = "SGE_GESAU",
        annual_series = "AGE_GESAU",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Einnahmen des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p19 = [
    Halbjahre( 
        title = "Vorleistungen Sonstige Produktionsabgaben",
        quarterly_series = "SGE_VORLPLUS",
        annual_series = "AGE_VORLPLUS",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Arbeitnehmerentgelt",
        quarterly_series = "SGE_BYANGST",
        annual_series = "AGE_BYANGST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Geleistete Vermögenseinkommen",
        quarterly_series = "SGE_BYUGST",
        annual_series = "AGE_BYUGST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Subventionen",
        quarterly_series = "SGE_SUBGST",
        annual_series = "AGE_SUBGST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Monetäre Sozialleistungen",
        quarterly_series = "SGE_YTLMSGST",
        annual_series = "AGE_YTLMSGST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Soziale Sachleistungen",
        quarterly_series = "SGE_CSTSO",
        annual_series = "AGE_CSTSO",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige laufende Transfers",
        quarterly_series = "SGE_YTSGST",
        annual_series = "AGE_YTSGST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Geleistete Vermögenstransfers",
        quarterly_series = "SGE_YTVGST",
        annual_series = "AGE_YTVGST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttoinvestitionen",
        quarterly_series = "SGE_IBRST",
        annual_series = "AGE_IBRST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Nettozugang an nicht-produzierten Vermögensgütern",
        quarterly_series = "SGE_INZST",
        annual_series = "AGE_INZST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Gesamtausgaben",
        quarterly_series = "SGE_GESAU",
        annual_series = "AGE_GESAU",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p20 = [
    Halbjahre( 
        title = "Vorleistungen Sonstige Produktionsabgaben",
        quarterly_series = "SGE_VORLPLUS",
        annual_series = "AGE_VORLPLUS",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Arbeitnehmerentgelt",
        quarterly_series = "SGE_BYANGST",
        annual_series = "AGE_BYANGST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Geleistete Vermögenseinkommen",
        quarterly_series = "SGE_BYUGST",
        annual_series = "AGE_BYUGST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Subventionen",
        quarterly_series = "SGE_SUBGST",
        annual_series = "AGE_SUBGST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Monetäre Sozialleistungen",
        quarterly_series = "SGE_YTLMSGST",
        annual_series = "AGE_YTLMSGST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Soziale Sachleistungen",
        quarterly_series = "SGE_CSTSO",
        annual_series = "AGE_CSTSO",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige laufende Transfers",
        quarterly_series = "SGE_YTSGST",
        annual_series = "AGE_YTSGST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Geleistete Vermögenstransfers",
        quarterly_series = "SGE_YTVGST",
        annual_series = "AGE_YTVGST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bruttoinvestitionen",
        quarterly_series = "SGE_IBRST",
        annual_series = "AGE_IBRST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Gesamtausgaben",
        quarterly_series = "SGE_GESAU",
        annual_series = "AGE_GESAU",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Ausgaben des Staates",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p21 = [
    Halbjahre( 
        title = "Export Waren",
        quarterly_series = "SGE_EXW",
        annual_series = "AGE_EXW",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export Dienstleistungen",
        quarterly_series = "SGE_EXD",
        annual_series = "AGE_EXD",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export",
        quarterly_series = "SGE_EX",
        annual_series = "AGE_EX",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMW",
        annual_series = "AGE_IMW",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMD",
        annual_series = "AGE_IMD",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IM",
        annual_series = "AGE_IM",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Außenbeitrag Waren",
        quarterly_series = "SGE_AW",
        annual_series = "AGE_AW",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Außenbeitrag Dienstleistungen",
        quarterly_series = "SGE_ADL",
        annual_series = "AGE_ADL",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Außenbeitrag",
        quarterly_series = "SGE_AG",
        annual_series = "AGE_AG",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p22 = [
    Halbjahre( 
        title = "Export Waren",
        quarterly_series = "SGE_EXW",
        annual_series = "AGE_EXW",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export Dienstleistungen",
        quarterly_series = "SGE_EXD",
        annual_series = "AGE_EXD",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export",
        quarterly_series = "SGE_EX",
        annual_series = "AGE_EX",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMW",
        annual_series = "AGE_IMW",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Dienstlestungen",
        quarterly_series = "SGE_IMD",
        annual_series = "AGE_IMD",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import",
        quarterly_series = "SGE_IM",
        annual_series = "AGE_IM",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Außenbeitrag Waren",
        quarterly_series = "SGE_AW",
        annual_series = "AGE_AW",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
]
    
halbjahre_p23 = [
    Halbjahre( 
        title = "Export Waren",
        quarterly_series = "SGE_EXW_9",
        annual_series = "AGE_EXW_9",
        yaxis = "Verkettete Volumina in Mrd.EUR", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export Dienstleistungen",
        quarterly_series = "SGE_EXD_9",
        annual_series = "AGE_EXD_9",
        yaxis = "Verkettete Volumina in Mrd.EUR", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export",
        quarterly_series = "SGE_EX_9",
        annual_series = "AGE_EX_9",
        yaxis = "Verkettete Volumina in Mrd.EUR", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMW_9",
        annual_series = "AGE_IMW_9",
        yaxis = "Verkettete Volumina in Mrd.EUR", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Dienstleistungen",
        quarterly_series = "SGE_IMD_9",
        annual_series = "AGE_IMD_9",
        yaxis = "Verkettete Volumina in Mrd.EUR", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import",
        quarterly_series = "SGE_IM_9",
        annual_series = "AGE_IM_9",
        yaxis = "Verkettete Volumina in Mrd.EUR", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p24 = [
    Halbjahre( 
        title = "Exporte",
        quarterly_series = "SGE_WBEX",
        annual_series = "AGE_WBEX",
        yaxis = "Wacchstumsbeiträge in Prozentpunkten", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Importe",
        quarterly_series = "SGE_WBIM",
        annual_series = "AGE_WBIM",
        yaxis = "Wacchstumsbeiträge in Prozentpunkten", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Außenbeitrag",
        quarterly_series = "sge_wbx",
        annual_series = "age_wbx",
        yaxis = "Wacchstumsbeiträge in Prozentpunkten", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = 100
    ),
]

halbjahre_p25 = [
    Halbjahre( 
        title = "Export Waren",
        quarterly_series = "SGE_EXW_9",
        annual_series = "AGE_EXW_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export Dienstleistungen",
        quarterly_series = "SGE_EXD_9",
        annual_series = "AGE_EXD_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export",
        quarterly_series = "SGE_EX_9",
        annual_series = "AGE_EX_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMW_9",
        annual_series = "AGE_IMW_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Dienstleistungen",
        quarterly_series = "SGE_IMD_9",
        annual_series = "AGE_IMD_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import",
        quarterly_series = "SGE_IM_9",
        annual_series = "AGE_IM_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p26 = [
    Halbjahre( 
        title = "Export Waren",
        quarterly_series = "SGE_EXW_p15",
        annual_series = "AGE_EXW_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Export Dienstleistungen",
        quarterly_series = "SGE_EXD_p15",
        annual_series = "AGE_EXD_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Export",
        quarterly_series = "SGE_EX_p15",
        annual_series = "AGE_EX_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMW_p15",
        annual_series = "AGE_IMW_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Import Dienstleistungen",
        quarterly_series = "SGE_IMD_p15",
        annual_series = "AGE_IMD_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Import",
        quarterly_series = "SGE_IM_p15",
        annual_series = "AGE_IM_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Terms of Trade Waren",
        quarterly_series = "SGE_TTW",
        annual_series = "AGE_TTW",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Terms of Trade Dienstleistungen",
        quarterly_series = "SGE_TTD",
        annual_series = "AGE_TTD",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Terms of Trade",
        quarterly_series = "SGE_TT",
        annual_series = "AGE_TT",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Export und Import, real",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p27 = [
    Halbjahre( 
        title = "Export Waren",
        quarterly_series = "SGE_EXW_p15",
        annual_series = "AGE_EXW_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export Dienstleistungen",
        quarterly_series = "SGE_EXD_p15",
        annual_series = "AGE_EXD_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Export",
        quarterly_series = "SGE_EX_p15",
        annual_series = "AGE_EX_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Waren",
        quarterly_series = "SGE_IMW_p15",
        annual_series = "AGE_IMW_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import Dienstleistungen",
        quarterly_series = "SGE_IMD_p15",
        annual_series = "AGE_IMD_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Import",
        quarterly_series = "SGE_IM_p15",
        annual_series = "AGE_IM_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Terms of Trade Waren",
        quarterly_series = "SGE_TTW",
        annual_series = "AGE_TTW",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Terms of Trade Dienstleistungen",
        quarterly_series = "SGE_TTD",
        annual_series = "AGE_TTD",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Terms of Trade",
        quarterly_series = "SGE_TT",
        annual_series = "AGE_TT",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Export und Import: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p28 = [
    Halbjahre( 
        title = "Wohnungsbau",
        quarterly_series = "SGE_IBWO",
        annual_series = "AGE_IBWO",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Wirtschaftsbau",
        quarterly_series = "SGE_IBGE",
        annual_series = "AGE_IBGE",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Öffentlicher Nichtwohnungsbau",
        quarterly_series = "SGE_IBNWST",
        annual_series = "AGE_IBNWST",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB",
        annual_series = "AGE_IB",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU",
        annual_series = "AGE_IAU",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO",
        annual_series = "AGE_ISO",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Anlageinvestitionen",
        quarterly_series = "SGE_IANL",
        annual_series = "AGE_IANL",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Vorratsveränderung",
        quarterly_series = "SGE_IL",
        annual_series = "AGE_IL",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Investitionen",
        quarterly_series = "SGE_IBR",
        annual_series = "AGE_IBR",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p29 = [
    Halbjahre( 
        title = "Wohnungsbau",
        quarterly_series = "SGE_IBWO",
        annual_series = "AGE_IBWO",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Wirtschaftsbau",
        quarterly_series = "SGE_IBGE",
        annual_series = "AGE_IBGE",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Öffentlicher Nichtwohnungsbau",
        quarterly_series = "SGE_IBNWST",
        annual_series = "AGE_IBNWST",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB",
        annual_series = "AGE_IB",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU",
        annual_series = "AGE_IAU",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO",
        annual_series = "AGE_ISO",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Anlageinvestitionen",
        quarterly_series = "SGE_IANL",
        annual_series = "AGE_IANL",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Investitionen",
        quarterly_series = "SGE_IBR",
        annual_series = "AGE_IBR",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen in jeweiligen Preisen",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p30 = [
    Halbjahre( 
        title = "Wohnungsbau",
        quarterly_series = "SGE_IBWO_9",
        annual_series = "AGE_IBWO_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Wirtschaftsbau",
        quarterly_series = "SGE_IBGE_9",
        annual_series = "AGE_IBGE_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Öffentlicher Nichtwohnungsbau",
        quarterly_series = "SGE_IBNWST_9",
        annual_series = "AGE_IBNWST_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB_9",
        annual_series = "AGE_IB_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_9",
        annual_series = "AGE_IAU_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_9",
        annual_series = "AGE_ISO_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Anlageinvestitionen",
        quarterly_series = "SGE_IAN_9",
        annual_series = "AGE_IAN_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
    Halbjahre( 
        title = "Investitionen",
        quarterly_series = "SGE_IBR_9",
        annual_series = "AGE_IBR_9",
        yaxis = "in Mrd. EUR", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.2f",
        scaling = None
    ),
]

halbjahre_p31 = [
    Halbjahre( 
        title = "Wohnungsbau",
        quarterly_series = "SGE_IBWO_9",
        annual_series = "AGE_IBWO_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Wirtschaftsbau",
        quarterly_series = "SGE_IBGE_9",
        annual_series = "AGE_IBGE_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Öffentlicher Nichtwohnungsbau",
        quarterly_series = "SGE_IBNWST_9",
        annual_series = "AGE_IBNWST_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB_9",
        annual_series = "AGE_IB_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_9",
        annual_series = "AGE_IAU_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_9",
        annual_series = "AGE_ISO_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Anlageinvestitionen",
        quarterly_series = "SGE_IAN_9",
        annual_series = "AGE_IAN_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Investitionen",
        quarterly_series = "SGE_IBR_9",
        annual_series = "AGE_IBR_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verkettete Volumina in Mrd.EUR",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p32 = [
    Halbjahre( 
        title = "Wohnungsbau",
        quarterly_series = "SGE_IBWO_p15",
        annual_series = "AGE_IBWO_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Wirtschaftsbau",
        quarterly_series = "SGE_IBGE_p15",
        annual_series = "AGE_IBGE_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Öffentlicher Nichtwohnungsbau",
        quarterly_series = "SGE_IBNWST_p15",
        annual_series = "AGE_IBNWST_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB_p15",
        annual_series = "AGE_IB_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_p15",
        annual_series = "AGE_IAU_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_p15",
        annual_series = "AGE_ISO_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Anlageinvestitionen",
        quarterly_series = "SGE_IAN_p15",
        annual_series = "AGE_IAN_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Investitionen",
        quarterly_series = "SGE_IBR_p15",
        annual_series = "AGE_IBR_p15",
        yaxis = "2015=100", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.2f",
        scaling = 100
    ),
]

halbjahre_p33 = [
    Halbjahre( 
        title = "Wohnungsbau",
        quarterly_series = "SGE_IBWO_p15",
        annual_series = "AGE_IBWO_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Wirtschaftsbau",
        quarterly_series = "SGE_IBGE_p15",
        annual_series = "AGE_IBGE_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Öffentlicher Nichtwohnungsbau",
        quarterly_series = "SGE_IBNWST_p15",
        annual_series = "AGE_IBNWST_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB_p15",
        annual_series = "AGE_IB_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_p15",
        annual_series = "AGE_IAU_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_p15",
        annual_series = "AGE_ISO_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Anlageinvestitionen",
        quarterly_series = "SGE_IAN_p15",
        annual_series = "AGE_IAN_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Investitionen",
        quarterly_series = "SGE_IBR_p15",
        annual_series = "AGE_IBR_p15",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Investitionen: Preisniveau",
        tickformat = ",.1f",
        scaling = None
    ),
]

halbjahre_p34 = [
    Halbjahre( 
        title = "Private Konsumausgaben",
        quarterly_series = "SGE_CP_WB",
        annual_series = "AGE_CP_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Konsumausgaben des Staates",
        quarterly_series = "SGE_CST_WB",
        annual_series = "AGE_CST_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Bruttoanlageinvestitionen",
        quarterly_series = "SGE_IAN_WB",
        annual_series = "AGE_IAN_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Ausrüstungen",
        quarterly_series = "SGE_IAU_WB",
        annual_series = "AGE_IAU_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Bauten",
        quarterly_series = "SGE_IB_WB",
        annual_series = "AGE_IB_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Sonstige Anlagen",
        quarterly_series = "SGE_ISO_WB",
        annual_series = "AGE_ISO_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Vorratsinvestitionen",
        quarterly_series = "SGE_IVC_WB",
        annual_series = "AGE_IVC_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Inländische Verwendung",
        quarterly_series = "SGE_NI_WB",
        annual_series = "AGE_NI_WB",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Außenbeitrag",
        quarterly_series = "SGE_WBX",
        annual_series = "AGE_WBX",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Exporte",
        quarterly_series = "SGE_WBEX",
        annual_series = "AGE_WBEX",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Importe",
        quarterly_series = "SGE_WBIM",
        annual_series = "AGE_WBIM",
        yaxis = "Beiträge der Verwendungskomponenten zum Anstieg des BIP in Prozentpunkten", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Bruttoinlandsprodukt,real",
        quarterly_series = "SGE_BIP_9",
        annual_series = "AGE_BIP_9",
        yaxis = "Vorjahresvergleich in %", 
        page = 1,
        page_title = "Verwendung des Inlandsprodukts, real. Wachstumsbeiträge",
        tickformat = ",.1f",
        scaling = 100
    ),
]

halbjahre_p35 = [
    Halbjahre( 
        title = "Außenbeitrag in Relation zum BIP",
        quarterly_series = "SGE_AWB",
        annual_series = "AGE_AWB",
        yaxis = "", 
        page = 1,
        page_title = "Nachrichtlich",
        tickformat = ",.1f",
        scaling = 100
    ),
    Halbjahre( 
        title = "Saldo der Leistungsbilanz",
        quarterly_series = "SGE_YEXIMC",
        annual_series = "AGE_YEXIMC",
        yaxis = "", 
        page = 1,
        page_title = "Nachrichtlich",
        tickformat = ",.1f",
        scaling = None
    ),
    Halbjahre( 
        title = "Saldo der Leistungsbilanz in Relation zum BIP",
        quarterly_series = "SGE_YEXIMCREL",
        annual_series = "AGE_YEXIMCREL",
        yaxis = "", 
        page = 1,
        page_title = "Nachrichtlich",
        tickformat = ",.1f",
        scaling = 100
    ),
]