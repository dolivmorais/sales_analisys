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
df2 = df.groupby('Dia')['Chamadas Realizadas'].sum().reset_index()

df2

fig2 = go.Figure(go.scatter(
        x=df2['Dia'],
        y=df2['Chamadas Realizadas'], mode='lines',fill='tozeroy')
)

fig2.add_annotation(text='Chamadas Médias por dia do Mês',
                    xref='paper', yref='paper',
                    font=dict(
                        size=20,
                        color='gray'
                    ),          

                    align="center",bgcolor="rgba(0,0,0,0.8)",
                    x=0.5, y=0.85, showarrow=False)
fig2.add_annotation(text=f"Média: {round(df2["Chamadas Realizadas"].mean(), 2)}",
                    xref="paper", yref="paper",
                    font=dict(
                        size=30,
                        color='gray'
                    ),
                    align="center",bgcolor="rgba(0,0,0,0.8)",
                    x=0.5, y=0.85, showarrow=False)

fig2.show()

#%%
df4 = df.groupby('Mês')['Chamadas Realizadas'].sum().reset_index()
df4

fig4 = go.Figure(go.Scatter(
    x=df4['Mês'], y=df4['Chamadas Realizadas'], mode='lines', fill='tozeroy'))

fig4.add_annotation(text="Chamadas Médias por Mês",
                    xref="paper", yref="paper",
                    font=dict(
                        size=15,
                        color='gray'
                    ),
                    align="center", bgcolor="rgba(0,0,0,0.8)",
                    x=0.05, y=0.85, showarrow=False)
fig4.add_annotation(text=f"Média: {round(df4['Chamadas Realizadas'].mean(),2)}",
                    xref="paper", yref="paper",
                    font=dict(
                        size=30,
                        color='gray'
                    ),
                    align="center", bgcolor="rgba(0,0,0,0.8)",
                    x=0.05, y=0.50, showarrow=False)

fig4.show()
# %%
df3 = df.groupby(['Meio de Propaganda', 'Mês'])['Valor Pago'].sum().reset_index()
df3

fig3 = px.line(df3, y="Valor Pago", x="Mês", color="Meio de Propaganda")
fig3.show()

# %%
df11 = df.groupby("Meio de Propaganda")["Valor Pago"].sum().reset_index()
df11

fig11 = go.Figure()
fig11.add_trace(go.Pie(labels=df11["Meio de Propaganda"], values=df11["Valor Pago"], hole=.7))

fig11.show()
# %%

df5 = df.groupby(['Mês', 'Equipe'])['Valor Pago'].sum().reset_index()
df5_group = df.groupby('Mês')["Valor Pago"].sum().reset_index()

fig5 = px.line(df5, y="Valor Pago", x="Mês", color="Equipe")
fig5.add_trace(go.Scatter(y=df5_group["Valor Pago"], x=df5_group["Mês"], mode='lines+markers', fill='tozeroy', fillcolor='rgba(255,0,0,0.2)'))


# %%
df6 = df.groupby('Status de Pagamento')['Chamadas Realizadas'].sum()

fig6 = go.Figure()
fig6.add_trace(go.Pie(labels=['Não Pago', 'Pago'], values=df6, hole=.6))
fig6.show()

#%%
# gerando grafico ...continuar 6:58