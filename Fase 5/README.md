# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
</a>
</p>

<br>

# FarmTech Solutions — Fase 5

## 👨‍🎓 Integrantes:
- [Ryan Carlos Sousa Alves da Cunha](https://www.linkedin.com/company/inova-fusca)
- [Vinícius Pereira Santana](https://www.linkedin.com/company/inova-fusca)
- [Vitor Augusto Prado Guisso](https://www.linkedin.com/company/inova-fusca)

## 👩‍🏫 Professores:
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)
### Coordenador(a)
- [Andre Godoi Chiovato](https://www.linkedin.com/company/inova-fusca)

---

## 📜 Descrição Geral

A Fase 5 contempla duas atividades integradas, voltadas à aplicação prática de Ciência de Dados no agronegócio e à simulação de custo computacional em ambiente de nuvem (AWS):

1. Previsão de Rendimento Agrícola com Machine Learning (Google Colab)
2. Simulação de Custos em Nuvem para Execução da Solução

---

## 📈 Atividade 1 — Previsão de Rendimento Agrícola com Regressão e Clusters

Notebook desenvolvido em Google Colab com os seguintes objetivos:

- Análise Exploratória dos Dados (EDA)
- Clusterização com KMeans + PCA
- Modelagem Preditiva com 5 algoritmos de regressão
- Avaliação com métricas (R², MAE, MSE, RMSE)
- Discussão crítica de resultados

**Base de dados utilizada:** `crop_yield.csv`

📎 [Abrir notebook no Google Colab](https://colab.research.google.com/github/vitorguisso/fork_fase4/blob/master/Fase%205/src/VitorGuisso_rm562317_pbl_fase5.ipynb)

> ⚠️ **Observação**:  
> O notebook utiliza `ipywidgets`, e por isso **não é renderizado corretamente no GitHub**.  
> Para visualização completa e interativa, abra diretamente no **Google Colab**.

---

### 🔍 Bibliotecas utilizadas

- `pandas`, `numpy`
- `matplotlib`, `seaborn`, `plotly`
- `sklearn`: KMeans, PCA, regressão, métricas
- `xgboost`
- `ipywidgets`

---

### 🔬 Clusterização com KMeans + PCA

- **K = 4 clusters**
- Redução dimensional com PCA (2D)
- Variáveis analisadas: temperatura, umidade, precipitação e produtividade

#### 🧠 Perfis de Clusters:

| Cluster | Perfil             | Yield Médio | Cultura dominante     |
|---------|--------------------|-------------|------------------------|
| 0       | Superprodutivo     | 178.310     | Oil palm fruit         |
| 1       | Equilibrado        | ~32.000     | Rice, Cocoa            |
| 2       | Moderado           | ~20.000     | Rubber, Beans          |
| 3       | Baixo Rendimento   | <10.000     | Rubber, Beans          |

---
## 🌽 Análise de Clusterização e Tendências de Produtividade Agrícola

### 🎯 Objetivo da Análise

Aplicar **clusterização (KMeans, K=4)** e **redução de dimensionalidade (PCA)** para agrupar culturas agrícolas com base em variáveis climáticas e produtivas: precipitação, temperatura, umidade relativa e rendimento (Yield). O objetivo foi encontrar padrões ocultos e auxiliar na tomada de decisão técnica e agronômica.

---

### 📊 Perfil dos Clusters

| Cluster | Condições Climáticas         | Yield Médio | Destaque                     |
|---------|------------------------------|-------------|------------------------------|
| 0       | Alta umidade e precipitação  | 178.310     | Oil palm fruit (66%)        |
| 1       | Temperatura alta, menos úmido| 29.671      | Cocoa, Rice, Rubber          |
| 2       | Clima ideal, mas baixo yield | 16.624      | Culturas mal adaptadas       |
| 3       | Clima seco, mas yield razoável| 51.344     | Boa resiliência das culturas |

---

### 📌 Principais Tendências e Insights

- **Cluster 0**: Altamente produtivo. Ideal para culturas tropicais. Indicado para investimento em tecnologias de precisão.
- **Cluster 1**: Clima bom, mas rendimento baixo. Pode exigir melhorias no manejo hídrico.
- **Cluster 2**: Condições perfeitas, porém desempenho fraco. Sinaliza problemas graves — pragas, solo ou genética inadequada.
- **Cluster 3**: Mesmo em clima desfavorável, apresenta rendimento superior ao Cluster 2 — indica **resiliência cultural**.

---

### 🚨 Detecção de Cenários Discrepantes (Outliers)

**Cluster 2** foi identificado como o mais preocupante:
- Clima favorável;
- Produtividade extremamente baixa;
- Indica falhas fora do clima: **cultura mal adaptada**, **problemas de solo**, **presença de pragas** ou **erro de manejo**.

---

### ✅ Conclusões Estratégicas

A clusterização foi eficaz para:

- Agrupar culturas com base em clima e rendimento real;
- Detectar **zonas de alto potencial não aproveitado**;
- Gerar insights sobre **substituição de culturas**, **ajustes técnicos**, e **foco em regiões resilientes**.

> Esta abordagem ajuda gestores agrícolas a tomar decisões mais embasadas, adaptando culturas às condições ambientais e otimizando o rendimento por hectare.





---
### 📊 Modelagem Preditiva

Foram utilizados:

1 - Regressão Linear

2 - Árvore de Decisão

3 - Floresta Aleatória

4 - KNN Regressor

5 - Support Vector Regressor

---

## 📌 Resumo e Conclusão

Durante esta fase, avaliamos o desempenho de diferentes algoritmos de regressão na previsão de rendimento agrícola com base em variáveis climáticas. Os principais resultados foram:

- **Regressão Linear** foi o único modelo a apresentar R² positivo em todas as culturas, destacando-se em *Rice* (R² = 0.3897), mas com poder explicativo ainda limitado.
- **Árvore de Decisão** e **Floresta Aleatória** tiveram desempenho insatisfatório, sugerindo overfitting ou variáveis insuficientes para explicar a produtividade.
- **KNN** apresentou leve vantagem em *Rice*, mas foi fraco nas demais culturas.
- **SVR** teve o pior desempenho geral, com R² negativo em todas as culturas, indicando incapacidade de generalizar padrões relevantes.

### 🔍 Possíveis causas para o baixo desempenho:

- **Base de dados pequena**: cada cultura possui apenas 39 amostras, o que compromete a robustez dos modelos.
- **Variáveis insuficientes**: apenas fatores climáticos foram considerados. Informações como tipo de solo, fertilizantes, genética, pragas e técnicas de manejo estão ausentes.
- **Falta de contexto agronômico**: ausência de dados sobre ciclos de cultivo, épocas de plantio ou características específicas das culturas dificultam a modelagem.
- **Tratamento superficial dos dados**: possíveis outliers e necessidade de agregações temporais (ex: médias mensais) não foram abordadas.

---

## ✅ Considerações Finais

Apesar dos resultados estatísticos modestos, o experimento foi valioso para:

- Testar e comparar diferentes algoritmos com dados reais;
- Refletir sobre a importância da qualidade e diversidade dos dados na modelagem preditiva;
- Identificar gargalos e oportunidades de melhoria na coleta e preparação dos dados.

### 📌 Recomendações futuras:

- Aumentar a base de dados com mais amostras por cultura;
- Incluir variáveis agronômicas e de manejo;
- Explorar modelos mais robustos e complexos (como XGBoost e Redes Neurais);
- Trabalhar em conjunto com especialistas do campo (engenheiros agrônomos, produtores).

> 🔁 **Em resumo**: os algoritmos não falharam — **os dados fornecidos foram limitantes**.  
> Uma base mais rica e contextualizada permitiria extrair todo o potencial dos modelos aplicados.

---
## ☁️ Atividade 2 — Estimativa de Custos na AWS

Simulação do custo de execução da solução de Machine Learning em duas regiões da AWS, considerando:
### 🔧 Especificações da instância:
- 2 CPUs
- 1 GiB 
- 5 Gbps de rede
- 50 GB 
- Linux (On-demand)

---

### 🌍 Comparativo de regiões

| Região               | Instância   | Custo Mensal | Observações                            |
|---------------------|-------------|--------------|----------------------------------------|
| São Paulo (sa-east-1)     | t3.micro    | USD 14,48     | ✅ Menor latência, conformidade LGPD     |
| Virgínia do Norte (us-east-1) | t3.micro    | USD 8,25      | ✅ Mais barato, ⚠️ Latência e LGPD       |

📄 [Ver estimativa completa na AWS](https://calculator.aws/#/estimate?id=5e388108dec7154c0db86ae2278a183ba6d2784f)

---

### ✅ Conclusão

- **Custo**: Virgínia é mais econômica (~28% mais barata)
- **Latência**: São Paulo atende melhor sensores no Brasil
- **LGPD**: Brasil é a escolha mais segura para dados sensíveis

🔎 A escolha depende do **nível de criticidade dos dados** e do **tempo de resposta necessário**.

---

## 🎥 Demonstração em Vídeo

📺 [Assista à demonstração de uso da AWS Calculator](https://youtu.be/SEU-LINK-AQUI)

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

* 0.1.0 - 09/09/2025  
  - Entrega completa da Fase 5: Colab + AWS

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>
