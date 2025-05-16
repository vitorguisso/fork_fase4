


'''DADOS BASE


SOJA

'É possível encontrar variações entre 200 e 500 mil plantas por hectare, sendo que a recomendação média da população de plantas para a cultura da soja é de 300 mil plantas por hectare.'
'Quando o assunto é espaçamento entre fileiras, o valor mais utilizado fica entre 40 e 50 cm.'

https://chbagro.com.br/blog/calculo-de-semeadura-da-soja-pms-soja-passo-a-passo


'De modo geral, a população indicada para a cultura de soja situa-se em torno de 300.000 plantas por hectare ou 30 plantas por metro quadrado, com variações conforme a cultivar.'

 Soja: A população ideal varia entre 140.000 a 170.000 plantas por hectare, dependendo da cultivar e das condições locais
https://agroinsight.com.br/impacto-da-ma-distribuicao-de-sementes-na-produtividade-da-soja-e-do-milho/#google_vignette



MILHO
'A população ideal para maximizar o rendimento de grãos de milho varia de 30.000 a 90.000 plantas por hectare, dependendo da disponibilidade hídrica, da fertilidade do solo, do ciclo da cultivar, da época de semeadura e do espaçamento entre linhas.'
 'Dados de pesquisa mostram vantagens do espaçamento reduzido (45 cm a 50 cm entre fileiras)'

Milho: A densidade recomendada pode variar de 30.000 a 90.000 plantas por hectare, conforme a região, altitude e época de plantio.
https://www.embrapa.br/agencia-de-informacao-tecnologica/cultivos/milho/producao/plantio/espacamento-e-densidade


'''

import os
############################################################################ MENU PRINCIPAL ############################################################################

'''Essas funções são responsáveis pelo primeiro menu (Principal). Nele o usuário seleciona se deseja trabalhar com milho ou soja. Além disso, esse menu é responsável por finalizar o programa.'''

def main():
    os.system('cls')
    exibir_opcoes()
    escolher_opcao()

def exibir_opcoes():
    print('Bem Vindo ao MISO, Seu programa para cultivo de milho ou soja Digital!\n')
    print('-----------Menu-------------\n')
    print('1. Informações sobre cultivo de milho')
    print('2. Informações sobre cultivo de soja')
    print('3. Sair\n')

def escolher_opcao():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))

        if opcao_escolhida == 1:
            menu_milho()
        elif opcao_escolhida == 2:
            menu_soja()
        elif opcao_escolhida == 3:
            finalizar_app()
        else:
            opcao_invalida()
    except ValueError:
        opcao_invalida()

def opcao_invalida():
    print('\nOpção inválida! Escolha uma opção válida.')
    input("Pressione uma tecla para voltar ao menu principal...")
    main()

def finalizar_app():
    print('Finalizando o programa. Obrigado por utilizar o MISO!')

############################################################################ MENU MILHO ############################################################################
'''Essas funções são responsáveis pelo menu destinado às opções sobre o milho. Nele, o usuário poderá calcular a área de plantio, o número de fileiras,a quantidade de sementes e os insumos utilizados.
 Também poderá visualizar dados estatísticos, listar os insumos em uma lista e editá-los. Além disso, é possível retornar ao menu principal.'''

insumos_milho = [] # Vetor para armazenas os insumos inseridos pelo usuário.

def menu_milho():
    os.system('cls')
    print("Maravilha, agora podemos seguir com as informações do cultivo de milho! \n")
    print('1. Calcular quantidade de sementes por metro | Área | N° Fileiras ')
    print('2. Calcular Manejo de Insumos')
    print('3. Exibir dados estatísticos como média e desvio padrão')
    print('4. Cadastro de Lista de Insumos')
    print('5. Voltar ao menu principal\n')
    escolher_opcao_milho()

