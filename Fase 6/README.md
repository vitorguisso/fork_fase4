# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
</a>
</p>

<br>

#  FarmTech Solutions — Fase 6

## 👨‍🎓 Integrantes:
- [Vinícius Pereira Santana](https://www.linkedin.com/company/inova-fusca)
- [Vitor Augusto Prado Guisso](https://www.linkedin.com/company/inova-fusca)

## 👩‍🏫 Professores:
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)
### Coordenador(a)
- [Andre Godoi Chiovato](https://www.linkedin.com/company/inova-fusca)

---

## 📜 Descrição Geral

Nesta fase, o objetivo foi **desenvolver e comparar diferentes abordagens de visão computacional** aplicadas a um **problema real de monitoramento em fazendas** — detecção simultânea de bovinos e funcionários.

A **FarmTech Solutions**, empresa fictícia de inovação no agronegócio, busca demonstrar aos clientes como um sistema de visão computacional pode ser aplicado na prática, garantindo:

- Monitoramento de animais no campo  
- Identificação de funcionários em áreas delimitadas  
- Potencial de automação para segurança e controle operacional

---

## 🧪 Atividades Desenvolvidas

- Construção de dataset com 80 imagens rotuladas manualmente no **MakeSense.ai**  
- Treinamento e teste de modelos YOLO adaptáveis (30 e 60 épocas)  
- Avaliação de YOLO pré-treinado (COCO) sem treinamento adicional  
- Desenvolvimento de uma **CNN do zero** como baseline de classificação  
- Comparação quantitativa e qualitativa entre os três modelos:
  - YOLO Adaptável
  - YOLO Padrão (COCO)
  - CNN do zero
- Geração de métricas (Precision, Recall, mAP50, mAP50-95, Latência)
- Construção de relatório técnico e README estruturado para entrega.

---

## 🔗 Links Importantes

- [📓 Notebook Fase 6](https://github.com/vitorguisso/fork_fase4/blob/master/Fase%206/src/VitorGuisso_rm562317_pbl_fase6.ipynb) (Caso não abra corretamente, utilize o arquivo .ipynb localizado em scripts)
- 📺 **Vídeo de Demonstração (5 min):** [YouTube - Não listado](#)  

---
## 📁 Arquivos do Projeto — Fase 6

Todos os arquivos gerados e utilizados neste projeto estão disponíveis em uma única pasta no Google Drive:

👉 [Acessar Arquivos no Google Drive](https://drive.google.com/drive/folders/1SmJSAe45lyQtrxiUbv5JriFim3BAgRya)

### 📦 Conteúdo da Pasta

- `DADOS GERADOS COLAB.zip` — Arquivo compactado contendo:
  - Resultados de treinamento YOLO (pesos, métricas, inferências)
  - Resultados da avaliação dos modelos (YOLO adaptável, YOLO COCO e CNN)
  - Arquivos auxiliares e gráficos gerados no Colab

- `DATASET.rar` — Dataset completo utilizado para treino, validação e teste:
  - Imagens e labels no formato YOLO
  - Duas classes: *bovino* e *funcionário*

---

### 🛠️ Como Utilizar no Colab

1. Faça o download do arquivo desejado (`.zip` ou `.rar`).
2. Extraia o conteúdo dentro do diretório `/content/` no Google Colab.
3. Atualize os caminhos no notebook, se necessário, para apontar para as pastas extraídas.
4. Execute o notebook para reproduzir os resultados ou realizar novos testes.

---

✅ **Dica:**  
- Para executar apenas o modelo já treinado → baixe **`DADOS GERADOS COLAB.zip`**.  
- Para refazer todo o treinamento → baixe também **`DATASET.rar`**.


---

## 🧰 Bibliotecas Utilizadas

- `ultralytics` — YOLOv8 (detecção)  
- `tensorflow` — CNN do zero (classificação)  
- `numpy`, `pandas` — manipulação de dados  
- `matplotlib` — visualizações e gráficos  
- `scikit-learn` — métricas (classification report e matriz de confusão)  
- `opencv-python` — manipulação de imagens

---

## 📝 Conclusão Final — Entrega 1 (Fase 6 - FarmTech Solutions)

Nesta entrega, foi desenvolvido um **sistema de visão computacional baseado em YOLOv8**, com o objetivo de demonstrar na prática o potencial de redes neurais para detecção de objetos em imagens. A solução faz parte da expansão da FarmTech Solutions para novas áreas de atuação, incluindo **segurança patrimonial**, **controle de acesso de funcionários** e **saúde animal**.

### 📌 Resumo da Solução Desenvolvida

- **Dataset** com duas classes (*bovino* e *funcionário*), totalizando mais de 80 imagens.  
- **Rotulagem** feita no MakeSense.ai, com divisão em train/val/test.  
- **Treinamento** de dois modelos: 30 e 60 épocas.  
- **Modelo base:** `yolov8n.pt` (leve e rápido).  
- **Avaliação:** Precision, Recall, mAP50 e inspeção visual com diferentes limiares de confiança.

### 📊 Principais Resultados

- **30 épocas:**  
  - Precision e Recall elevados.  
  - mAP50 ≈ 0.8.  
  - Predições coerentes e bem delimitadas.  

- **60 épocas:**  
  - Colapso com CONF=0.25 (métricas zeradas).  
  - Baixa confiança nas predições (overfitting).

- **Limiar 0.01:**  
  - Modelo de 60 épocas ainda detectava objetos, mas com confiança baixa.  
  - Modelo de 30 épocas manteve bom desempenho.

### 🧠 Análise Crítica

- Mais épocas não significam melhor desempenho: **o modelo de 60 épocas superajustou** ao dataset pequeno.  
- Técnicas como **early stopping** e **data augmentation** ajudam a mitigar esse problema.  
- O modelo leve (`yolov8n`) facilitou prototipagem rápida, mas também saturou mais cedo.

### ✅ Conclusão Geral

- O modelo de **30 épocas foi superior**, atingindo métricas sólidas e bom equilíbrio entre precisão e robustez.  
- O modelo de 60 épocas apresentou overfitting, perdendo capacidade de generalização.  
- A solução apresenta potencial real para aplicações em monitoramento rural.

---

## 📊 Conclusão Final — Entrega 2 (Comparativo de Modelos)

Após a implementação e avaliação dos três modelos propostos — **CNN do zero**, **YOLO padrão (pré-treinado COCO)** e **YOLO adaptável (fine-tuning)** — foi possível observar diferenças claras em desempenho, robustez e capacidade de generalização.

| Modelo                     | Arquitetura                       | Acurácia (Test) | Precision | Recall | mAP50 | mAP50-95 | Tempo de Inferência (ms/img) | Classes Simultâneas | Observações Principais                                                                 |
|----------------------------|-------------------------------------|-----------------|-----------|--------|--------|-----------|-------------------------------|----------------------|-----------------------------------------------------------------------------------------|
| CNN do Zero                | ConvNet (3 blocos)                 | **0.25**        | —         | —      | —      | —         | —                             | ❌ (single-label)   | Modelo simples, rápido, mas incapaz de generalizar bem; previu majoritariamente uma única classe. |
| YOLO Padrão (COCO)         | Detector pré-treinado (COCO)       | —              | **1.00**  | **1.00**| —      | —         | **196.87**                    | ✅ (multi-objeto)   | Reconheceu corretamente bovinos e funcionários com base em classes “cow” e “person” já aprendidas no COCO. |
| YOLO Adaptável (ep30)      | YOLO treinado no dataset próprio   | —              | **0.804** | **0.571**| **0.706** | **0.448** | —                           | ✅ (multi-objeto)   | Bom desempenho geral, com detecção consistente das classes no dataset customizado.     |
| YOLO Adaptável (ep60)      | YOLO treinado no dataset próprio   | —              | **0.000** | **0.000**| **0.000** | **0.000** | —                           | ✅ (multi-objeto)   | Overfitting evidente ou falha no treinamento. O modelo perdeu capacidade de generalização. |

### 📌 Principais Diferenças
- **YOLO adaptável (ep30)** apresentou bom equilíbrio entre precisão e recall.  
- **YOLO padrão (COCO)** teve 100% de precisão e recall nas classes cow/person, mostrando força do transfer learning.  
- **CNN** foi insuficiente para cenários multi-objeto.

---

## 🧭 Conclusão Geral do Projeto

- ✅ **Modelos simples (CNN do zero)** servem como baseline, mas são limitados.  
- 🚀 **YOLO padrão (pré-treinado)** é útil para protótipos rápidos.  
- 🧠 **YOLO adaptável (30 épocas)** foi o melhor modelo, equilibrando precisão, robustez e aplicabilidade prática.  
- ⚠️ **YOLO adaptável (60 épocas)** reforçou a importância de evitar overfitting em datasets pequenos.

👉 **Recomendação prática:** Para aplicações reais de monitoramento em fazendas, a melhor estratégia é usar **YOLO pré-treinado com fine-tuning (30 épocas)**, garantindo detecção simultânea de bovinos e funcionários com alta confiabilidade.

---

## 🚀 Sugestões de Melhoria

- Balancear e expandir o dataset para reduzir viés e melhorar generalização.  
- Aplicar *early stopping* e *data augmentation* no treinamento.  
- Ajustar limiares de detecção para otimizar precisão e recall.  
- Testar YOLO em cenários reais (vídeo/streaming em tempo real).  
- Explorar outras arquiteturas (Faster R-CNN, EfficientDet) para comparação futura.

---
## 📁 Estrutura de Pastas

| Pasta/Arquivo                | Descrição |
| ---------------------------  | --------- |
| **assets/**                  | Imagens e gráficos |
| **document/**                | Documentos técnicos (PDFs, relatórios) |
| **scripts/**                 | Scripts auxiliares |
| **src/**                     | Código principal (`.ipynb`) |
| **README.md**                | Instruções e documentação do projeto |

---

## 🗂️ Histórico de Lançamentos

* 0.1.0 - 14/10/2025  
  - Entrega completa da Fase 6
---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

