import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv() 

def enviar_email(arquivo, total=0):
    try:
        # CREDENCIAIS
        email_remetente = os.getenv("EMAIL_REMETENTE")
        senha = os.getenv("SUA_SENHA_APP")
        email_destino = os.getenv("EMAIL_DESTINO")
        
        # Verifica se as credenciais existem
        if not email_remetente or not senha or not email_destino:
            print("❌ Credenciais de email não encontradas no .env")
            print(f"   EMAIL_REMETENTE: {'OK' if email_remetente else 'FALTANDO'}")
            print(f"   SUA_SENHA_APP: {'OK' if senha else 'FALTANDO'}")
            print(f"   EMAIL_DESTINO: {'OK' if email_destino else 'FALTANDO'}")
            return False
        
        # CABECALHO
        msg = EmailMessage()
        msg["Subject"] = f"🚗 {total} Oportunidades abaixo da FIPE encontradas!"
        msg["From"] = email_remetente
        msg["To"] = email_destino

        # BODY 
        msg.set_content(f"""
🚨 RELATÓRIO DE OPORTUNIDADES - CARROS 🚗

🔥 {total} oportunidades encontradas abaixo da FIPE!

Critérios utilizados:
✔ Preço abaixo da tabela FIPE
✔ Desconto mínimo de 10%
✔ Quilometragem até 80.000 km
✔ Ano a partir de 2018

📊 O arquivo em anexo contém os melhores carros encontrados hoje.

⏱ Este relatório é gerado automaticamente.

Fique atento — essas oportunidades somem rápido!

---
Sistema automático de monitoramento 🚀
""")

        # ANEXO
        if not os.path.exists(arquivo):
            print(f"❌ Arquivo não encontrado: {arquivo}")
            return False
        
        with open(arquivo, "rb") as f:
            msg.add_attachment(
                f.read(),
                maintype="application",
                subtype="vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                filename=os.path.basename(arquivo)
            )

        # ENVIO
        print("📧 Conectando ao Gmail...")
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            print("📧 Fazendo login...")
            smtp.login(email_remetente, senha)
            print("📧 Enviando email...")
            smtp.send_message(msg)
        
        print("✅ Email enviado com sucesso! 📧")
        return True
        
    except Exception as e:
        print(f"❌ Erro ao enviar email: {e}")
        return False