def escolher_opcao_milho():
    try:
        opcao_escolhida_milho = int(input('Escolha uma opção: '))

        if opcao_escolhida_milho == 1:
            calcular_area_e_sementes_milho()
        elif opcao_escolhida_milho == 2:
            calculo_insumos_milho()
        elif opcao_escolhida_milho == 3:
            exibir_estatisticas_milho()
        elif opcao_escolhida_milho == 4:
            lista_insumos_milho()
        elif opcao_escolhida_milho == 5:
            main()
        else:
            opcao_invalida_milho()
    except ValueError:
        opcao_invalida_milho()

def opcao_invalida_milho():
    print('\nOpção inválida! Escolha uma opção válida.')
    input("Pressione uma tecla para voltar ao menu do milho...")
    menu_milho()

def calcular_area_e_sementes_milho():
    print("\n### CÁLCULO COMPLETO DA ÁREA, FILEIRAS E SEMENTES DE MILHO ###\n")

    # Entrada de dados para a área de plantio
    while True:
        try:
            largura_milho = float(input("Digite a LARGURA da área de plantio (em metros) - Base para as fileiras: ").replace(',', '.'))
            comprimento_milho = float(input("Digite o COMPRIMENTO da área de plantio (em metros): ").replace(',', '.'))
            espacamento_fileiras_milho = float(input("Digite o ESPAÇAMENTO entre fileiras (em metros, ex: 0.5): ").replace(',', '.'))
            populacao_desejada_milho = int(input("Digite a POPULAÇÃO desejada de plantas por hectare: "))

            if largura_milho > 0 and comprimento_milho > 0 and espacamento_fileiras_milho > 0 and populacao_desejada_milho > 0:
                break
            else:
                print("ERRO: Todos os valores devem ser números positivos!")
        except ValueError:
            print("ERRO: Digite valores numéricos válidos!")

    # Cálculo da área total e conversão para hectares
    area_m2_milho = largura_milho * comprimento_milho
    area_hectares_milho = area_m2_milho / 10000  # 1 hectare = 10.000 m²

    # Cálculo do número de fileiras
    num_fileiras_milho = int(largura_milho / espacamento_fileiras_milho) + 1  # +1 devido ao metro zero também ter uma fileira de sementes

    # Cálculo do número de plantas por metro linear
    plantas_por_metro_milho = (populacao_desejada_milho * espacamento_fileiras_milho) / 10000

    # Cálculo do espaçamento entre sementes dentro da fileira
    espacamento_sementes_milho = 1 / plantas_por_metro_milho

    # Cálculo do número de sementes por fileira
    sementes_por_fileira_milho = int(comprimento_milho / espacamento_sementes_milho)

    # Cálculo total de sementes necessárias para a área total
    total_sementes_milho = num_fileiras_milho * sementes_por_fileira_milho

    # Cálculo de quantidade de sementes kg pela área
    sementes_kg = (populacao_desejada_milho / 3500) #3500 sementes é a média de peso para um kg de sementes
    germinacao_milho = (sementes_kg * 1.1)

    # Exibir os resultados
    print("\n### RESULTADOS DO CÁLCULO - MILHO ###")
    print(f"Área total de plantio: {area_m2_milho:.2f} m² ({area_hectares_milho:.2f} hectares)")
    print(f"Número de fileiras de plantio: {num_fileiras_milho}")
    print(f"Plantas por metro linear: {plantas_por_metro_milho:.2f}")
    print(f"Espaçamento entre sementes: {espacamento_sementes_milho:.2f} metros")
    print(f"Sementes por fileira: {sementes_por_fileira_milho}")
    print(f"Total de sementes necessárias: {total_sementes_milho}")
    print(f"Total de sementes necessárias: {germinacao_milho:.2f}kg")

    input("\nPressione uma tecla para voltar ao menu...")
    menu_milho()


 # DESENVOLVIMENTO CÁLCULO INSUMOS MILHO ##############################################
    '''Os calculos dos insumos do milho foram baseados informações fornecidas pelo Emater, Empresa de Assistência Técnica e Extensão Rural

    Foram baseadas nas seguintes informações:

    Insumos para o plantio no tratamento de semente para doenças de solo:
    - Carboxina + Thiram 200 g/L: 100 a 150mL/60kg de semente;

    Inseticidas:
    - Metomil (metilcarbamato de oxima) 215 g/L: 400 a 600 mL/hectare;
    
    Para efeito de cálculo, foram considerados os valores máximos de consumo.

fonte: https://www.emater.go.gov.br/wp/wp-content/uploads/2022/11/orientacoes-para-cultura-de-milho.pdf '''

