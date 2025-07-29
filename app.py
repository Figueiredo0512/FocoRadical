import streamlit as st
import pandas as pd
import datetime

# URL pública do CSV no GitHub
csv_url = 'https://raw.githubusercontent.com/Figueiredo0512/FocoRadical/main/eventos_foco.csv'

# Carrega o DataFrame
df = pd.read_csv(csv_url)

# Converte a data para datetime (de dd-mm-yyyy para datetime)
df['data'] = pd.to_datetime(df['data'], format='%d-%m-%Y', errors='coerce')

# Marca eventos passados ou futuros
hoje = pd.to_datetime(datetime.date.today())
df['status'] = df['data'].apply(lambda x: 'Futuro' if x >= hoje else 'Passado')

# Cria uma coluna de score simples (ajuste conforme quiser)
def calcular_score(row):
    score = 0
    if row['fotografos'] == 0:
        score += 3
    if 'MTB' in str(row['categoria']).upper() or 'TRAIL' in str(row['categoria']).upper():
        score += 2
    if row['estado'] in ['SP', 'MG']:
        score += 1
    return score

df['score'] = df.apply(calcular_score, axis=1)

# Sidebar de filtros
st.sidebar.title("Filtros")
estado = st.sidebar.selectbox("Estado", options=["Todos"] + sorted(df['estado'].dropna().unique().tolist()))
categorias = st.sidebar.multiselect("Categorias", df['categoria'].dropna().unique().tolist())
status = st.sidebar.radio("Status do Evento", options=['Todos', 'Futuro', 'Passado'], index=1)

# Aplica filtros
filtro = df.copy()
if estado != "Todos":
    filtro = filtro[filtro['estado'] == estado]
if categorias:
    filtro = filtro[filtro['categoria'].isin(categorias)]
if status != "Todos":
    filtro = filtro[filtro['status'] == status]

# Ordena por score (melhores oportunidades primeiro)
filtro = filtro.sort_values(by='score', ascending=False)

# Layout principal
st.title("📸 Painel de Eventos - Foco Radical")
st.markdown("### Eventos com maior potencial de venda")
st.dataframe(filtro.reset_index(drop=True))

# Gráfico de distribuição por categoria
st.markdown("### Distribuição por Categoria")
st.bar_chart(filtro['categoria'].value_counts())

# Gráfico de número de fotógrafos
st.markdown("### Número de Fotógrafos por Evento")
st.bar_chart(filtro['fotografos'].value_counts().sort_index())

# Créditos ou rodapé
st.markdown("---")
st.caption("Projeto colaborativo Gepeto & ChatGPT - Dados extraídos via script Python do Foco Radical")
