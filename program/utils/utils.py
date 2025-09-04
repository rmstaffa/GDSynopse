# packages

# core packages
import panel as pn
pn.extension("plotly")
import pandas as pd
import numpy as np
import re
from collections import OrderedDict,namedtuple

# third party
from loguru import logger
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# prject packages
from . import plot,utils


#%% functions

def format_quarter(date):
    quarter = (date.month - 1) // 3 + 1
    return f'{date.year}Q{quarter}'

def format_hj(date):
    if date.month <= 6:
        return f'{date.year}_1Hj'
    else:
        return f'{date.year}_2Hj'

def create_verwendung(komponente,synopse,settings):

    colors = settings.settings["colors"]
    tickformat = settings.settings["tickformat"]
    window_kf = settings.settings["window_kf"] 
    start_fc = pd.to_datetime(settings.settings["fc_start"])
    
    # -- TAB 1 | 2 | 4 | 6 --
    df,name = synopse.get_series(komponente.quarterly_series)
    df_change = df.pct_change(fill_method=None)
    TAB1,TAB2 = df.loc[window_kf,:].dropna(),df_change.loc[window_kf,:].dropna()*100
    TAB1plot,TAB2plot = TAB1.copy(),TAB2.copy()
    # Verkettete Volumenangaben (ksb) Mrd. Eur
    TAB1.index = TAB1.index.map(utils.format_quarter) 
    # q-q laufende Rate %
    TAB2.index = TAB2.index.map(utils.format_quarter)
    # q4-q4 Rate %
    TAB6 = df.resample("YE").last().pct_change(fill_method=None).loc[window_kf,:].dropna()*100
    # Statistischer Überhang
    TAB5 = (df.resample("YE").last() / df.resample("YE").mean())
    TAB5 = TAB5.loc[window_kf,:].dropna()*100-100
    # Jahresrate kbs
    TAB4 = df.dropna().resample("YE").mean().pct_change(fill_method=None).loc[window_kf,:]*100

    # -- TAB 3 --
    dfA,name = synopse.get_series(komponente.annual_series)
    dfA_change = dfA.pct_change(fill_method=None)
    TAB3 = dfA_change.loc[window_kf,:].dropna()*100

    # adjust index for yearly tables
    TAB3.index = TAB3.index.year
    TAB4.index = TAB4.index.year
    TAB5.index = TAB5.index.year
    TAB6.index = TAB6.index.year
    
    # add mean if specified
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        TAB1["Ø"] = TAB1.mean(axis=1)
        TAB2["Ø"] = TAB2.mean(axis=1)
        TAB3["Ø"] = TAB3.mean(axis=1)
        TAB4["Ø"] = TAB4.mean(axis=1)
        TAB5["Ø"] = TAB5.mean(axis=1)
        TAB6["Ø"] = TAB6.mean(axis=1)

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Add traces
    for inst in TAB1plot.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_line"]
        else:
            style = dict(color=colors[inst])
            
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=style,showlegend=False), row=1, col=1)
        
    for inst in TAB2plot.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_marker"]
        else:
            style = dict(color=colors[inst])
        
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot[inst], name=inst,marker=style), row=2, col=1)
        
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        
        # add mean
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot.mean(axis=1), mode='lines', name="Durchschnitt",line=dict(color="black",dash="dash")), row=1, col=1)
        # add mean
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot.mean(axis=1),name="Durchschnitt",marker=dict(color="lightgray",pattern_shape="\\"),showlegend=False), row=2, col=1)
        
    fig.add_vrect(x0=start_fc-pd.Timedelta("15D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("45D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    xaxis2=dict(gridcolor='whitesmoke'),
                    yaxis1=dict(title="Mrd. Euro",tickformat=tickformat), 
                    yaxis2=dict(title="Q-o-Q Change (%)",tickformat=tickformat),paper_bgcolor='rgba(0, 0, 0, 0)',
                    height=550)



    # Save Plotly figure as HTML div
    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    tables_Q = [TAB1,TAB2]
    tables_A = [TAB3,TAB4,TAB5,TAB6]
    
    # Define a dictionary with formatters for numerical columns
    formatters_Q = {col: '{:,.2f}'.format for col in TAB1.columns}
    formatters_A = {col: '{:,.1f}'.format for col in TAB1.columns}
    html_tables = [df.to_html(classes='table-style-2', border=0, formatters=formatters_Q) for df in tables_Q]+[df.to_html(classes='table-style-2', border=0, formatters=formatters_A) for df in tables_A]

    return [komponente.title, plotly_html_div, html_tables]

def create_arbeitsmarkt(komponente,synopse,settings):

    colors = settings.settings["colors"]
    tickformat = settings.settings["tickformat"]
    window_kf = settings.settings["window_kf"] 
    start_fc = pd.to_datetime(settings.settings["fc_start"])
    
    # -- TAB 1 | 2 | 3
    df,name = synopse.get_series(komponente.series)
    df_change = df.pct_change(fill_method=None)
    df_delta = df.diff()

    TAB1,TAB2,TAB3 = df.loc[window_kf,:].dropna(),df_change.loc[window_kf,:].dropna()*100,df_delta.loc[window_kf,:].dropna()

    # change index to year
    TAB1.index = TAB1.index.year
    TAB2.index = TAB2.index.year
    TAB3.index = TAB3.index.year
    
    # create plot
    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Add traces
    for inst in TAB1.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_line"]
        else:
            style = dict(color=colors[inst])
            
        fig.add_trace(go.Scatter(x=TAB1.index, y=TAB1[inst], mode='lines', name=inst,line=style,showlegend=False), row=1, col=1)
        
    for inst in TAB2.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_marker"]
        else:
            style = dict(color=colors[inst])
        
        fig.add_trace(go.Bar(x=TAB2.index, y=TAB2[inst], name=inst,marker=style), row=2, col=1)
        
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        # add mean
        fig.add_trace(go.Scatter(x=TAB1.index, y=TAB1.mean(axis=1), mode='lines', name="Durchschnitt",line=dict(color="black",dash="dash")), row=1, col=1)
        # add mean
        fig.add_trace(go.Bar(x=TAB2.index, y=TAB2.mean(axis=1),name="Durchschnitt",marker=dict(color="lightgray",pattern_shape="\\"),showlegend=False), row=2, col=1)
        
    fig.add_vrect(x0=start_fc.year-.5,
                x1=TAB1.index[-1]+.5,
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    xaxis2=dict(gridcolor='whitesmoke'),
                    yaxis1=dict(title=komponente.axis_title,tickformat=tickformat), 
                    yaxis2=dict(title="Q-o-Q Change (%)",tickformat=tickformat),paper_bgcolor='rgba(0, 0, 0, 0)')
    
    
    # add mean to tables (after plotting for recycling purposes) if specified
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        TAB1["Ø"] = TAB1.mean(axis=1)
        TAB2["Ø"] = TAB2.mean(axis=1)
        TAB3["Ø"] = TAB3.mean(axis=1)
    
    # Save Plotly figure as HTML div
    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')
    tables_level = [TAB1]
    tables_change = [TAB2,TAB3]
    
    # Define a dictionary with formatters for numerical columns
    formatters_level = {col: '{:,.0f}'.format for col in TAB1.columns}
    formatters_change = {col: '{:,.1f}'.format for col in TAB1.columns}
    html_tables = [df.to_html(classes='table-style-2', border=0, formatters=formatters_level) for df in tables_level]+[df.to_html(classes='table-style-2', border=0, formatters=formatters_change) for df in tables_change]

    return [komponente.title, plotly_html_div, html_tables]

def create_bws(komponente,synopse,settings):

    colors = settings.settings["colors"]
    tickformat = settings.settings["tickformat"]
    window_kf = settings.settings["window_kf"] 
    start_fc = pd.to_datetime(settings.settings["fc_start"])
    
    df,name = synopse.get_series(komponente.quarterly_series)
    df_change = df.pct_change(fill_method=None)

    TAB1,TAB2 = df.loc[window_kf,:].copy(),df_change.loc[window_kf,:].copy()*100
    TAB1plot,TAB2plot = TAB1.copy(),TAB2.copy()
    # Verkettete Volumenangaben (ksb) Mrd. Eur
    TAB1.index = TAB1.index.map(utils.format_quarter) 
    # q-q laufende Rate %
    TAB2.index = TAB2.index.map(utils.format_quarter)


    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Add traces
    for inst in TAB1plot.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_line"]
        else:
            style = dict(color=colors[inst])
        
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=style,showlegend=False), row=1, col=1)
    
        
    for inst in TAB2plot.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_marker"]
        else:
            style = dict(color=colors[inst])
        
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot[inst], name=inst,marker=style), row=2, col=1)
        
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        # add mean
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot.mean(axis=1), mode='lines', name="Durchschnitt",line=dict(color="black",dash="dash")), row=1, col=1)
        # add mean
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot.mean(axis=1),name="Durchschnitt",marker=dict(color="lightgray",pattern_shape="\\"),showlegend=False), row=2, col=1)
        
    fig.add_vrect(x0=start_fc-pd.Timedelta("15D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("45D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    xaxis2=dict(gridcolor='whitesmoke'),
                    yaxis1=dict(title="Mrd. Euro",tickformat=tickformat), 
                    yaxis2=dict(title="Q-o-Q Change (%)",tickformat=tickformat),paper_bgcolor='rgba(0, 0, 0, 0)')


    # Save Plotly figure as HTML div
    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    # add avg to TAB2 (after plotting for recycling purposes)
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        TAB1["Ø"] = TAB1.mean(axis=1)
        TAB2["Ø"] = TAB2.mean(axis=1)

    tables_Q = [TAB1,TAB2]

    # Define a dictionary with formatters for numerical columns
    formatters_Q = {col: '{:,.2f}'.format for col in TAB2.columns} # tab2 cause it has also the avg
    formatters_A = {col: '{:,.1f}'.format for col in TAB2.columns} # tab2 cause it has also the avg
    html_tables = [df.to_html(classes='table-style-2', border=0, formatters=formatters_Q) for df in tables_Q]
    
    
    return [komponente.title, plotly_html_div, html_tables]

def create_mittelfrist(komponente,synopse,settings):

    global TAB1

    colors = settings.settings["colors"]

    tickformat = settings.settings["tickformat"]
    window_kf = settings.settings["window_kf"] 
    window_mf = settings.settings["window_mf"] 
    start_fc = pd.to_datetime(settings.settings["fc_start"])

    df,name = synopse.get_series(komponente.annual_series)

    if "PP" in komponente.yaxis2:
        df_change = df.diff()
    elif komponente.title == "Totale Faktorproduktivität (TFP)": # special case handling
        df_change = df.apply(lambda x: np.exp(x)/np.exp(x.shift(1))-1, axis=0)*100
    else:
        df_change = df.pct_change(fill_method=None)*100

    TAB1,TAB2 = df.loc[window_mf,:],df_change.loc[window_mf,:]
    TAB1plot,TAB2plot = TAB1.copy(),TAB2.copy()
    # change index to year
    TAB1plot.index,TAB2plot.index = TAB1plot.index.year,TAB2plot.index.year 

    # handle special cases
    if komponente.title == "Produktionslücke":
        TAB2plot = TAB1plot

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1)

    # Add traces
    for inst in TAB1plot.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_line"]
        else:
            style = dict(color=colors[inst])
        
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=style,showlegend=False), row=1, col=1)
        
        
    for inst in TAB2plot.columns:
        
        if inst == "GD":
            style = settings.settings["prognose_style_marker"]
        else:
            style = dict(color=colors[inst])
        
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot[inst], name=inst,marker=style), row=2, col=1)
        
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        # add mean
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot.mean(axis=1), mode='lines', name="Durchschnitt",line=dict(color="black",dash="dash")), row=1, col=1)
        # add mean
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot.mean(axis=1),name="Durchschnitt",marker=dict(color="lightgray",pattern_shape="\\"),showlegend=False), row=2, col=1)
        
    fig.add_vrect(x0=start_fc.year-.5,
                    x1=TAB1plot.index[-1]+.5,
                    fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    xaxis2=dict(gridcolor='whitesmoke'),
                    yaxis1=dict(title=komponente.yaxis1,tickformat=",.0f"), 
                    yaxis2=dict(title=komponente.yaxis2,tickformat=",.2f"),)


    TAB1,TAB2 = df.loc[window_mf,:].copy(),df_change.loc[window_mf,:].copy()
    # change index to year
    TAB1.index,TAB2.index = TAB1.index.year,TAB2.index.year
    # get MIttelwert
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        TAB1["Ø"] = TAB1.mean(axis=1)
        TAB2["Ø"] = TAB2.mean(axis=1)

    title3 = f"Delta {TAB1.index[-1]}-{window_kf.stop[2:]}"
    TAB1_b = pd.DataFrame({f"{title3}":TAB1.iloc[-1,:] - TAB1.loc[int(window_kf.stop),:]})
    TAB1_b = TAB1_b.T
    TAB1_b.columns = TAB1.columns
    
    title4 = f"Ø Delta {TAB1.index[-1]}-{window_kf.stop[2:]}"
    TAB2_b = pd.DataFrame({f"{title4}":TAB2.loc[int(window_kf.stop):,:].mean(axis=0)})
    TAB2_b = TAB2_b.T
    TAB2_b.columns = TAB2.columns   

    # transpose 
    # TAB1,TAB2 = TAB1.T,TAB2.T
    
    # catching special cases
    if komponente.title == "Produktionslücke": 
        TAB2 = TAB1 # no changes for the ygap

    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')
    tables_level = TAB1,TAB1_b
    title1 = komponente.yaxis1
    tables_change = [TAB2,TAB2_b]
    title2 = komponente.yaxis2
    
    idx = [True,False]
    

    # Define a dictionary with formatters for numerical columns
    cols_collecter = list(TAB1.columns) + list(TAB1_b.columns)
    formatters_level = {col: '{:,.1f}'.format for col in cols_collecter}
    formatters_change = {col: '{:,.1f}'.format for col in cols_collecter}
    html_tables = [df.to_html(classes='table-style-2', border=0, formatters=formatters_level,index=i) for (df,i) in zip(tables_level,idx)]+[df.to_html(classes='table-style-2', border=0, formatters=formatters_change,index=i) for (df,i) in zip(tables_change,idx)]

    return [komponente.title, plotly_html_div, html_tables, [title1,title2,title3,title4]]