def calculo_insumos_milho():
    os.system('cls')
    print("### CÁLCULO DE INSUMOS PARA PLANTIO DE MILHO ###\n")

    # Entrada de dados
    try:
        kg_semente = float(input("Digite a quantidade de sementes utilizadas (kg): "))
        area_hectares = float(input("Digite a área total em hectares: "))
        ruas_milho = int(input("Digite a quantidade ocupada de ruas: "))

        if kg_semente <= 0 or area_hectares <= 0:
            print("ERRO: Os valores devem ser positivos!")
            input("Pressione uma tecla para tentar novamente...")
            calculo_insumos_milho()
            return

    except ValueError:
        print("ERRO: Digite um número válido!")
        input("Pressione uma tecla para tentar novamente...")
        calculo_insumos_milho()
        return

    # Cálculo dos insumos (apenas dose máxima)

    ## Tratamento de Sementes (Carboxina + Thiram)
    dose_carboxina_ml = (kg_semente / 60) * 150
    dose_carboxina_kg = (dose_carboxina_ml / 1000) * 0.2  # 200g/L = 0.2 kg/L

    ## Inseticida (Metomil)
    dose_metomil_ml = area_hectares * 600
    dose_metomil_kg = (dose_metomil_ml / 1000) * 0.215  # 215g/L = 0.215 kg/L

    ## Cálculo de ruas para cobertura em L
    area_util_milho = (ruas_milho - area_hectares)
    eficiencia_aplicacao_milho = 0.9
    dose_recomendada_milho = 2 #L/h
    qtd_ins_milho = (area_util_milho * dose_recomendada_milho / eficiencia_aplicacao_milho)

    # Exibir resultados corrigidos
    os.system('cls')
    print("### RESULTADO DO CÁLCULO DE INSUMOS ###\n")
    print(f"Para {kg_semente:.2f} kg de sementes e {area_hectares:.2f} hectares de plantio, você precisará de:\n")

    print("Tratamento de Sementes (Carboxina + Thiram):")
    print(f" - {dose_carboxina_ml:.2f} mL de solução e {dose_carboxina_kg:.4f} kg do produto\n")

    print("Inseticida (Metomil):")
    print(f" - {dose_metomil_ml:.2f} mL de solução e {dose_metomil_kg:.2f} kg do produto\n")

    print("Inseticida (Metomil):")
    print(f'Aplicar {qtd_ins_milho:.2f}L de metomil para área de {area_hectares:.2f} hectares de plantio com {ruas_milho} ruas')

    input("Pressione uma tecla para voltar ao menu do milho...")
    menu_milho()

# ESTATISTICAS MILHO#####################################
'''
CÁLCULO DE MÉDIA E DESVIO PADRÃO DOS INSUMOS

Neste projeto, estamos calculando a média e o desvio padrão para dois insumos utilizados no plantio de milho:

1. **Carboxina + Thiram (Tratamento de Sementes)**
   - Média: Representa o consumo médio de Carboxina + Thiram por hectare.
   - Desvio Padrão: Mede a variação na aplicação do insumo entre diferentes áreas de cultivo.

2. **Metomil (Inseticida)**
   - Média: Representa o consumo médio de Metomil por hectare.
   - Desvio Padrão: Mede a variação na aplicação do Metomil entre diferentes áreas de cultivo.

Os cálculos são realizados no R, onde usamos os seguintes conjuntos de dados fictícios para exemplificar:

- **Dados de Carboxina + Thiram (kg/hectare)**
  carboxina_hectare <- c(1.1, 1.3, 1.2, 1.4, 1.0, 1.2, 1.3, 1.1)

- **Dados de Metomil (kg/hectare)**
  metomil_hectare <- c(0.4, 0.6, 0.5, 0.55, 0.45, 0.5, 0.52, 0.48)

Fórmulas utilizadas no R:

- **Média do Consumo de Insumo por Hectare**:
  Média = sum(X) / n  

- **Desvio Padrão do Consumo de Insumo por Hectare**:
  Desvio Padrão = sqrt(sum((X_i - Média)^2) / (n-1))

Onde:
- X = valores de consumo por hectare
- n = número total de medições

Após rodarmos esses cálculos no R, substituímos os valores obtidos no Python para exibição no programa.

'''

