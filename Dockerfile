FROM python:3.11-slim

WORKDIR /app

# Instalando apenas o essencial para compilar pacotes se necessário
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Baixando os recursos do NLTK/TextBlob
RUN python -m textblob.download_corpora

COPY . .

EXPOSE 8501

# Usando o formato JSON para o CMD (evita o warning que apareceu no seu log)
CMD ["sh", "-c", "python src/main.py && streamlit run src/app.py --server.port=8501 --server.address=0.0.0.0"]