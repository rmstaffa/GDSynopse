#%% packages

# core packages
import pandas as pd
import numpy as np
import re
from collections import OrderedDict
import glob
import time
from pathlib import Path

# third party
from loguru import logger
from dataclasses import dataclass, field

#%%

def transformA(df):
    '''
    transform data from raw to processed
    '''
    
    # extract variable names
    all_mnemonics = df.iloc[:,0].astype(str)
    all_names = df.iloc[:,1].astype(str)
    pat = re.compile(r"[A-Z0-9_\.]+")
    boolean = all_mnemonics.str.contains(pat)
    mnemonics = all_mnemonics[boolean].str.strip()
    mnemonics = mnemonics.str.split(".").str[0]
    names = all_names[boolean].str.strip()

    # create mapping 
    mnemonic_map = OrderedDict(zip(mnemonics,names))

    # create yearly
    pat_date = re.compile(r"[0-9]{4}")

    # get yearly dates
    row_yrly,_ = np.where(df.iloc[:10,:10].apply(lambda x: x.astype(str).str.contains("Jahr")))

    # get dates
    dates_yrly = df.iloc[row_yrly[0],:].astype(str).reset_index(drop=True)
    dates_yrly = dates_yrly[dates_yrly.str.contains(pat_date)]
    mnemonics_yrly = mnemonics[mnemonics.str.startswith("A")]

    data_yrly = pd.DataFrame(
            df.iloc[mnemonics_yrly.index,dates_yrly.index.tolist()].to_numpy(),
            columns=dates_yrly.tolist(),index=mnemonics_yrly.tolist()
            ).T

    # add datetime indexes
    data_yrly.index = pd.to_datetime(data_yrly.index.str.replace(".0",".06"),format="%Y.%m")
    data_yrly = data_yrly.apply(lambda x: pd.to_numeric(x,errors="coerce"), axis=1)
    data_yrly.columns = data_yrly.columns.str.lower()
    
    # -- yearly additional computations
    
    # add Stundenproduktivität
    data_yrly["age_prodh"] = data_yrly["age_bip_v_x"] / data_yrly["age_av_x_x"]  * 1000_000
    data_yrly["age_prodheu"] = data_yrly["age_ypoteu_c_x"] / data_yrly["age_lpeu_c_x"] * 1_000_000

    # Arbeitszeit je Erwerbstätigen
    data_yrly["age_wtempl"] = data_yrly["age_av_x_x"] / data_yrly["age_ew_x_x"] * 1000

    # ToT
    data_yrly["age_tot"] = data_yrly["age_av_x_x"] / data_yrly["age_ew_x_x"] * 1000

    # add Output gap 
    # (EU)
    data_yrly["age_ygapeu"] = (data_yrly["age_bip_v_x"] - data_yrly["age_ypoteu_c_x"])/data_yrly["age_ypoteu_c_x"] * 100
    # (MODEM)
    data_yrly["age_ygap"] = (data_yrly["age_bip_v_x"] - data_yrly["age_ypot_c_x"])/data_yrly["age_ypot_c_x"] * 100

    # add NAWRU
    data_yrly["age_nawrueu"] = 100 - data_yrly["age_1_nairueu_c_x"]

    # Preisniveau 2015 _c_x
    comp = ["ge_cp","ge_cst","ge_iau","ge_ib","ge_iv","ge_ex","ge_im","ge_bip"]
    for c in comp:
        
        if c == "ge_iv":
            data_yrly["a"+c+"_p15"] = data_yrly["a"+"ge_iv_c_x"] / data_yrly["a"+c+"_v_x"]
        else:
            data_yrly["a"+c+"_p15"] = data_yrly["a"+c+"_c_x"] / data_yrly["a"+c+"_v_x"]

    # Terms of Trade
    data_yrly["age_tt"] = data_yrly["age_ex_p15"] / data_yrly["age_im_p15"] * 100

    # Bruttonationaleinkommen
    data_yrly["age_bnek"] = data_yrly["age_yexim_c_x"] + data_yrly["age_bip_c_x"] 

    # Nettonationaleinkommen 
    data_yrly["age_nnek"] = data_yrly["age_bnek"] - data_yrly["age_ab_c_x"] 

    # verfügbares EK
    data_yrly["age_verfek"] = (data_yrly["age_sp_c_x"] + data_yrly["age_cp_c_x"]) - data_yrly["age_sytlph_c_x"]  

    # Nettolöhne- und Gehälter:
    data_yrly["age_nlg"] = data_yrly["age_blgl_c_x"] - data_yrly["age_svgan_c_x"] - data_yrly["age_tan_c_x"]  

    # Primäreinkommen der privaten Haushalte
    data_yrly["age_pekphh"] = (data_yrly["age_svgag_c_x"]+data_yrly["age_blgl_c_x"]+data_yrly["age_verfek"]+data_yrly["age_tytlms_c_x"]) - (data_yrly["age_gvt_c_x"]+data_yrly["age_nlg"]+data_yrly["age_ytlmseph_c_x"])

    # Primär-einkommen der übrigen Sektoren
    data_yrly["age_pekusek"] = data_yrly["age_nnek"] - data_yrly["age_pekphh"]

    # Volkseinkommen
    data_yrly["age_vek"] = data_yrly["age_nnek"] - data_yrly["age_tindmsub_c_x"]

    # Arbeitnehmerentgelte
    data_yrly["age_aneg"] = data_yrly["age_svgag_c_x"] + data_yrly["age_blgl_c_x"]

    # Unternehmens und Vermögenseinkommen
    data_yrly["age_uvek"] = data_yrly["age_vek"] - data_yrly["age_aneg"]

    # Lohnstückkosten
    data_yrly["age_lucost"] = (data_yrly["age_byan_c_x"]/data_yrly["age_ewa_x_x"])/(data_yrly["age_bip_v_x"]/data_yrly["age_ew_x_x"])

    # Lohnstückkosten auf Stundenbasis
    data_yrly["age_lucoststd"] = (data_yrly["age_byan_c_x"]/data_yrly["age_ava_x_x"])/(data_yrly["age_bip_v_x"]/data_yrly["age_av_x_x"])

    # Abzüge (Nettonationaleinkommen)
    data_yrly["age_abzuege"] = data_yrly["age_svgan_c_x"] + data_yrly["age_tan_c_x"]

    # Saldo (Nettonationaleinkommen)
    data_yrly["age_saldo"] = data_yrly["age_byan_c_x"] - data_yrly["age_aneg"]

    # Reale Arbeitskosten je Stunde
    data_yrly["age_rak"] = data_yrly["age_byan_c_x"] / data_yrly["age_ava_x_x"] / data_yrly["age_bip_p15"]

    # Übrige Primäreinkommen (Entnahmen)
    data_yrly["age_upk"] = data_yrly["age_verfek"] + data_yrly["age_tytlms_c_x"] - (data_yrly["age_gvt_c_x"]+data_yrly["age_nlg"]+data_yrly["age_ytlmseph_c_x"])

    # Sparquote
    data_yrly["age_spq"] = data_yrly["age_sp_c_x"] / (data_yrly["age_verfek"] + data_yrly["age_sytlph_c_x"])

    # Bruttolohn je Arbeitnehmer (EUR)
    data_yrly["age_blje"] = data_yrly["age_blgn_c_x"] / data_yrly["age_ewa_x_x"]

    # Arbeitszeit je Arbeitnehmer (Std.)
    data_yrly["age_awje"] = data_yrly["age_ava_x_x"] / data_yrly["age_ewa_x_x"]

    # Effektivverdienste (Bruttolöhne je Kopf im Monat im Inland)
    data_yrly["age_effver"] = (data_yrly["age_blgn_c_x"] / data_yrly["age_ewa_x_x"])*(1000000/12)

    # Saldo (Lohnentwicklung)
    data_yrly["age_saldoam"] = data_yrly["age_blgl_c_x"] - data_yrly["age_blgn_c_x"]

    # Lohndrift
    data_yrly["age_ldrift"] = data_yrly["age_effver"].pct_change(fill_method=None) - data_yrly["age_tlgmam"].pct_change(fill_method=None) 

    # GEsamteinnahmen Staat
    data_yrly["age_gesei"] = data_yrly.loc[:,["age_test_c_x","age_svest_c_x","age_byuest_c_x","age_ytsest_c_x","age_ytvest_c_x","age_ycst_c_x","age_ssest_c_x"]].sum(axis=1)

    # Vorleistungen Sonstige Produktionsabgaben
    data_yrly["age_vorlplus"] = data_yrly["age_cstvo_c_x"] + data_yrly["age_gpgst_c_x"]

    # GEsamtausgaben Staat
    data_yrly["age_gesau"] = data_yrly.loc[:,["age_vorlplus","age_byangst_c_x","age_byugst_c_x","age_subgst_c_x","age_ytlmsgst_c_x","age_ytsgst_c_x","age_ytvgst_c_x","age_ibrst_c_x","age_inzst_c_x","age_cstso_c_x"]].sum(axis=1)

    # FInanzierungssaldo Staat
    data_yrly["age_finsa"] = data_yrly["age_gesei"] - data_yrly["age_gesau"]

    # Dienstleistungsexporte
    data_yrly["age_exd"] = data_yrly["age_ex_c_x"] - data_yrly["age_exw_c_x"]

    # Dienstleistungsimporte
    data_yrly["age_imd"] = data_yrly["age_im_c_x"] - data_yrly["age_imw_c_x"]

    # Außenbeitrag Waren
    data_yrly["age_aw"] = data_yrly["age_exw_c_x"] - data_yrly["age_imw_c_x"]

    # Außenbeitrag Dienstleistungen
    data_yrly["age_adl"] = data_yrly["age_exd"] - data_yrly["age_imd"]

    # Außenbeitrag GEsamt
    data_yrly["age_ag"] = data_yrly["age_aw"] + data_yrly["age_adl"]

    # reale Außenbeiträge
    # =(M373-J373)/J395*K549/K571*100
    data_yrly["age_wbex"] = data_yrly["age_ex_v_x"].pct_change(periods=1,fill_method=None) * (data_yrly["age_ex_c_x"] / data_yrly["age_bip_c_x"]).shift(1)

    data_yrly["age_wbim"] = -(data_yrly["age_im_v_x"].pct_change(periods=1,fill_method=None) * (data_yrly["age_im_c_x"] / data_yrly["age_bip_c_x"]).shift(1))

    # saldo 
    data_yrly["age_wbx"] = data_yrly["age_wbex"] + data_yrly["age_wbim"]

    comp = ["ge_exw","ge_imw","ge_exd","ge_imd"]
    for c in comp:
        
        data_yrly["a"+c+"_p15"] = data_yrly["a"+c+"_c_x"] / data_yrly["a"+c+"_v_x"]
        
    # ToT (Waren)
    data_yrly["age_ttw"] = data_yrly["age_exw_p15"] / data_yrly["age_imw_p15"]
    # ToT (Dienstleistungen)
    data_yrly["age_ttd"] = data_yrly["age_exd_p15"] / data_yrly["age_imd_p15"] 

    # Anlageinvestitionen
    data_yrly["age_ianl"] = data_yrly["age_ib_c_x"] + data_yrly["age_iau_c_x"] + data_yrly["age_iso_c_x"]

    # Investitionen
    data_yrly["age_ibr"] = data_yrly["age_ianl"] + data_yrly["age_il_c_x"]

    comp = ["ge_ibwo","ge_ibge","ge_ibnwst","ge_ib","ge_iau","ge_iso","ge_ian","ge_ibr"]
    for c in comp:
        
        # handle special case Anlageinve        
        data_yrly["a"+c+"_p15"] = data_yrly["a"+c+"_c_x"] / data_yrly["a"+c+"_v_x"]

    # =L409 (pct_change VJ)
    # real_change * share_t-1

    lst = ["ge_cp","ge_cst","ge_ibr","ge_ian","ge_iau","ge_ib","ge_iso","ge_iv","ge_ex","ge_im","ge_bip"]

    for comp in lst:
        
        if comp == "ge_iv":
            data_yrly["a"+comp+"_wb"] = data_yrly["a"+comp+"_v_x"].pct_change(fill_method=None) * (data_yrly["a"+"ge_iv_c_x"] / data_yrly["age_bip_c_x"]).shift(1)
        else:
            data_yrly["a"+comp+"_wb"] = data_yrly["a"+comp+"_v_x"].pct_change(fill_method=None) * (data_yrly["a"+comp+"_c_x"] / data_yrly["age_bip_c_x"]).shift(1)
        
    # inventories contr
    data_yrly["age_ivc_wb"] = data_yrly["age_iv_wb"] - data_yrly["age_cp_wb"] - data_yrly["age_cst_wb"] - data_yrly["age_ian_wb"]

    # AUßenbeitrag in Relation BIP
    data_yrly["age_awb"] = data_yrly["age_ag"] / data_yrly["age_bip_c_x"]

    # Saldo der Leistungsbilanz in Relation zum BIP 
    data_yrly["age_yeximcrel"] = data_yrly["age_yeximc_c_x"] / data_yrly["age_bip_c_x"]

    # MFP / POTENTIAL
    # Deflatoren
    data_yrly["age_pbip"] = data_yrly["age_bip_c_x"] / data_yrly["age_bip_v_x"]*100
    data_yrly["age_pcp"] = data_yrly["age_cp_c_x"] / data_yrly["age_cp_v_x"]*100
    data_yrly["age_pcst"] = data_yrly["age_cst_c_x"] / data_yrly["age_cst_v_x"]*100
    data_yrly["age_piau"] = data_yrly["age_iau_c_x"] / data_yrly["age_iau_v_x"]*100
    data_yrly["age_pib"] = data_yrly["age_ib_c_x"] / data_yrly["age_ib_v_x"]*100
    data_yrly["age_pex"] = data_yrly["age_ex_c_x"] / data_yrly["age_ex_v_x"]*100
    data_yrly["age_pim"] = data_yrly["age_im_c_x"] / data_yrly["age_im_v_x"]*100
    # Arbeitszeit
    data_yrly["age_mfpazeit"] = data_yrly["age_av_x_x"] / data_yrly["age_ew_x_x"]*1000
    # Trms of Trade
    data_yrly["age_termtrade"] = data_yrly["age_pex"] / data_yrly["age_pim"] 
    # Quoten
    data_yrly["age_qcp"] = data_yrly["age_cp_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qcst"] = data_yrly["age_cst_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qiau"] = (data_yrly["age_iau_c_x"]+data_yrly["age_iso_c_x"]) / data_yrly["age_bip_c_x"]
    data_yrly["age_qib"] = data_yrly["age_ib_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qex"] = data_yrly["age_ex_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qim"] = data_yrly["age_im_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qni"] = data_yrly["age_iv_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qab"] = data_yrly["age_exim_c_x"] / data_yrly["age_bip_c_x"]
    data_yrly["age_qil"] = data_yrly["age_il_c_x"] / data_yrly["age_bip_c_x"]

    # Lohnquote
    data_yrly["age_lohnq"] = (data_yrly["age_blgl_c_x"] + data_yrly["age_svgag_c_x"]) / data_yrly["age_vek"]
    # bereinigte Lohnquote
    data_yrly["age_blohnq"] = data_yrly["age_lohnq"] * data_yrly["age_av_x_x"] / data_yrly["age_ava_x_x"]

    # tatsächlich vs. potenziell
    data_yrly["age_ewpot"] = data_yrly["age_lpeu_c_x"] / data_yrly["age_hoursteu_c_x"] * 1000
    data_yrly["age_aztat"] = data_yrly["age_av_x_x"] / data_yrly["age_ew_x_x"] * 1000
    data_yrly = data_yrly.copy() # consolidate the fragmented data (avoids the warning)
    data_yrly["age_lppot"] = data_yrly["age_lpeu_c_x"] 
    
    data_yrly["age_ewp_c_x"] = data_yrly["age_popw_c_x"]*data_yrly["age_parts_c_x"]

    return data_yrly, mnemonic_map

