# 🚗📊 Mercado Livre x FIPE Hunter — Descoberta de Oportunidades de Compra

Este projeto tem como objetivo automatizar a análise de oportunidades de compra no mercado de veículos/produtos, comparando preços anunciados no **Mercado Livre** com a referência oficial da **Tabela FIPE**.

A ideia central é identificar produtos abaixo do valor de mercado e gerar **insights de compra inteligente**.

---

## 🚀 Objetivo do projeto

- Coletar dados de anúncios do Mercado Livre
- Normalizar e estruturar informações com IA
- Consultar valores da Tabela FIPE como referência
- Comparar preços automaticamente
- Identificar **oportunidades de compra abaixo do valor de mercado**
- Gerar insights para decisões mais inteligentes

---

## 🧠 Como funciona

O pipeline do sistema funciona em etapas:

### 1. 📡 Coleta de dados (Scraping)
- Utiliza **Scrapy**
- Utiliza **Playwright** para sites dinâmicos
- Extrai dados como:
  - Nome do produto
  - Preço
  - Modelo
  - Link do anúncio
  - Informações do vendedor

---

### 2. 🤖 Processamento com IA
- Integração com **OpenAI API**
- Normaliza dados inconsistentes
- Extrai informações estruturadas de textos
- Padroniza nomes de produtos e modelos

---

### 3. 📊 Integração com FIPE
- Consulta valores de referência da Tabela FIPE
- Compara preço do anúncio vs valor de mercado
- Calcula diferença percentual

---

### 4. 💡 Geração de oportunidades
O sistema identifica oportunidades como:

- Produto abaixo da FIPE (ex: -20%, -30%, -50%)
- Possível revenda com margem
- Alertas de preço abaixo do mercado

---

## ⚙️ Tecnologias utilizadas

- Python 3.x  
- Scrapy  
- Playwright  
- OpenAI API  
- pandas  
- FIPE API / dataset  
- asyncio  

---

---

## ▶️ Como executar

### 1. Instalar dependências
bash
pip install scrapy playwright openai pandas

2. Instalar navegador do Playwright
playwright install

4. Rodar o scraper
scrapy crawl excel

6. Executar análise de oportunidades
python -m email_sender

📊 Exemplo de resultado
{
  "produto": "Honda Civic 2020",
  "preco_anuncio": 85000,
  "preco_fipe": 95000,
  "diferenca": -10.5,
  "oportunidade": true
}
