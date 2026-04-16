import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Crypto Sentiment AI", layout="wide")

st.title("🎭 Crypto Sentiment Analysis Dashboard")
st.write("Análise em tempo real do sentimento do mercado via Processamento de Linguagem Natural (NLP).")

# Carregar os dados salvos pelo pipeline
df = pd.read_csv('data/sentiment_results.csv')

# Layout de Colunas para as métricas principais
col1, col2, col3 = st.columns(3)

with col1:
    total = len(df)
    st.metric("Total de Notícias", total)

with col2:
    bullish = len(df[df['sentiment'] == "Bullish (Positivo)"])
    st.metric("Manchetes Otimistas", bullish, delta=f"{bullish} un.")

with col3:
    bearish = len(df[df['sentiment'] == "Bearish (Negativo)"])
    st.metric("Manchetes Pessimistas", bearish, delta=f"-{bearish} un.", delta_color="inverse")

st.divider()

# Gráfico de Distribuição de Sentimento
st.subheader("📊 Distribuição do Sentimento")
sentiment_counts = df['sentiment'].value_counts()

fig, ax = plt.subplots(figsize=(10, 4))
sentiment_counts.plot(kind='barh', color=['gray', 'red', 'green'], ax=ax)
ax.set_xlabel("Quantidade de Notícias")
st.pyplot(fig)

# Tabela Interativa
st.subheader("📰 Detalhes das Notícias e Scores de IA")
st.dataframe(df[['score', 'sentiment', 'text']], use_container_width=True)

st.info("💡 Dica: Scores próximos a 1.0 são altamente positivos. Próximos a -1.0 são altamente negativos.")