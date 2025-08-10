# 📊 Imersão de Dados com Python — Alura

Este repositório reúne o conteúdo e os códigos desenvolvidos durante a **Imersão de Dados com Python da Alura**.
O objetivo foi aprender a manipular, limpar, visualizar e apresentar dados de forma interativa, utilizando **Python** e bibliotecas voltadas para análise e visualização.

---

## 📅 Estrutura das Aulas

A imersão foi dividida em **4 etapas principais**:

### **Aula 1 — Explore dados com Pandas**

- Leitura de bases de dados (`.csv`, `.xlsx`, etc.).
- Uso do `pandas` para inspeção e exploração inicial dos dados.
- Estatísticas descritivas (`.describe()`, `.value_counts()`).
- Seleção e filtragem de dados.

---

### **Aula 2 — Limpeza e preparação dos dados**

- Tratamento de valores ausentes (`NaN`).
- Padronização de formatos de texto, datas e números.
- Conversão de tipos de dados (`astype()`).
- Criação de novas colunas derivadas.
- Remoção e tratamento de dados inconsistentes.

---

### **Aula 3 — Visualização e storytelling com dados**

- Uso do `matplotlib`, `seaborn` e `plotly.express` para gráficos.
- Criação de histogramas, gráficos de barras e gráficos de pizza.
- Ajuste de títulos, legendas e escalas.
- Técnicas para contar histórias com dados de forma clara e envolvente.

---

### **Aula 4 — Dashboard interativo**

- Desenvolvimento de um dashboard com **Streamlit**.
- Adição de filtros interativos (multiselect, slider).
- KPIs dinâmicos com `st.metric`.
- Exibição de gráficos interativos com Plotly.
- Publicação do dashboard para acesso online.

---

## 🛠 Tecnologias Utilizadas

- **Python 3.x**
- **Pandas** — manipulação de dados.
- **Plotly Express** — visualização interativa.
- **Matplotlib** — visualização estática.
- **Streamlit** — criação do dashboard.
- **Jupyter Notebook** — exploração e testes.

---

## 🚀 Como Executar

1. Clone este repositório:
   ```bash
   git clone https://github.com/DanGuarnieri/Imersao_dados_alura.git

   ```
2. Entre na pasta do projeto
   ```bash
   cd imersao-dados-alura
   ```
3. Criar e Ativar o ambiente virtual (Windows)
   ```bash
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```
4. Instale as dependências
   ```bash
   pip install -r requirements.txt
   ```
5. Para rodar o dashboard:
   ```bash
   streamlit run app.py
   ```

---

## ✨ Resultado Final

O projeto final é um Dashboard Interativo de Análise Salarial que permite filtrar dados, visualizar métricas e explorar gráficos dinâmicos, contando a história dos dados de forma visual e intuitiva.
