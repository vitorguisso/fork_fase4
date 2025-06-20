# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href="https://www.fiap.com.br/"><img src="../assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Administração Paulista" width="40%"></a>
</p>

---

## FarmTech Solutions — Fase 4

### 👨‍🎓 Integrantes
- Vinícius Pereira Santana 1
- Vitor Augusto Prado Guisso 2
- Ryan Carlos Sousa Alves da Cunha 3

### 👩‍🏫 Professores
- **Tutor:** Lucas Gomes Moreira
- **Coordenador:** Andre Godoi Chiovato

---

## 📜 Introdução

Na Fase 4 aprimoramos:
- **Circuito ESP32**: Adicionamos um relé real para controlar a bomba de irrigação.
- **Display LCD**: Informações críticas em tempo real (umidade, status da bomba).
- **Scikit-learn**: Modelo preditivo para antecipar a irrigação.
- **Dashboard Streamlit**: Visualização interativa.
- **Banco Oracle**: Mantido para registrar histórico.

---

## 📜 Circuito Wokwi

- Sensores DHT22, LDR
- Botões para fósforo/potássio
- **Relé** para bomba
- **LCD I2C** para exibir dados
- Conexões otimizadas (SDA, SCL)

![Circuito Wokwi](../assets/circuito.PNG)

---

## 📜 Funcionamento

- Se a **umidade menor ou igual a 40%**, a bomba representada pelo relé é acionada até a umidade ficar maior que 40%.
- A predição do modelo complementa essa decisão.
- O display LCD mostra **Umidade (%)** e **Status da Bomba** diretamente no circuito.
- As demais informações (**pH, Fósforo, Potássio**) são exibidas no **Monitor Serial** com mensagens de orientação.
- O Serial Plotter mostra a curva de umidade em tempo real

---

## 🖥️ Monitor Serial

Abaixo, um exemplo da exibição das leituras no **Monitor Serial**, com mensagens de alerta para pH, fósforo e potássio:

![Monitor Serial](./assets/visor.png)

---

## 📈 Serial Plotter

O **Serial Plotter** mostra a curva de variação da umidade em tempo real, ajudando a visualizar o acionamento da bomba:

![Gráfico de Umidade](./assets/grafico_pHxumidade.png)


## 📜 Código ESP32

- Código C++ otimizado para economizar memória.
- Relé acionado via GPIO.
- LCD atualizado a cada leitura.

---

## 📜 Streamlit + Scikit-learn

- Dashboard com:
  - Tabela de registros
  - Gráfico de histórico de umidade
  - Previsão online de irrigação
- Pipeline salvo em pickle.

---

## 📜 Banco de Dados Oracle

- Mesma tabela `sistema_irrigacao`
- Scripts `CREATE`, `INSERT`, `SELECT` dentro de `scripts/`

---

## 📜 Conclusão

A Fase 4 integrou **hardware físico**, **Machine Learning**, **dashboard web** e **persistência de dados**, simulando um sistema de agricultura inteligente real.

---

