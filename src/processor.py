from textblob import TextBlob
import pandas as pd

class SentimentAnalyzer:
    def __init__(self):
        print("🤖 Analisador de Sentimentos Inicializado")

    def analyze_list(self, text_list):
        results = []
        for text in text_list:
            blob = TextBlob(text)
            polarity = blob.sentiment.polarity
            
            if polarity > 0.1:
                label = "Bullish (Positivo)"
            elif polarity < -0.1:
                label = "Bearish (Negativo)"
            else:
                label = "Neutral (Neutro)"
                
            results.append({
                "text": text,
                "score": round(polarity, 2),
                "sentiment": label
            })
        
        return pd.DataFrame(results)

# Pequeno teste interno
if __name__ == "__main__":
    test_news = [
        "Bitcoin hits new all-time high as institutional adoption grows",
        "Regulators are considering a ban on crypto mining in some regions",
        "The market is moving sideways with low volume today"
    ]
    analyzer = SentimentAnalyzer()
    df = analyzer.analyze_list(test_news)
    print(df)