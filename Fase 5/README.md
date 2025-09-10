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

## 📜 Descrição

Este projeto foi desenvolvido para analisar dados climáticos e de solo com o objetivo de prever o **rendimento agrícola** em fazendas atendidas pela FarmTech Solutions. A Fase 5 é composta por duas entregas complementares:

### 📌 Parte 1 — Google Colab:  
**Previsão de Rendimento Agrícola com Regressão Supervisionada e Análise de Clusters**

Etapas realizadas:
- Análise Exploratória dos Dados (EDA)
- Identificação de padrões com **KMeans (K=4)** + **PCA**
- Modelagem Preditiva com **5 algoritmos de Regressão**:
  - Linear Regression
  - Decision Tree Regressor
  - Random Forest Regressor
  - SVR (Support Vector Regression)
  - XGBoost Regressor
- Avaliação com métricas: R² Score, MAE, MSE, RMSE

Base de dados utilizada: `crop_yield.csv`

---

## 🧠 Principais Bibliotecas Utilizadas

- `pandas`, `numpy`
- `matplotlib`, `seaborn`, `plotly`
- `sklearn` (PCA, KMeans, métricas, regressão)
- `xgboost`

---

## 📈 Clusterização com PCA + KMeans

- Redução de dimensionalidade com PCA para 2D
- Agrupamento em 4 clusters:
  - **Cluster 0 ("Superprodutivo")**: clima ideal, dominado por *Oil palm fruit*
  - **Cluster 1 ("Equilíbrio")**: culturas com bom rendimento e estabilidade
  - **Cluster 2 ("Moderado")**: boa umidade, menor yield
  - **Cluster 3 ("Baixo rendimento")**: condições climáticas menos favoráveis

Insights:
- Mesmo sob clima similar, cada cultura responde de forma única.
- *Oil palm fruit* distorce modelos se não for tratada separadamente.
- Agrupar culturas permite modelos mais estáveis e específicos.

---

## 🤖 Modelos Preditivos

Os seguintes modelos foram treinados com validação cruzada:

- **Linear Regression** → base de comparação
- **Random Forest** → alto desempenho com poucos ajustes
- **XGBoost** → melhor resultado geral
- **SVR** → desempenho mediano
- **Decision Tree** → rápido, mas propenso a overfitting

Métricas como RMSE e R² foram usadas para avaliar a performance dos modelos. O **XGBoost** apresentou o melhor equilíbrio entre precisão e robustez.

---

## 📁 Estrutura de Pastas

| Pasta/Arquivo                | Descrição |
| ---------------------------  | --------- |
| **assets/**                  | Imagens, gráficos e logos |
| **document/**                | Documentos técnicos e relatórios |
| **scripts/**                 | Scripts auxiliares (ex: manipulação de dados) |
| **src/**                     | Código-fonte principal (ex: notebook Colab) |
| **README.md**                | Este arquivo de apresentação |

---

## 🗂️ Histórico de Lançamentos

* 0.1.0 - 09/09/2025  
  - Entrega inicial da análise preditiva e clusterização

---

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>