def create_annahmen_new(komponente,synopse,settings):

    colors = settings.settings["colors"]
    
    tickformat = settings.settings["tickformat"]
    window_kf = settings.settings["window_kf"] 
    window_ann = slice(f"{int(window_kf.start)-1}",window_kf.stop)
    
    # -- table 
    df,name = synopse.get_series(komponente.series)

    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        df["Ø"] = df.mean(axis=1)
        
    df = df.loc[window_ann]

    if komponente.series[0].lower() == "a":
        df.index = df.index.year
    else:
        df.index = df.index.map(utils.format_quarter) 

    # df = df.T
    
    # Define a dictionary with formatters for numerical columns
    formatters_Q = {col: '{:,.2f}'.format for col in df.columns}
    formatters_A = {col: '{:,.1f}'.format for col in df.columns}
    html_table = df.to_html(classes='table-style-2', border=0, formatters=formatters_Q)
    html_table = html_table.replace('\n', '')

    # -- plot
    dat1 = synopse.get_series(komponente.series)[0]
    TAB1plot = dat1.loc[window_kf,:]
    
    tickformat = settings.settings["tickformat"]
    window_kf = settings.settings["window_kf"] 
    start_fc = pd.to_datetime(settings.settings["fc_start"])
    
    fig1 = go.Figure()

    # Add traces
    for inst in [e for e in TAB1plot.columns if e!= "Ø"]:
        
        if inst == "GD":
            style = settings.settings["prognose_style_line"]
        else:
            style = dict(color=colors[inst])
            
        fig1.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=style,showlegend=True))
        
    
    if komponente.series[0].lower() == "a":
        fig1.add_vrect(x0=start_fc-pd.Timedelta("165D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("50D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
    else:
        fig1.add_vrect(x0=start_fc-pd.Timedelta("15D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("45D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        # add mean
        fig1.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot.mean(axis=1), mode='lines', name="Durchschnitt",line=dict(color="black",dash="dash")))
        
    # Update xaxis properties
    fig1.update_layout(plot.layout, 
                       title="<b>"+komponente.title,
                    barmode="group",
                    yaxis=dict(title=komponente.axis_title,tickformat=tickformat), 
                    height=400)
    
    # Save Plotly figure as HTML div
    plotly_html_div1 = fig1.to_html(full_html=False, include_plotlyjs='cdn')
    
    
    return [komponente.title, plotly_html_div1, html_table]

def get_halfyear_single(settings,synopse,quarterly_series,annual_series,change,window_hj):
    
    # -- hj
    hj = synopse.get_series(quarterly_series)[0].copy()
    # take changes to previous year if change
    if change == "Vorjahresvergleich":
        hj = hj.pct_change(periods=2,fill_method=None) * 100
    if change == "Differenz":
        hj = hj.diff(periods=2)
        
    # restrict to window
    hj = hj.loc[window_hj]
    # adjust index to Halbjahre
    hj.index = hj.index.map(lambda x: utils.format_hj(x))
    # add mean if specified
    if settings.settings["show_mean"]:
        hj["Ø"] = hj.mean(axis=1)

    hj = hj.T

    # -- annual
    annual = synopse.get_series(annual_series)[0].copy()
    # take changes to previous year if change
    if change == "Vorjahresvergleich":
        annual = annual.pct_change(periods=1,fill_method=None) * 100
    if change == "Differenz":
        annual = annual.diff(periods=1)
    
    # restrict to window
    annual = annual.loc[window_hj]
    # adjust index to Jahre
    annual.index = annual.index.year
    # add Institute
    if settings.settings["show_mean"]&(settings.settings["Prognose"]==False):
        annual["Ø"] = annual.mean(axis=1)

    annual = annual.T

    combined = []

    for yr in annual.columns:

        tmp = pd.concat([
            hj.filter(regex=f"{yr}"),annual.filter(regex=f"{yr}")	
        ],axis=1)
        combined.append(tmp)

    combined = pd.concat(combined, axis=1)

    return combined,hj,annual

def get_halfyear(settings,synopse,komponente,window_hj):
    
    
    if "Differenz" in komponente.yaxis:
        change = "Differenz"
    elif "Vorjahresvergleich" in komponente.yaxis:
        change = "Vorjahresvergleich" 
    else:
        change = None
    
    if len(komponente.quarterly_series.split("/"))>1:

        _,hj_num,annual_num = get_halfyear_single(settings,synopse,komponente.quarterly_series.split("/")[0].strip(),komponente.annual_series.split("/")[0].strip(),change,window_hj)
        _,hj_den,annual_den = get_halfyear_single(settings,synopse,komponente.quarterly_series.split("/")[1].strip(),komponente.annual_series.split("/")[1].strip(),change,window_hj)

        # calculate ratio
        combined = []
        for yr in annual_num.columns:

            tmp_num = pd.concat([
                hj_num.filter(regex=f"{yr}"),annual_num.filter(regex=f"{yr}")	
            ],axis=1)
            tmp_den = pd.concat([
                hj_den.filter(regex=f"{yr}"),annual_den.filter(regex=f"{yr}")	
            ],axis=1)


            combined.append(tmp_num / tmp_den)

        combined = pd.concat(combined, axis=1)


    else:
        combined,hj,annual = get_halfyear_single(settings,synopse,komponente.quarterly_series,komponente.annual_series,change,window_hj)


    return combined

def create_halbjahre(komponente,synopse,settings):
    
    
    window_kf = settings.settings["window_kf"] 
    window_hj = slice(f"{int(window_kf.start)-1}",window_kf.stop)

    combined = get_halfyear(settings,synopse,komponente,window_hj)
        
    if komponente.scaling:
        combined = combined * komponente.scaling
    
    # Define a dictionary with formatters for numerical columns
    form_string = '{:' + komponente.tickformat + '}'

    # Create the formatters dictionary
    formatters = {col: (lambda x, form=form_string: form.format(x)) for col in combined.columns}


    html_table = combined.to_html(classes='table table-striped small-font', border=0, formatters=formatters) 

    return [komponente.title, komponente.page_title, komponente.yaxis, html_table]


def create_mfp_pot_typ1(komponente,synopse,settings):

    colors = dict(zip(
        [settings.settings["GD"],settings.settings["GD(t-1)"]],
        ["dodgerblue","lightblue"] # settings.settings["colors"]
    ))
    tickformat = settings.settings["tickformat"]
    window_mf = settings.settings["window_mf"] 
    window_mf_plot = slice(komponente.start_yr,
                           settings.settings["window_mf"].stop)
    start_fc = pd.to_datetime(settings.settings["fc_start"])

    # -- TAB 1 | 2 | 4 | 6 --
    df,name = synopse.get_series(komponente.annual_series)
    df = df.rename(columns={
        "z":settings.settings["GD"],
        "y":settings.settings["GD(t-1)"],
    })

    df_change = df.pct_change(fill_method=None)
    TAB1,TAB2 = df.loc[window_mf_plot,:].dropna(how="all"),df_change.loc[window_mf_plot,:].dropna(how="all")
    TAB1plot,TAB2plot = TAB1.copy(),TAB2.copy()
    
    TAB1,TAB2 = df.loc[window_mf,:].dropna(how="all"),df_change.loc[window_mf,:].dropna(how="all")    
    TAB1.index,TAB2.index = TAB1.index.year,TAB2.index.year

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                        subplot_titles=(komponente.title1,komponente.title2))

    # Add traces
    for inst in TAB1plot.columns[::-1]:
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=dict(color=colors[inst]),showlegend=False), row=1, col=1)

    for inst in TAB2plot.columns[::-1]:
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot[inst], name=inst,marker=dict(color=colors[inst])), row=2, col=1)

    fig.add_vrect(x0=start_fc-pd.Timedelta("220D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("220D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    xaxis2=dict(gridcolor='whitesmoke'),
                    yaxis1=dict(title=komponente.yaxis_title1,tickformat=komponente.yaxis_format1), 
                    yaxis2=dict(title=komponente.yaxis_title2,tickformat=komponente.yaxis_format2),
                    paper_bgcolor='rgba(0, 0, 0, 0)')

    # Save Plotly figure as HTML div
    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    formatters_level = {col: '{:,.2f}'.format for col in TAB2.columns} 
    formatters_change = {col: '{:,.1%}'.format for col in TAB2.columns} 

    html_tables = [TAB1.to_html(classes='table-style-3', border=0, formatters=formatters_level), TAB2.to_html(classes='table-style-3', border=0, formatters=formatters_change)]

    return [komponente, plotly_html_div, html_tables]

def create_mfp_pot_typ2(komponente,synopse,settings):

    colors = dict(zip(
        [settings.settings["GD"],settings.settings["GD(t-1)"]],
        ["dodgerblue","lightblue"] # settings.settings["colors"]
    ))
    tickformat = settings.settings["tickformat"]
    window_mf = settings.settings["window_mf"] 
    window_mf_plot = slice(komponente.start_yr,
                           settings.settings["window_mf"].stop)
    start_fc = pd.to_datetime(settings.settings["fc_start"])
    
    # -- TAB 1 | 2 | 4 | 6 --
    df,name = synopse.get_series(komponente.annual_series)
    df = df.rename(columns={
        "z":settings.settings["GD"],
        "y":settings.settings["GD(t-1)"],
    })

    formatters = {col: '{:,.2f}'.format for col in df.columns} 

    if komponente.title1 == "Veränderung zum Vorjahr":
        df = df.pct_change(fill_method=None)
        formatters = {col: '{:,.1%}'.format for col in df.columns} 
        
    if ("quote" in komponente.title.lower())|("anteil" in komponente.title.lower()):
        formatters = {col: '{:,.1%}'.format for col in df.columns}

    TAB1 = df.loc[window_mf_plot,:].dropna(how="all")
    TAB1plot = TAB1.copy()
    
    TAB1 = df.loc[window_mf,:].dropna(how="all")
    TAB1.index = TAB1.index.year

    fig = go.Figure()

    # Add traces
    for inst in TAB1plot.columns[::-1]:
        if ("quote" in komponente.title.lower())|("anteil" in komponente.title.lower())|("eur" not in komponente.yaxis_title2.lower()):
            fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=dict(color=colors[inst]),showlegend=True))
        else:
            fig.add_trace(go.Bar(x=TAB1plot.index, y=TAB1plot[inst],  name=inst,marker=dict(color=colors[inst]),showlegend=True))

    fig.add_vrect(x0=start_fc-pd.Timedelta("220D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("220D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    yaxis1=dict(title=komponente.yaxis_title1,tickformat=komponente.yaxis_format1),
                    paper_bgcolor='rgba(0, 0, 0, 0)')

    # Save Plotly figure as HTML div
    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')
    
    html_tables = [TAB1.to_html(classes='table-style-3', border=0, formatters=formatters), None]

    return [komponente, plotly_html_div, html_tables]

def create_mfp_pot_typ3(komponente,synopse,settings):

    colors = dict(zip(
        ["potenziell","tatsächlich"],
        ["black","dodgerblue"] # settings.settings["colors"]
    ))
    tickformat = settings.settings["tickformat"]
    window_mf = settings.settings["window_mf"]
    window_mf_plot = slice(komponente.start_yr,settings.settings["window_mf"].stop)
    start_fc = pd.to_datetime(settings.settings["fc_start"])
    
    # geht nur auf z
    df1,name1 = synopse.get_series(komponente.annual_series[0])
    df2,name2 = synopse.get_series(komponente.annual_series[1])
    df1.drop(columns=["y"],inplace=True)
    df2.drop(columns=["y"],inplace=True)

    df = pd.concat([df1,df2],axis=1)
    df.columns = ["potenziell","tatsächlich"]

    df_change = df.pct_change(fill_method=None)
    TAB1,TAB2 = df.loc[window_mf_plot,:].dropna(how="all"),df_change.loc[window_mf_plot,:].dropna(how="all")
    TAB1plot,TAB2plot = TAB1.copy(),TAB2.copy()
    
    TAB1,TAB2 = df.loc[window_mf,:].dropna(how="all"),df_change.loc[window_mf,:].dropna(how="all")
    TAB1.index,TAB2.index = TAB1.index.year,TAB2.index.year

    fig = make_subplots(rows=2, cols=1, shared_xaxes=True, vertical_spacing=0.1,
                            subplot_titles=(komponente.title1,komponente.title2))

    # Add traces
    for inst in TAB1plot.columns[::-1]:
        fig.add_trace(go.Scatter(x=TAB1plot.index, y=TAB1plot[inst], mode='lines', name=inst,line=dict(color=colors[inst]),showlegend=False), row=1, col=1)

    for inst in TAB2plot.columns[::-1]:
        fig.add_trace(go.Bar(x=TAB2plot.index, y=TAB2plot[inst], name=inst,marker=dict(color=colors[inst])), row=2, col=1)

    fig.add_vrect(x0=start_fc-pd.Timedelta("220D"),
                x1=TAB1plot.index[-1]+pd.Timedelta("220D"),
                fillcolor="lightgray", opacity=0.5, layer="below", line_width=0,)
        
    # Update xaxis properties
    fig.update_layout(plot.layout, title="<b>"+komponente.title,
                    barmode="group",
                    xaxis2=dict(gridcolor='whitesmoke'),
                    yaxis1=dict(title=komponente.yaxis_title1,tickformat=komponente.yaxis_format1), 
                    yaxis2=dict(title=komponente.yaxis_title2,tickformat=komponente.yaxis_format2),paper_bgcolor='rgba(0, 0, 0, 0)')

    # Save Plotly figure as HTML div
    plotly_html_div = fig.to_html(full_html=False, include_plotlyjs='cdn')

    formatters_level = {col: '{:,.2f}'.format for col in TAB2.columns} 
    formatters_change = {col: '{:,.1%}'.format for col in TAB2.columns} 

    html_tables = [TAB1.to_html(classes='table-style-3', border=0, formatters=formatters_level), TAB2.to_html(classes='table-style-3', border=0, formatters=formatters_change)]

    return [komponente, plotly_html_div, html_tables]

def create_mfp_pot(komponente,synopse,settings):

    if isinstance(komponente.annual_series,list):
        return create_mfp_pot_typ3(komponente,synopse,settings)
    if komponente.yaxis_title2:
        return create_mfp_pot_typ1(komponente,synopse,settings)

    return create_mfp_pot_typ2(komponente,synopse,settings)




