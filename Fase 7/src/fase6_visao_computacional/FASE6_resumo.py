import webbrowser


def mostrar_resumo_fase6():
    print("===== FASE 6 - VISÃO COMPUTACIONAL (FARMTECH SOLUTIONS) =====\n")

    print("Objetivo geral:")
    print("- Desenvolver e comparar diferentes abordagens de visão computacional")
    print("  para monitoramento em fazendas, com detecção simultânea de BOVINOS")
    print("  e FUNCIONÁRIOS em campo.\n")

    print("Contexto do projeto:")
    print("- Parte do ecossistema da FarmTech Solutions, focado em segurança,")
    print("  monitoramento operacional e apoio à gestão da fazenda.\n")

    print("Principais atividades desenvolvidas:")
    print("- Construção de um dataset com ~80 imagens rotuladas no MakeSense.ai;")
    print("- Duas classes: bovino e funcionário;")
    print("- Divisão em conjuntos de treino/validação/teste;")
    print("- Treinamento de modelos YOLO adaptáveis com 30 e 60 épocas;")
    print("- Avaliação de um YOLO pré-treinado (COCO) sem fine-tuning;")
    print("- Desenvolvimento de uma CNN do zero como baseline;")
    print("- Comparação quantitativa (precision, recall, mAP) e qualitativa;")
    print("- Geração de relatório técnico, gráficos e vídeos de demonstração.\n")

    print("Modelos avaliados:")
    print("- YOLO adaptável (fine-tuning com 30 épocas);")
    print("- YOLO adaptável (fine-tuning com 60 épocas);")
    print("- YOLO padrão (pré-treinado no dataset COCO);")
    print("- CNN desenvolvida do zero (baseline de classificação).\n")

    print("Principais resultados:")
    print("- YOLO adaptável com 30 épocas apresentou melhor equilíbrio,")
    print("  com mAP50 em torno de 0.8 e boas detecções para bovinos e funcionários;")
    print("- YOLO com 60 épocas apresentou sinais de overfitting (métricas piores),")
    print("  mostrando que mais épocas nem sempre significam melhor modelo;")
    print("- YOLO padrão COCO detectou bem pessoas, mas teve desempenho fraco")
    print("  para bovinos, pois não estava ajustado ao contexto da fazenda;")
    print("- A CNN do zero foi útil apenas como baseline, mas insuficiente para")
    print("  detecção robusta de múltiplos objetos em cenários reais.\n")

    print("Conclusão geral da Fase 6:")
    print("- O modelo YOLO adaptável com 30 épocas foi o mais adequado,")
    print("  oferecendo boa precisão, robustez e aplicabilidade prática;")
    print("- O projeto demonstrou o potencial da visão computacional para")
    print("  monitorar automaticamente animais e funcionários na fazenda;")
    print("- A solução pode ser integrada com outros módulos da FarmTech,")
    print("  como alertas em tempo real e dashboards de gestão.\n")

    print("Arquivos e resultados completos (notebooks, gráficos e inferências)")
    print("estão documentados no README da Fase 6, com links para:")
    print("- Notebook original no Google Colab;")
    print("- Vídeos de demonstração das entregas;")
    print("- Pasta no Google Drive com resultados e dataset.\n")

    input("Pressione ENTER para voltar ao menu da Fase 6...")


def abrir_colab_fase6():
    url = "https://colab.research.google.com/github/vitorguisso/fork_fase4/blob/master/Fase%206/src/VitorGuisso_rm562317_fase6.ipynb"
    print("\nAbrindo notebook da Fase 6 no Google Colab...\n")
    webbrowser.open(url)
    input("Pressione ENTER para voltar ao menu da Fase 6...")


def menu_fase6():
    while True:
        print("====================================")
        print("    FASE 6 - VISÃO COMPUTACIONAL    ")
        print("====================================\n")
        print("1 - Ver resumo da Fase 6 (YOLO, CNN, resultados)")
        print("2 - Abrir notebook da Fase 6 no Google Colab")
        print("0 - Voltar ao sistema integrado (Fase 7)")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            print()
            mostrar_resumo_fase6()
        elif opcao == "2":
            abrir_colab_fase6()
        elif opcao == "0":
            print("\nVoltando ao sistema integrado...\n")
            break
        else:
            print("\nOpção inválida! Tente novamente.\n")