def exibir_estatisticas_milho():
    os.system('cls')

    # Valores calculados no R (Substituir com os valores obtidos no R)
    media_carboxina = 1.2  # kg/hectare
    desvio_padrao_carboxina = 0.15  # kg/hectare

    media_metomil = 0.5  # kg/hectare
    desvio_padrao_metomil = 0.05  # kg/hectare

    # Exibir os resultados
    print("### ESTATÍSTICAS DOS INSUMOS ###\n")

    print("Tratamento de Sementes (Carboxina + Thiram):")
    print(f" - Média: {media_carboxina:.2f} kg de produto/hectare")
    print(f" - Desvio Padrão: {desvio_padrao_carboxina:.2f} kg/hectare\n")

    print("Inseticida (Metomil):")
    print(f" - Média: {media_metomil:.2f} kg/hectare")
    print(f" - Desvio Padrão: {desvio_padrao_metomil:.2f} kg de produto/hectare\n")

    input("Pressione uma tecla para voltar ao menu...")
    menu_milho()

################### LISTA DE INSUMOS MILHO ###################

#Para a lista de insumos, criamos um submenu. Nele, o usuário pode adicionar, editar, excluir e visualizar os insumos cadastrados.

def lista_insumos_milho():
    os.system('cls')
    print('------- Insumos Milho -------')
    print('1. Cadastrar insumo')
    print('2. Editar insumo')
    print('3. Excluir insumo')
    print('4. Exibir insumos cadastrados')
    print('5. Voltar para o menu do milho')

    try:
        opcao_insumo_milho = int(input('\nEscolha uma opção: '))

        if opcao_insumo_milho == 1:
            cadastrar_insumo()
        elif opcao_insumo_milho == 2:
            editar_insumo()
        elif opcao_insumo_milho == 3:
            excluir_insumo()
        elif opcao_insumo_milho == 4:
            exibir_insumos()
        elif opcao_insumo_milho == 5:
            menu_milho()
        else:
            opcao_invalida_insumos_milho()

    except ValueError:
        opcao_invalida_insumos_milho()


def cadastrar_insumo():
    nome_insumo = input('Digite o nome do insumo que deseja cadastrar: ').strip()
    if nome_insumo:
        insumos_milho.append(nome_insumo)
        print(f'O insumo "{nome_insumo}" foi cadastrado com sucesso!')
    else:
        print("Erro: O nome do insumo não pode estar vazio.")

    input("Pressione uma tecla para voltar ao menu de insumos...\n")
    lista_insumos_milho()


def editar_insumo():
    if not insumos_milho:
        print("\nNenhum insumo cadastrado para editar.")
        input("Pressione uma tecla para voltar ao menu.")
        lista_insumos_milho()
        return

    print("\nLista de insumos cadastrados:")
    for i, insumo in enumerate(insumos_milho, start=1):
        print(f"{i}. {insumo}")

    try:
        indice = int(input("\nDigite o número do insumo que deseja editar (ou 0 para cancelar): ")) - 1
        if indice == -1:
            lista_insumos_milho()
            return

        if 0 <= indice < len(insumos_milho):
            novo_nome = input("Digite o novo nome do insumo: ").strip()
            if novo_nome:
                insumos_milho[indice] = novo_nome
                print(f'Insumo atualizado para "{novo_nome}" com sucesso!')
            else:
                print("Erro: O nome do insumo não pode estar vazio.")
        else:
            print("Erro: Número inválido! Escolha um número da lista.")
    except ValueError:
        print("Erro: Digite um número válido.")

    input("Pressione uma tecla para voltar ao menu de insumos...\n")
    lista_insumos_milho()


