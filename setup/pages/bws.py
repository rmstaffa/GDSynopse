from collections import OrderedDict,namedtuple

Bruttowertschoepfung = namedtuple("Verwendung",
                 ["title","quarterly_series"])

bws = [Bruttowertschoepfung(
            title = "Bruttowertschöpfung (real)",
            quarterly_series = "QGE_WB_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Produzierendes Gewerbe ohne Bau (real)",
            quarterly_series = "QGE_WBBE_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Verarbeitendes Gewerbe (real)",
            quarterly_series = "QGE_WBC_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Energie- und Wasserversorgung, Entsorgung u.Ä. (real)",
            quarterly_series = "QGE_WBDE_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Baugewerbe (real)",
            quarterly_series = "QGE_WBF_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Handel, Verkehr, Gastgewerbe (real)",
            quarterly_series = "QGE_WBGI_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Handel (real)",
            quarterly_series = "QGE_WBG_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Verkehr und Lagerei (real)",
            quarterly_series = "QGE_WBH_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Gastgewerbe (real)",
            quarterly_series = "QGE_WBI_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Information und Kommunikation (real)",
            quarterly_series = "QGE_WBJ_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Finanz- und Versicherungsdienstleister (real)",
            quarterly_series = "QGE_WBK_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Grundstücks- und Wohnungswesen (real)",
            quarterly_series = "QGE_WBL_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Unternehmensdienstleister (real)",
            quarterly_series = "QGE_WBMN_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Öffentliche Dienstleister, Erziehung, Gesundheit (real)",
            quarterly_series = "QGE_WBOQ_V_A"),
        Bruttowertschoepfung(
            title = "Bruttowertschöpfung Sonstige Dienstleister (real)",
            quarterly_series = "QGE_WBRT_V_A")
]

