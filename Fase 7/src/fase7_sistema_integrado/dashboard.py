import os

from fase1_calculo_plantio.FASE1_misoi import main as fase1_main
from fase2_banco_relacional.FASE2_controle_estoque_com_banco import menu as fase2_menu
from fase4_sistema_irrigacao_dashboard.FASE4_sistema_irrigacao import menu as fase4_menu
from fase6_visao_computacional.FASE6_resumo import menu_fase6
from fase5_analise_aws.aws_alertas import enviar_alerta_aws


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def menu_principal():
    while True:
        limpar_tela()
        print("====================================")
        print("      SISTEMA INTEGRADO - FASE 7    ")
        print("               FIAP                  ")
        print("====================================\n")

        print("1 - Abrir sistema de cálculo de plantio (Fase 1)")
        print("2 - Abrir sistema de controle de estoque (Fase 2)")
        print("3 - Abrir sistema de irrigação e sensores (Fases 3 e 4)")
        print("4 - Enviar alerta AWS com base nos sensores (Fase 5)")
        print("5 - Abrir menu da visão computacional (Fase 6)")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        # ================= FASE 1 ==================
        if opcao == "1":
            limpar_tela()
            print("Abrindo sistema de cálculo de plantio (Fase 1)...\n")
            fase1_main()
            input("\nRetornando ao sistema integrado...\nPressione ENTER para voltar ao menu...")

        # ================= FASE 2 ==================
        elif opcao == "2":
            limpar_tela()
            print("Abrindo sistema de controle de estoque (Fase 2)...\n")
            fase2_menu()
            input("\nRetornando ao sistema integrado...\nPressione ENTER para voltar ao menu...")

        # ================= FASE 3 + FASE 4 ==================
        elif opcao == "3":
            limpar_tela()
            print("Abrindo sistema de irrigação e sensores (Fases 3 e 4)...\n")
            fase4_menu()
            input("\nRetornando ao sistema integrado...\nPressione ENTER para voltar ao menu...")

        # ================= FASE 5 (AWS ALERTAS) ==================
        elif opcao == "4":
            limpar_tela()
            print("=== ENVIO DE ALERTA AWS (FASE 5) ===\n")
            print("Informe os dados de sensores (Fase 4).")
            print("Use os valores exibidos no banco da irrigação.\n")

            try:
                umidade = float(input("Umidade atual do solo (%): ").replace(",", "."))
                ph = float(input("pH atual do solo: ").replace(",", "."))
                fosforo = input("Fósforo (Presente/Ausente): ").strip()
                potassio = input("Potássio (Presente/Ausente): ").strip()

                enviar_alerta_aws(umidade, ph, fosforo, potassio)

            except ValueError:
                print("\nValores numéricos inválidos. Tente novamente.")

            input("\nPressione ENTER para voltar ao menu...")

        # ================= FASE 6 (VISÃO COMPUTACIONAL) ==================
        elif opcao == "5":
            limpar_tela()
            menu_fase6()
            input("\nRetornando ao sistema integrado...\nPressione ENTER para voltar ao menu...")

        # ================= SAIR ==================
        elif opcao == "0":
            print("\nSaindo do sistema integrado...")
            break

        else:
            print("\nOpção inválida! Tente novamente.")
            input("\nPressione ENTER para voltar ao menu...")


if __name__ == "__main__":
    menu_principal()
