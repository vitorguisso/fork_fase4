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

![Circuito Wokwi](../assets/circuito%20limpo.PNG)

---

## 📜 Funcionamento

- Se a **umidade < 40%**, o relé liga a bomba.
- A predição do modelo complementa essa decisão.
- O LCD exibe: Umidade, pH, Fósforo, Potássio, Status da bomba.
- O Serial Plotter mostra a curva de umidade em tempo real.

---

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

