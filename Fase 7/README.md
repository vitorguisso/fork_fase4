# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
</a>
</p>

<br>

# FarmTech Solutions – Sistema Integrado de Monitoramento Agrícola (Fase 7)

## 👨‍🎓 Integrantes
- [Vinícius Pereira Santana]()
- [Vitor Augusto Prado Guisso]()

## 👩‍🏫 Professores
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)

### Coordenador(a)
- [Andre Godoi Chiovato](https://www.linkedin.com/company/inova-fusca)

---

## 📜 Descrição geral

Esta fase consolida todo o trabalho desenvolvido ao longo do ano pela FarmTech Solutions, integrando:

- Simulador de cálculo de plantio (Fase 1)  
- Sistema de controle de estoque com banco relacional Oracle (Fase 2)  
- Sistema de monitoramento de irrigação e sensores com bomba automática (Fases 3 e 4)  
- Envio de alertas inteligentes via AWS SNS com base nos dados dos sensores (Fase 5)  
- Módulo de visão computacional para monitoramento de fazendas (Fase 6)  

Tudo é acessado por meio de um único menu em linha de comando:

`Fase 7/src/fase7_sistema_integrado/dashboard.py`

O sistema integrado permite:

- Navegar entre todas as fases do projeto  
- Conectar ao banco Oracle FIAP  
- Enviar alertas automáticos para e-mail através da AWS  
- Visualizar o menu da visão computacional e seus resultados  

---

## 🧪 Atividades desenvolvidas por fase

### **Fase 1 – Cálculo de plantio**
- Estimativa da população de plantas por hectare  
- Dados considerados:
  - Espaçamento entre linhas  
  - Espaçamento entre plantas  
  - Área total de cultivo  

### **Fase 2 – Controle de estoque com Oracle**
- CRUD completo de insumos agrícolas  
- Uso de `cx_Oracle` para conexão remota  
- Organização do código com menu próprio  

### **Fases 3 e 4 – Sistema de irrigação e sensores**
- Sensores simulados: umidade, pH, fósforo e potássio  
- Armazenamento em tabela Oracle `sistema_irrigacao`  
- Bomba ligada/desligada com base na umidade (< 40%)  
- Menus para inserir, atualizar, deletar e listar registros  

### **Fase 5 – AWS SNS**
- Tópico SNS configurado para alertas automáticos  
- E-mails enviados conforme leituras dos sensores  
- Recomendações geradas automaticamente  
- Integração via `boto3` e variáveis de ambiente no sistema  

### **Fase 6 – Visão computacional**
- Detecta bovinos e funcionários  
- Comparação entre:
  - YOLO adaptado (treinado)  
  - YOLO pré-treinado (COCO)  
  - CNN desenvolvida do zero  
- Resultados apresentados em vídeo e notebook  

### **Fase 7 – Sistema Integrado**
Menu completo com:

1. Abrir sistema de cálculo de plantio (Fase 1)  
2. Abrir sistema de controle de estoque (Fase 2)  
3. Abrir sistema de irrigação e sensores (Fases 3 e 4)  
4. Enviar alerta AWS com base nos sensores (Fase 5)  
5. Abrir menu da visão computacional (Fase 6)  
0. Sair  

---

## 🔗 Links importantes

- 📓 **Notebook Fase 6:**  
  https://github.com/vitorguisso/fork_fase4/blob/master/Fase%206/src/VitorGuisso_rm562317_fase6.ipynb  

- 📁 **Google Drive — arquivos da visão computacional:**  
  https://drive.google.com/drive/folders/1SmJSAe45lyQtrxiUbv5JriFim3BAgRya  

- 🎥 **Vídeo de demonstração da Fase 7 (sistema integrado):**  
  [Vídeo Demonstração Fase 7](https://www.youtube.com/watch?v=2mTAzm6e73U)

---

## 🧰 Bibliotecas principais utilizadas

- `cx_Oracle` – conexão com Oracle  
- `boto3` – AWS SNS  
- `ultralytics` – YOLO (detecção)  
- `opencv-python` – processamento de imagens  
- `tensorflow` – CNN (baseline)  
- `pandas`, `numpy`, `matplotlib` – análise / gráficos  
- `scikit-learn` – ML (RandomForest, métricas)  
- `streamlit` – dashboard (Fase 4 App)  

---

# 🔧 Como executar o projeto

## **1. Pré-requisitos**
- Python 3.10 ou superior  
- Oracle Instant Client 64 bits instalado  
- Acesso ao Oracle FIAP  
- Conta AWS com permissão SNS  
- Git instalado  

---

## **2. Clonar o repositório**

```bash
git clone https://github.com/vitorguisso/fork_fase4.git
cd "fork_fase4/Fase 7"