def load_data(path,cls):
    '''
    load data from excel to data class
    '''

    # get all sheets
    mfp = pd.read_excel(path, sheet_name=None, header=None)
    
    # create dataframes
    for gd in mfp.keys():
        
        if gd in ["z","y"]:
        
            yrly,mnemonic_map = transformA(mfp[gd])
            
            data_dict = OrderedDict(
                {"A":yrly}
            )
            
            setattr(cls,
                    gd,
                    data_dict)
        
    setattr(cls,"mnemonic_map",mnemonic_map)
    setattr(cls,"Prognosen",list(mfp.keys()))

@dataclass
class SynopseData:
    
    path: str
    time: str = field(default_factory=lambda: time.strftime("%Y-%m-%d %H:%M:%S"))
    
    # A private dictionary to cache dynamically created attributes
    _dynamic_attributes: dict = field(default_factory=dict, init=False, repr=False)
    
    def __post_init__(self):
        
        '''
        check validity of path
        '''
        path = Path(self.path)
        if not path.exists():
            raise ValueError(f"Invalid path: {self.path}")
        

    def __getattr__(self, name):
        """
        Handle dynamic attribute generation and prevent recursion.
        """
        # Explicitly handle IPython's probing attribute to avoid recursion
        # if name == "_ipython_canary_method_should_not_exist_":

        #     raise AttributeError(name)

        # Check if the attribute exists in the dynamic attributes dictionary
        if name not in self._dynamic_attributes:
            # logger.debug(f"Dynamically generating attribute '{name}'")
            self._dynamic_attributes[name] = self._generate_attribute(name)
        return self._dynamic_attributes[name]

    def _generate_attribute(self, name):
        
        name = name.lower()
        
        if name[0] == "a": 
            freq = "A"
        else:
            freq = "A"

        container = []
        for inst in ["z","y"]:
            
            container.append(getattr(self,inst)[freq].loc[:,name])
            
        df = pd.concat(container,axis=1)
        df.columns = ["z","y"]
        
        try:
            return df, self.mnemonic_map[name.upper()]
        except KeyError:
            return df, "No description available"
    
    def get_series(self, name):
        
        return self.__getattr__(name)
    
    def load_data(self):
        
        load_data(self.path,self)
        
        return self
    
    


