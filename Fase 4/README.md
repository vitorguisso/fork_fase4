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

- [**assets**](./assets): imagens do circuito Wokwi, prints do Serial Plotter, DER.
- [**document**](./document): Solução Técnica, Circuito e Lógica de Controle, modelo de banco de dados (MER/DER) e CRUD.
- [**scripts**](./scripts): arquivo `.sql` para criação e estrutura da tabela de irrigação.
- [**src**](./src):
  - `app.py`: Código Python com **Scikit-learn** e **Streamlit**
  - `codigo_ESP32.ino`: Código otimizado do ESP32 para o Wokwi (com Display LCD, Relay, sensores e Serial Plotter)
- **README.md**: este arquivo de guia geral.

---

## 🔧 Como executar tudo (passo a passo)

### 📌 **1) Simulador Wokwi**
- Abra o arquivo `codigo_ESP32.ino` no [Wokwi](https://wokwi.com/).
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

- **Instalar dependências:**
  ```bash
  pip install cx_Oracle pandas scikit-learn streamlit