def excluir_insumo():
    if not insumos_milho:
        print("\nNenhum insumo cadastrado para excluir.")
        input("Pressione uma tecla para voltar ao menu.")
        lista_insumos_milho()
        return

    print("\nLista de insumos cadastrados:")
    for i, insumo in enumerate(insumos_milho, start=1):
        print(f"{i}. {insumo}")

    try:
        indice = int(input("\nDigite o número do insumo que deseja excluir (ou 0 para cancelar): ")) - 1
        if indice == -1:
            lista_insumos_milho()
            return

        if 0 <= indice < len(insumos_milho):
            insumo_removido = insumos_milho.pop(indice)
            print(f'O insumo "{insumo_removido}" foi removido com sucesso!')
        else:
            print("Erro: Número inválido! Escolha um número da lista.")
    except ValueError:
        print("Erro: Digite um número válido.")

    input("Pressione uma tecla para voltar ao menu de insumos...\n")
    lista_insumos_milho()


def exibir_insumos():
    if insumos_milho:
        print("\nLista de insumos cadastrados:")
        for insumo in insumos_milho:
            print(f' - {insumo}')
    else:
        print("\nNenhum insumo cadastrado ainda.")

    input('\nPressione uma tecla para voltar ao menu de insumos...\n')
    lista_insumos_milho()


def opcao_invalida_insumos_milho():
    print('\nOpção inválida! Escolha uma opção válida.')
    input("Pressione uma tecla para voltar ao menu de insumos...")
    lista_insumos_milho()


############################################################################ MENU SOJA ############################################################################
'''Essas funções são responsáveis pelo menu destinado às opções sobre o soja. Nele, o usuário poderá calcular a área de plantio, o número de fileiras,a quantidade de sementes e os insumos utilizados.
 Também poderá visualizar dados estatísticos, listar os insumos em uma lista e editá-los. Além disso, é possível retornar ao menu principal.'''

insumos_soja = []

def menu_soja():
    os.system('cls')
    print("Maravilha, agora podemos seguir com as informações do cultivo de soja! \n")
    print('1. Calcular quantidade de sementes por metro | Área | N° Fileiras')
    print('2. Calcular Manejo de Insumos')
    print('3. Exibir dados estatísticos como média e desvio padrão')
    print('4. Cadastro de Lista de Insumos')
    print('5. Voltar ao menu principal\n')
    escolher_opcao_soja()

def escolher_opcao_soja():
    try:
        opcao_escolhida_soja = int(input('Escolha uma opção: '))

        if opcao_escolhida_soja == 1:
            calcular_area_e_sementes_soja()
        elif opcao_escolhida_soja == 2:
            calculo_insumos_soja()
        elif opcao_escolhida_soja == 3:
            dados_estatisticos_soja()
        elif opcao_escolhida_soja == 4:
            lista_insumos_soja()
        elif opcao_escolhida_soja == 5:
            main()
        else:
            opcao_invalida_soja()
    except ValueError:
        opcao_invalida_soja()

def opcao_invalida_soja():
    print('\nOpção inválida! Escolha uma opção válida.')
    input("Pressione uma tecla para voltar ao menu da soja...")
    menu_soja()

