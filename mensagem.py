import requests
import processar_eventos

#   Crie um bot no Telegram através do BotFather e insira o token abaixo
bot_token = "7704652779:AAE1Plz26DNlzC8NSB-CHJFc1T-75kOoKAc"
chat_id = "837174968"  # ID do chat ou grupo para onde a mensagem será enviada
mensagem = "Arquivo atualizado com sucesso! \nAcesse as atualizacoes em: https://chatgpt.com/g/g-p-68792803187481918ffd190415b3eccb-foco-radical/project "

url = f"https://api.telegram.org/bot{bot_token}/sendMessage"

payload = {
    "chat_id": chat_id,
    "text": mensagem
}

try:
    response = requests.post(url, data=payload)
    if response.status_code == 200:
        print("Mensagem enviada com sucesso no Telegram!")
    else:
        print(f"Falha ao enviar mensagem. Código: {response.status_code}, Resposta: {response.text}")
except Exception as e:
    print(f"Erro ao enviar mensagem: {e}")
