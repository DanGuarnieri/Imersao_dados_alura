import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da Página
#Define o título da página, o ícone e o layout para ocupar a largura inteira.

st.set_page_config(
    page_title="Dashboard de Salários na Área de Dados",
    page_icon="🎲",
    layout="wide"
)
caminho = r"C:\Users\Guarnieri\Desktop\python\Imersao_dados_alura\dados-imersao-final.csv"
#Leitura do arquivo Base
df = pd.read_csv(caminho)


#Barra Lateral (Filtros)
st.sidebar.header("🔍 Filtros")

#Filtro de Ano
anos_disponiveis = sorted(df['ano'].unique())
anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

#Filtro de Senioridade
senioridades_disponiveis = sorted(df['senioridade'].unique())
senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

#Filtro por Tipo de Contrato
contratos_disponiveis = sorted(df['contrato'].unique())
contratos_selecionados = st.sidebar.multiselect("Contrato", contratos_disponiveis, default=contratos_disponiveis)

#Filtro por Tamanho da empresa
tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

# Filtragem do DataFrame

df_filtrado = df[
    (df['ano'].isin(anos_selecionados)) &
    (df['senioridade'].isin(senioridades_selecionadas)) &
    (df['contrato'].isin(contratos_selecionados)) & 
    (df['tamanho_empresa'].isin(tamanhos_selecionados))
]

# Conteúdo Principal
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")
st.markdown("Explore os dados salariais na área de dados nos últimos anos. Utilize os filtros à esquerda para refinar a sua análise.")

#KPIs

st.subheader("Métricas gerais (Salário Anual em USD)")

if not df_filtrado.empty:
    salario_medio = df_filtrado['usd'].mean()
    salario_maximo = df_filtrado['usd'].max()
    salario_minimo = df_filtrado['usd'].min()
    total_registros = df_filtrado.shape[0]
    cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
else:
    salario_medio, salario_minimo, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, 0, "" 

col1, col2, col3, col4, col5 = st.columns(5)
col1.metric("Salário Médio", f"${salario_medio:,.0f}")
col2.metric("Salário Máximo", f"${salario_maximo:,.0f}")
col3.metric("Salário Mínimo", f"${salario_minimo:,.0f}")
col4.metric("Total de Registros", f'{total_registros:}')
col5.metric("Cargo mais frequente", cargo_mais_frequente)

st.markdown("---")

st.subheader("Gráficos")

col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    if not df_filtrado.empty:
        top_cargos = df_filtrado.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        grafico_cargos = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': "Média Salarial anual (USD)", 'cargo': ''}
        )
        grafico_cargos.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico_cargos, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos")


with col_graf2:
    if not df_filtrado.empty:
        grafico_hist = px.histogram(
            df_filtrado,
            x='usd',
            nbins=30,
            title="Distribuição de Salários anuais",
            labels={'usd': "Faixa salarial (USD)", 'count': ''}
        )
        grafico_hist.update_layout(title_x=0.1)
        st.plotly_chart(grafico_hist, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição")


col_graf3, col_graf4 = st.columns(2)

with col_graf3:
    if not df_filtrado.empty:
        remoto_contagem = df_filtrado['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        grafico_remoto = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title="Proporção dos tipos de trabalho",
            hole=0.5
        )
        grafico_remoto.update_traces(textinfo='percent+label')

        grafico_remoto.update_layout(title_x=0.1)
        st.plotly_chart(grafico_remoto, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho")


with col_graf4:
    if not df_filtrado.empty:
        data_scientist_region = df[df['cargo'] == 'Data Scientist']
        media_ds_pais = data_scientist_region.groupby('residencia_iso3')['usd'].mean().sort_values(ascending=False).reset_index()
        fig = px.choropleth(media_ds_pais,
                    locations='residencia_iso3',
                    color='usd',
                    color_continuous_scale='rdylgn',
                    title="Média Salarial por Pais para Data Scientist",
                    labels={'residencia' : 'País', 'usd': 'Média Salarial Anual (USD)'})
        fig.update_layout(title_x=0.1)
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição")

st.subheader("Dados Detalhados")

#Exibir dataframe, mas, convertendo exibição do ano para texto, para não aparecer 2,025
st.dataframe(
    df_filtrado,
    column_config={
        "ano": st.column_config.TextColumn("Ano")
    }
)