def calcular_area_e_sementes_soja():
    print("\n### CÁLCULO COMPLETO DA ÁREA, FILEIRAS E SEMENTES DE SOJA ###\n")

    # Entrada de dados para a área de plantio
    while True:
        try:
            largura_soja = float(
                input("Digite a LARGURA da área de plantio (em metros) - Base para as fileiras: ").replace(',',
                                                                                                           '.'))
            comprimento_soja = float(
                input("Digite o COMPRIMENTO da área de plantio (em metros): ").replace(',', '.'))
            espacamento_fileiras_soja = float(
                input("Digite o ESPAÇAMENTO entre fileiras (em metros, ex: 0.4): ").replace(',', '.'))
            populacao_desejada_soja = int(input("Digite a POPULAÇÃO desejada de plantas por hectare: "))

            if largura_soja > 0 and comprimento_soja > 0 and espacamento_fileiras_soja > 0 and populacao_desejada_soja > 0:
                break
            else:
                print("ERRO: Todos os valores devem ser números positivos!")
        except ValueError:
            print("ERRO: Digite valores numéricos válidos!")

    # Cálculo da área total e conversão para hectares
    area_m2_soja = largura_soja * comprimento_soja
    area_hectares_soja = area_m2_soja / 10000  # 1 hectare = 10.000 m²

    # Cálculo do número de fileiras
    num_fileiras_soja = int(largura_soja / espacamento_fileiras_soja) + 1  # +1 devido ao metro zero também ter uma fileira de sementes

    # Cálculo do número de plantas por metro linear
    plantas_por_metro_soja = (populacao_desejada_soja * espacamento_fileiras_soja) / 10000

    # Cálculo do espaçamento entre sementes dentro da fileira
    espacamento_sementes_soja = 1 / plantas_por_metro_soja

    # Cálculo do número de sementes por fileira
    sementes_por_fileira_soja = int(comprimento_soja / espacamento_sementes_soja)

    # Cálculo total de sementes necessárias para a área total
    total_sementes_soja = num_fileiras_soja * sementes_por_fileira_soja

    # Cálculo de quantidade de sementes kg pela área
    sementes_kg_soja = (populacao_desejada_soja / 3500) #3500 sementes é a média de peso para um kg de sementes
    germinacao_soja = (sementes_kg_soja * 1.1)

    # Exibir os resultados
    print("\n### RESULTADOS DO CÁLCULO - SOJA ###\n")
    print(f"- Área total de plantio: {area_m2_soja:.2f} m² ({area_hectares_soja:.2f} hectares)")
    print(f"- Número de fileiras de plantio: {num_fileiras_soja}")
    print(f"- Plantas por metro linear: {plantas_por_metro_soja:.2f}")
    print(f"- Espaçamento entre sementes: {espacamento_sementes_soja:.2f} metros")
    print(f"- Sementes por fileira: {sementes_por_fileira_soja}")
    print(f"- Total de sementes necessárias: {total_sementes_soja}")
    print(f"- Total de sementes necessárias: {germinacao_soja:.2f}kg")

    input("\nPressione uma tecla para voltar ao menu...")
    menu_soja()

    '''print('Vamos calcular a quantidade de sementes a serem plantadas por metro\n')

    while True:
        try:
            populacao_desejada = int(input("Digite a população desejada de plantas por hectare: "))
            if populacao_desejada > 0:
                break
            else:
                print("ERRO: A população desejada deve ser um número positivo!")
        except ValueError:
            print("ERRO: Digite um número inteiro válido!")

    while True:
        try:
            espacamento = float(input("Digite o espaçamento entre linhas ex 0.50: ").replace(',', '.'))
            if espacamento > 0:
                break
            else:
                print("ERRO: O espaçamento deve ser um número positivo!")
        except ValueError:
            print("ERRO: Digite um número decimal válido! Exemplo: 0.50")

    while True:
        try:
            area = int(input("Digite a área total em m²: "))
            if area > 0:
                break
            else:
                print("ERRO: A área deve ser um número positivo!")
        except ValueError:
            print("ERRO: Digite um número inteiro válido!")

    hectares = 10000
    area_espacamento = int(area / espacamento)
    print(f'\nA área de espaçamento é {area_espacamento}')

    resultado = (populacao_desejada / hectares / area_espacamento) * 10000
    print(f'Este cálculo indica que, para atingir uma população de {populacao_desejada} por hectare com espaçamento de {espacamento} m entre linhas, deve-se semear {resultado:.2f} sementes por metro.')

    input('\nAperte uma tecla para voltar ao menu da soja')
    menu_soja()'''

