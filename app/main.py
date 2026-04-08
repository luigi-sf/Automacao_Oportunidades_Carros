import schedule
import time
import subprocess
from excel.utils.analisar_excel import analisar
from excel.utils.email_sender import enviar_email
import os
import sys
import shutil


def mover_carros_para_data():
    # Detecta o ambiente
    if os.path.exists("/app"):  # Docker
        origem = "/app/app/excel/carros.xlsx"
        destino = "/app/data/carros.xlsx"
    else:  # Windows local
        origem = os.path.join(os.path.dirname(__file__), "excel", "carros.xlsx")
        destino = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "carros.xlsx")
    
    # Move o arquivo se existir
    if os.path.exists(origem):
        os.makedirs(os.path.dirname(destino), exist_ok=True)
        shutil.move(origem, destino)
        print(f"📁 Arquivo movido: {origem} -> {destino}")
        return True
    else:
        print(f"⚠️ Arquivo não encontrado: {origem}")
        return False


def rodar_scrapy():
    # Detecta se está rodando no Docker ou local
    if os.path.exists("/app"):  # Está no Docker (Linux)
        excel_dir = "/app/app/excel"
    else:  # Está no Windows (local)
        excel_dir = os.path.join(os.path.dirname(__file__), "excel")
    
    print(f"📂 Executando Scrapy em: {excel_dir}")
    subprocess.run([sys.executable, "-m", "scrapy", "crawl", "excel"], cwd=excel_dir)


def rodar_analise():
    print("📊 Rodando análise...")
    
    # Move o arquivo da pasta excel para data
    mover_carros_para_data()
    
    arquivo, total = analisar()

    if arquivo:
        enviar_email(arquivo, total)
        print(f"📩 Email enviado com {total} oportunidades")
    else:
        print("⚠️ Nenhuma oportunidade")


# EXECUÇÃO IMEDIATA
print("🚀 Rodando execução inicial...")
rodar_scrapy()
time.sleep(10)  # espera scraping começar
rodar_analise()


# AGENDAMENTO

# scraping 1x por dia
schedule.every().day.at("09:00").do(rodar_scrapy)

# análise a cada 1h
schedule.every(1).hours.do(rodar_analise)


print("⏰ Automação iniciada...")

while True:
    schedule.run_pending()
    time.sleep(5)