# 🎭 Crypto Sentiment AI

Este projeto utiliza Inteligência Artificial e NLP para monitorar o "humor" do mercado de criptoativos em tempo real. Ele automatiza a coleta de manchetes de notícias e aplica modelos de análise de sentimento para quantificar se o cenário atual é de euforia (Bullish) ou pânico (Bearish). É um pipeline de dados completo que transforma texto não-estruturado em indicadores financeiros acionáveis.

## 🚀 Funcionalidades
- **Ingestão de Dados (NLP):** Coleta automatizada de manchetes em tempo real via RSS Feeds (CoinTelegraph).
- **Análise de Sentimento:** Processamento de linguagem natural utilizando a biblioteca **TextBlob** para cálculo de polaridade.
- **Pipeline Modular:** Separação clara entre coleta, processamento de texto e visualização.
- **Dashboard Interativo:** Interface em Streamlit com métricas de sentimento e distribuição de scores.
- **Containerização:** Totalmente preparado com Docker para garantir que o ambiente de NLP seja idêntico em qualquer máquina.

## 🛠️ Tecnologias Utilizadas
- **Python 3.13**
- **TextBlob & NLTK**: Para processamento de linguagem natural e análise de sentimento.
- **Feedparser**: Para extração de dados de fontes de notícias.
- **Pandas**: Para manipulação e estruturação dos dados processados.
- **Streamlit**: Para a criação do dashboard visual.
- **Docker**: Para deploy simplificado e isolamento de dependências.

## 🧠 Diferenciais Técnicos
- **Tratamento de Dados Não-Estruturados**: Conversão de texto bruto em dados quantitativos (Polarity Scores).
- **Arquitetura Modular**: CScripts independentes para `ingestion`, `processor` e `app`, facilitando a manutenção.
- **Métricas MLOps**: O pipeline executa a atualização dos dados automaticamente ao iniciar o container.

## 🛠️ Como Executar
1. Clone o repositório: `git clone [https://github.com/AndersonBHBR/sentiment-analysis-ai.git](https://github.com/AndersonBHBR/sentiment-analysis-ai.git) cd sentiment-analysis-ai`
2. Construa a imagem Docker: `docker build -t sentiment-analysis-ai .`
3. Execute o container: `docker run -p 8501:8501 sentiment-analysis-ai`
4. Acesse o dashboard: Abra o navegador em `http://localhost:8501`.

## 🙋 Sobre o Autor

Feito com 💻 e ☕ por [Anderson Lima Araújo](https://www.linkedin.com/in/anderson-araujo-pcd)😊  
Sou desenvolvedor Full Stack com foco em IA, APIs modernas, soluções web escaláveis e interesse em projetos internacionais 🌍
<p>
    <img align=left margin=10 width=80 src="https://avatars.githubusercontent.com/u/7528140?v=4"/>
    <p>&nbsp&nbsp&nbspAnderson Lima Araújo<br>
    &nbsp&nbsp&nbsp<a href="http://instagram.com/andersonbhbr">Instagram</a>&nbsp;|&nbsp;<a href="https://github.com/AndersonBHBR">GitHub</a>&nbsp;|&nbsp;<a href="https://www.linkedin.com/in/anderson-araujo-pcd/">LinkedIn</a>&nbsp;|&nbsp;<a href="https://www.behance.net/andersonbhbr">Behance</a></p>
</p>
<br/><br/>