# CÁLCULO INSUMOS SOJA#####################################
'''Para fins de cálculo, vamos utilizar nesse projeto o inceticida Unânimebr - 
 
 COMPOSIÇÃO:
 1-(4-chlorophenyl)-3-(2,6-difluorobenzoyl)urea (DIFLUBENZURON) .................................. 480 g/L (48 % m/v)
 Outros Ingredientes:............................................................................. 710 g/L (71 % m/v)
 
 Para o soja, ele é aplicado para combater pragas Lagarta-da-soja (Anticarsia gemmatalis) e possui recomendação de 40 mL/ha (19,2 g i.a/ha)
 
 FONTE:#https://www.adapar.pr.gov.br/sites/adapar/arquivos_restritos/files/documento/2021-03/unanimebr.pdf
 
 '''
def calculo_insumos_soja():
    print("\n### CÁLCULO DE INSUMOS PARA SOJA - INSETICIDA UNÂNIMEBR ###\n")

    # Entrada de dados: área de plantio em hectares
    while True:
        try:
            soja_area_insumos= float(input("Digite a ÁREA TOTAL de plantio em hectares: ").replace(',', '.'))
            ruas_soja = int(input("Digite a quantidade ocupada de ruas: "))
            if soja_area_insumos > 0:
                break
            else:
                print("ERRO: A área deve ser um número positivo!")
        except ValueError:
            print("ERRO: Digite um valor numérico válido!")

    # Cálculo da quantidade necessária de inseticida
    soja_quantidade_unanimebr_ml = soja_area_insumos * 40  # 40 mL por hectare
    soja_quantidade_i_a_g = soja_area_insumos * 19.2  # 19,2 g i.a. por hectare

    #Cálculo da quantidade necessárias levando em consideração as ruas
    area_util_soja = (ruas_soja - soja_area_insumos)
    eficiencia_soja = 0.9
    dose_recomendada_soja = 0.40 #L/h
    qtd_ins_soja = (area_util_soja * dose_recomendada_soja / eficiencia_soja)

    # Exibir os resultados
    print("\n### RESULTADOS DO CÁLCULO ###")
    print(f"Área total de plantio: {soja_area_insumos:.2f} hectares")
    print(f"Quantidade de inseticida UnânimeBR necessária: {soja_quantidade_unanimebr_ml:.2f} mL de solução")
    print(f"Quantidade de ingrediente ativo aplicada: {soja_quantidade_i_a_g:.2f} g ({soja_quantidade_i_a_g/1000:.2f} Kg) de ingrediente ativo ")
    print(f'Aplicar {qtd_ins_soja:.2f}L de metomil para área de {soja_area_insumos:.2f} hectares de plantio com {ruas_soja} ruas')

    input("\nPressione uma tecla para voltar ao menu...")
    menu_soja()

# ESTATISTICAS MILHO#####################################
# Resultados calculados no R
def dados_estatisticos_soja():
    media_sementes = 507500  # Média de sementes por hectare
    desvio_padrao_sementes = 15708  # Desvio padrão das sementes por hectare

    media_espacamento = 0.21  # Média do espaçamento entre sementes em metros
    desvio_padrao_espacamento = 0.013  # Desvio padrão do espaçamento entre sementes


    # Exibindo os resultados no terminal
    print("\n### DADOS ESTATÍSTICOS - SOJA ###\n")
    print(f"- Média de sementes por hectare: {media_sementes:.2f} sementes/hectare")
    print(f"- Desvio padrão das sementes por hectare: {desvio_padrao_sementes:.2f} sementes/hectare\n")
    print(f"- Média do espaçamento entre sementes: {media_espacamento:.2f} metros")
    print(f"- Desvio padrão do espaçamento entre sementes: {desvio_padrao_espacamento:.3f} metros")

    input('\nDigite uma tecla para voltar ao menu da soja')
    menu_soja()

################### LISTA DE INSUMOS SOJA ###################
#Para a lista de insumos, criamos um submenu. Nele, o usuário pode adicionar, editar, excluir e visualizar os insumos cadastrados.

