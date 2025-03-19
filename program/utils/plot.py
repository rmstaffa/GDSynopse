import plotly.express as px
import plotly as py
import plotly.graph_objs as go
from plotly.subplots import make_subplots

layout = go.Layout(
    yaxis=dict(showgrid=True,gridcolor='whitesmoke'),
    xaxis=dict(showgrid=True,gridcolor='whitesmoke'),
    paper_bgcolor='rgba(255,255,255,255)',
    plot_bgcolor='rgba(255,255,255,255)',
    legend=dict(bgcolor='whitesmoke',
                bordercolor='lightgray',
                borderwidth=1, orientation="h"),
    barmode='stack',
    hovermode='x',
    modebar_add=[
    "toggleSpikelines",
],font=dict(
        family="Constantia"
    ))