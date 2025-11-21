import boto3
import os

# ============================================================
#  BUSCA AS CREDENCIAIS NAS VARIÁVEIS DE AMBIENTE DO WINDOWS
# ============================================================
ACCESS_KEY = os.getenv("AWS_KEY")  # sua chave pública
SECRET_KEY = os.getenv("AWS_SECRET")  # sua chave secreta
REGION = "sa-east-1"  # São Paulo
TOPIC_ARN = "arn:aws:sns:sa-east-1:776010787681:farmtech-alertas"


# ============================================================
#  MONTA A MENSAGEM DO ALERTA
# ============================================================
def montar_mensagem_alerta(umidade, ph, fosforo, potassio):
    recomendacoes = []

    if umidade < 30:
        recomendacoes.append("Umidade baixa: recomendado acionar a irrigação.")
    elif umidade > 80:
        recomendacoes.append("Umidade muito alta: avaliar drenagem ou reduzir irrigação.")

    if ph < 5.5:
        recomendacoes.append("pH ácido: considerar calagem (correção com calcário).")
    elif ph > 7.5:
        recomendacoes.append("pH alcalino: avaliar correção para reduzir alcalinidade.")

    if fosforo.lower() == "ausente":
        recomendacoes.append("Fósforo ausente: recomendar adubação fosfatada.")
    if potassio.lower() == "ausente":
        recomendacoes.append("Potássio ausente: recomendar adubação potássica.")

    if not recomendacoes:
        recomendacoes.append("Todos os parâmetros estão dentro da faixa ideal. Manter monitoramento.")

    recomendacoes_txt = "\n- ".join(recomendacoes)

    mensagem = (
        "ALERTA DE MONITORAMENTO - FARMTECH SOLUTIONS\n\n"
        "Leitura atual dos sensores:\n"
        f"- Umidade: {umidade:.2f}%\n"
        f"- pH: {ph:.2f}\n"
        f"- Fósforo: {fosforo}\n"
        f"- Potássio: {potassio}\n\n"
        "Ações recomendadas:\n"
        f"- {recomendacoes_txt}"
    )

    return mensagem


# ============================================================
#  ENVIA ALERTA PARA O SNS
# ============================================================
def enviar_alerta_aws(umidade, ph, fosforo, potassio):
    # Validação: se as credenciais não existirem, avisa no console
    if ACCESS_KEY is None or SECRET_KEY is None:
        print("\n[ERRO] Credenciais AWS não encontradas nas variáveis de ambiente!")
        print("Crie as variáveis AWS_KEY e AWS_SECRET no seu sistema.\n")
        return

    try:
        # Criação do cliente SNS com as credenciais carregadas
        sns = boto3.client(
            "sns",
            region_name=REGION,
            aws_access_key_id=ACCESS_KEY,
            aws_secret_access_key=SECRET_KEY
        )

        mensagem = montar_mensagem_alerta(umidade, ph, fosforo, potassio)

        response = sns.publish(
            TopicArn=TOPIC_ARN,
            Subject="Alerta de Sensores - FarmTech Solutions",
            Message=mensagem
        )

        print("\n[✓] Alerta enviado para o AWS SNS com sucesso!")
        print(f"MessageId: {response.get('MessageId')}\n")

    except Exception as e:
        print("\n[ERRO AO ENVIAR ALERTA]")
        print(e)
        print()
