from ingestion import fetch_crypto_news
from processor import SentimentAnalyzer
import os

def run_pipeline():
    # 1. Coleta
    print("📡 Passo 1: Coletando notícias...")
    df_news = fetch_crypto_news()
    
    if df_news.empty:
        print("❌ Falha na coleta.")
        return

    # 2. Processamento
    print("🧠 Passo 2: Analisando sentimentos...")
    analyzer = SentimentAnalyzer()
    
    # Aplicamos a análise na coluna 'title' que veio do RSS
    df_analisado = analyzer.analyze_list(df_news['title'].tolist())
    
    # 3. Merge e Salvamento
    # Adicionamos a data de publicação original ao resultado
    df_analisado['published'] = df_news['published']
    
    # Criamos a pasta data se não existir
    if not os.path.exists('data'):
        os.makedirs('data')
        
    df_analisado.to_csv('data/sentiment_results.csv', index=False)
    print("✅ Pipeline finalizado! Resultados salvos em data/sentiment_results.csv")
    print("\nResumo do Sentimento do Mercado:")
    print(df_analisado['sentiment'].value_counts())

if __name__ == "__main__":
    run_pipeline()