def lista_insumos_soja():
    os.system('cls')
    print('------- Insumos Soja -------')
    print('1. Cadastrar insumo')
    print('2. Editar insumo')
    print('3. Excluir insumo')
    print('4. Exibir insumos cadastrados')
    print('5. Voltar para o menu da soja')

    try:
        opcao_insumo_soja = int(input('\nEscolha uma opção: '))

        if opcao_insumo_soja == 1:
            cadastrar_insumo_soja()
        elif opcao_insumo_soja == 2:
            editar_insumo_soja()
        elif opcao_insumo_soja == 3:
            excluir_insumo_soja()
        elif opcao_insumo_soja == 4:
            exibir_insumos_soja()
        elif opcao_insumo_soja == 5:
            menu_soja()
        else:
            opcao_invalida_insumos_soja()

    except ValueError:
        opcao_invalida_insumos_soja()

def cadastrar_insumo_soja():
    nome_insumo = input('Digite o nome do insumo que deseja cadastrar: ').strip()
    if nome_insumo:
        insumos_soja.append(nome_insumo)
        print(f'O insumo "{nome_insumo}" foi cadastrado com sucesso!')
    else:
        print("Erro: O nome do insumo não pode estar vazio.")

    input("Pressione uma tecla para voltar ao menu de insumos da soja...\n")
    lista_insumos_soja()

def editar_insumo_soja():
    if not insumos_soja:
        print("\nNenhum insumo cadastrado para editar.")
        input("Pressione uma tecla para voltar ao menu.")
        lista_insumos_soja()
        return

    print("\nLista de insumos cadastrados:")
    for i, insumo in enumerate(insumos_soja, start=1):
        print(f"{i}. {insumo}")

    try:
        indice = int(input("\nDigite o número do insumo que deseja editar (ou 0 para cancelar): ")) - 1
        if indice == -1:
            lista_insumos_soja()
            return

        if 0 <= indice < len(insumos_soja):
            novo_nome = input("Digite o novo nome do insumo: ").strip()
            if novo_nome:
                insumos_soja[indice] = novo_nome
                print(f'Insumo atualizado para "{novo_nome}" com sucesso!')
            else:
                print("Erro: O nome do insumo não pode estar vazio.")
        else:
            print("Erro: Número inválido! Escolha um número da lista.")
    except ValueError:
        print("Erro: Digite um número válido.")

    input("Pressione uma tecla para voltar ao menu de insumos da soja...\n")
    lista_insumos_soja()

def excluir_insumo_soja():
    if not insumos_soja:
        print("\nNenhum insumo cadastrado para excluir.")
        input("Pressione uma tecla para voltar ao menu.")
        lista_insumos_soja()
        return

    print("\nLista de insumos cadastrados:")
    for i, insumo in enumerate(insumos_soja, start=1):
        print(f"{i}. {insumo}")

    try:
        indice = int(input("\nDigite o número do insumo que deseja excluir (ou 0 para cancelar): ")) - 1
        if indice == -1:
            lista_insumos_soja()
            return

        if 0 <= indice < len(insumos_soja):
            insumo_removido = insumos_soja.pop(indice)
            print(f'O insumo "{insumo_removido}" foi removido com sucesso!')
        else:
            print("Erro: Número inválido! Escolha um número da lista.")
    except ValueError:
        print("Erro: Digite um número válido.")

    input("Pressione uma tecla para voltar ao menu de insumos da soja...\n")
    lista_insumos_soja()

def exibir_insumos_soja():
    if insumos_soja:
        print("\nLista de insumos cadastrados:")
        for insumo in insumos_soja:
            print(f' - {insumo}')
    else:
        print("\nNenhum insumo cadastrado ainda.")

    input('\nPressione uma tecla para voltar ao menu de insumos da soja...\n')
    lista_insumos_soja()

def opcao_invalida_insumos_soja():
    print('\nOpção inválida! Escolha uma opção válida.')
    input("Pressione uma tecla para voltar ao menu de insumos da soja...")
    lista_insumos_soja()




if __name__ == '__main__':
    main()

