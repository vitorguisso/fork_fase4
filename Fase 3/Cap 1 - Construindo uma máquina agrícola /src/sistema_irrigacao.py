#GRUPO
#RyanCarlos_RM561677_fase3_cap1
#ViniciusSantana_RM564940_fase3_cap1
#VitorGuisso_RM562317_fase3_cap1


import cx_Oracle

# Configurações de conexão
username = "RM562317"
password = "100598"
dsn = "oracle.fiap.com.br/orcl"

# Dados simulados da plataforma Wokwi
dados_iniciais = [
    (50.5, 6.4, "Ausente", "Ausente"),
    (50.5, 6.4, "Presente", "Ausente"),
    (50.5, 6.4, "Ausente", "Presente"),
    (50.5, 2.6, "Ausente", "Ausente"),
    (42.0, 11.9, "Ausente", "Ausente"),
    (27.0, 11.9, "Ausente", "Ausente"),
    (41.0, 7.2, "Presente", "Ausente")
]

# Função para calcular o estado da bomba com base na umidade
def calcular_bomba(umidade):
    return "LIGADA" if umidade < 40 else "DESLIGADA"

# Conecta ao banco e prepara cursor
try:
    connection = cx_Oracle.connect(username, password, dsn)
    cursor = connection.cursor()
except cx_Oracle.DatabaseError as e:
    print("Erro ao conectar ao banco:", e)
    exit()

# Verifica se a tabela está vazia e insere os dados iniciais
cursor.execute("SELECT COUNT(*) FROM sistema_irrigacao")
count = cursor.fetchone()[0]
if count == 0:
    for dado in dados_iniciais:
        bomba = calcular_bomba(dado[0])
        cursor.execute("""
            INSERT INTO sistema_irrigacao (umidade, ph, fosforo, potassio, bomba)
            VALUES (:1, :2, :3, :4, :5)
        """, (*dado, bomba))
    connection.commit()
    print("[✓] Dados iniciais inseridos no banco.")

# =============================
# Função: Exibir todos os dados
# =============================
def ler_tudo():
    cursor.execute("SELECT * FROM sistema_irrigacao ORDER BY id")
    registros = cursor.fetchall()

    print("\n=== BANCO DE DADOS ATUAL ===")
    for r in registros:
        print(f"id: {r[0]} | Umidade: {r[1]:.2f}% | pH: {r[2]:.2f} | Fósforo: {r[3]} | Potássio: {r[4]} | Bomba: {r[5]}")
    print("-----------------------------")

# =============================
# Função: Inserir novo registro
# =============================
def criar_registro():
    while True:
        try:
            umidade = float(input("Digite a umidade (0 a 100): "))
            if 0 <= umidade <= 100:
                break
            print("Erro: valor fora do intervalo.")
        except ValueError:
            print("Erro: digite um número.")

    while True:
        try:
            ph = float(input("Digite o pH (0 a 14): "))
            if 0 <= ph <= 14:
                break
            print("Erro: valor fora do intervalo.")
        except ValueError:
            print("Erro: digite um número.")

    while True:
        fosforo = input("Fósforo (Presente/Ausente): ").capitalize()
        if fosforo in ["Presente", "Ausente"]:
            break
        print("Erro: apenas Presente ou Ausente.")

    while True:
        potassio = input("Potássio (Presente/Ausente): ").capitalize()
        if potassio in ["Presente", "Ausente"]:
            break
        print("Erro: apenas Presente ou Ausente.")

    bomba = calcular_bomba(umidade)

    cursor.execute("""
        INSERT INTO sistema_irrigacao (umidade, ph, fosforo, potassio, bomba)
        VALUES (:1, :2, :3, :4, :5)
    """, (umidade, ph, fosforo, potassio, bomba))
    connection.commit()
    print("[✓] Registro inserido.")

# =============================
# Função: Atualizar registro
# =============================
def atualizar():
    ler_tudo()
    try:
        id_registro = int(input("ID do registro a atualizar: "))
    except ValueError:
        print("Erro: ID inválido.")
        return

    campo = input("Campo (umidade, ph, fosforo, potassio): ").lower()
    if campo not in ["umidade", "ph", "fosforo", "potassio"]:
        print("Campo inválido.")
        return

    if campo == "umidade":
        while True:
            try:
                valor = float(input("Novo valor (0 a 100): "))
                if 0 <= valor <= 100:
                    break
                print("Erro: fora do intervalo.")
            except ValueError:
                print("Erro: número inválido.")
        cursor.execute(f"UPDATE sistema_irrigacao SET umidade = :1 WHERE id = :2", (valor, id_registro))
        bomba = calcular_bomba(valor)
        cursor.execute("UPDATE sistema_irrigacao SET bomba = :1 WHERE id = :2", (bomba, id_registro))
    elif campo == "ph":
        while True:
            try:
                valor = float(input("Novo pH (0 a 14): "))
                if 0 <= valor <= 14:
                    break
                print("Erro: fora do intervalo.")
            except ValueError:
                print("Erro: número inválido.")
        cursor.execute("UPDATE sistema_irrigacao SET ph = :1 WHERE id = :2", (valor, id_registro))
    else:
        while True:
            valor = input(f"Novo valor para {campo} (Presente/Ausente): ").capitalize()
            if valor in ["Presente", "Ausente"]:
                break
            print("Erro: valor inválido.")
        cursor.execute(f"UPDATE sistema_irrigacao SET {campo} = :1 WHERE id = :2", (valor, id_registro))

    connection.commit()
    print("[✓] Registro atualizado.")

# =============================
# Função: Deletar registro
# =============================
def deletar():
    ler_tudo()
    try:
        id_registro = int(input("ID do registro a excluir: "))
        cursor.execute("DELETE FROM sistema_irrigacao WHERE id = :1", (id_registro,))
        connection.commit()
        print("[✓] Registro deletado.")
    except ValueError:
        print("ID inválido.")

# =============================
# MENU
# =============================
def menu():
    while True:
        print("\n===== MENU SISTEMA DE IRRIGAÇÃO =====")
        print("1 - Ver registros")
        print("2 - Inserir novo registro")
        print("3 - Atualizar registro")
        print("4 - Deletar registro")
        print("0 - Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ler_tudo()
        elif opcao == "2":
            criar_registro()
        elif opcao == "3":
            atualizar()
        elif opcao == "4":
            deletar()
        elif opcao == "0":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

    cursor.close()
    connection.close()

menu()

