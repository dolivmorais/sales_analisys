#%%
from dash import html, dcc, Input, Output
import dash_bootstrap_components as dbc
import plotly_express as px
import plotly.graph_objects as go
import pandas as pd

from dash_bootstrap_templates import ThemeChangerAIO
import dash

df = pd.read_csv("dataset_asimov.csv")

df
#%%
df.loc[df['Mês'] == "Jan", "Mês"] = 1
df.loc[df['Mês'] == "Fev", "Mês"] = 2
df.loc[df['Mês'] == "Mar", "Mês"] = 3
df.loc[df['Mês'] == "Abr", "Mês"] = 4
df.loc[df['Mês'] == "Mai", "Mês"] = 5
df.loc[df['Mês'] == "Jun", "Mês"] = 6
df.loc[df['Mês'] == "Jul", "Mês"] = 7
df.loc[df['Mês'] == "Ago", "Mês"] = 8
df.loc[df['Mês'] == "Set", "Mês"] = 9
df.loc[df['Mês'] == "Out", "Mês"] = 10
df.loc[df['Mês'] == "Nov", "Mês"] = 11
df.loc[df['Mês'] == "Dez", "Mês"] = 12

df
#%%
df['Chamadas Realizadas'] = df['Chamadas Realizadas'].astype(int)
df['Dia'] = df['Dia'].astype(int)
df['Mês'] = df['Mês'].astype(int)

df['Valor Pago'] = df['Valor Pago'].str.lstrip('R$ ')
df['Valor Pago'] = df["Valor Pago"].astype(int)

df
# %%
df.loc[df['Status de Pagamento'] == 'Pago','Status de Pagamento'] = 1
df.loc[df['Status de Pagamento'] ==  'Não pago', 'Status de Pagamento'] = 0
          
df
# %%
df1 = df.groupby('Equipe') ['Valor Pago'].sum().reset_index()

df1

fig1 = go.Figure(go.Bar(
    x=df1['Valor Pago'],
    y=df1['Equipe'],
    orientation='h',
    textposition='auto',
    text=df1['Valor Pago'],
    insidetextfont=dict(family='Times', size=12)
))

fig1.show()



# %%
