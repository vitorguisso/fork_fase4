# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/">
  <img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" border="0" width="40%" height="40%">
</a>
</p>

<br>

# FarmTech Solutions — Fase 4

## 👨‍🎓 Integrantes:
- [Vinícius Pereira Santana](https://www.linkedin.com/company/inova-fusca)
- [Vitor Augusto Prado Guisso](https://www.linkedin.com/company/inova-fusca)

## 👩‍🏫 Professores:
### Tutor(a)
- [Lucas Gomes Moreira](https://www.linkedin.com/company/inova-fusca)
### Coordenador(a)
- [Andre Godoi Chiovato](https://www.linkedin.com/company/inova-fusca)

---

## 📜 Descrição

Este projeto simula um sistema **inteligente de irrigação e monitoramento** usando:
- Sensores de **umidade**, **pH**, **presença de fósforo e potássio**
- Controle automatizado de **bomba de água** usando **ESP32** no **Wokwi**
- Interface gráfica com **Streamlit**
- Modelagem preditiva com **Scikit-learn**
- Integração com **Banco de Dados Oracle**
- Visualização de dados com **Serial Plotter**

O sistema coleta dados em tempo real, decide quando irrigar, armazena no banco de dados e permite visualização e previsões pelo dashboard.

---

## 📁 Estrutura de Pastas

## 📂 **Estrutura do Repositório**

| Pasta/Arquivo                | Descrição |
| ---------------------------  | --------- |
| **assets/**                  | Imagens do circuito, gráficos, logo, prints |
| **document/**                | Documentos técnicos: MER, CRUD, Solução Técnica |
| **scripts/**                 | Scripts SQL para criação da tabela `sistema_irrigacao` |
| **src/**                     | Códigos executáveis: `app.py` (Streamlit + Scikit-learn), `sistema_irrigacao.py` (CRUD com Oracle),C++ |
| **README.md**                | Este arquivo com instruções gerais |

---
## 🔗 **Links**

- [🌐 Acesse o Circuito Wokwi](https://wokwi.com/projects/434291929867724801)
- [▶️ Assista ao Vídeo no YouTube](https://youtu.be/hbWBFAC73Io)

## 🔧 Como executar

### 📌 **1) Simulador Wokwi**
- [🌐 Acesse o Circuito Wokwi](https://wokwi.com/projects/434291929867724801)
- Rode o circuito para visualizar:
  - Sensores simulados
  - Relay simulando a bomba
  - Display LCD com status
  - Serial Plotter mostrando a variável de umidade.

### 📌 **2) Backend Python**
- **Requisitos:**
  - Python 3.x
  - Pacotes:
    - `cx_Oracle`
    - `pandas`
    - `scikit-learn`
    - `streamlit`
  - Oracle Instant Client 64-bit
     Baixe e configure no PATH.
    
- **Instalar dependências:**
  ```bash
  pip install cx_Oracle pandas scikit-learn streamlit

ATENÇÃO: No código está configurado com:
