import feedparser
import pandas as pd

def fetch_crypto_news():
    # RSS do CoinTelegraph (um dos maiores portais de cripto)
    url = "https://cointelegraph.com/rss/tag/bitcoin"
    feed = feedparser.parse(url)
    
    news_data = []
    
    for entry in feed.entries:
        news_data.append({
            "title": entry.title,
            "link": entry.link,
            "published": entry.published
        })
    
    return pd.DataFrame(news_data)

if __name__ == "__main__":
    print("📡 Coletando notícias do CoinTelegraph...")
    df_news = fetch_crypto_news()
    if not df_news.empty:
        print(f"✅ {len(df_news)} notícias encontradas!")
        print(df_news[['title']].head())
    else:
        print("❌ Nenhuma notícia encontrada. Verifique a conexão.")