# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Bio Machine

## Machine FIAP

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/company/inova-fusca">Vinícius Pereira Santana 1</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Vitor Augusto Prado Guisso 2</a>
- <a href="https://www.linkedin.com/company/inova-fusca">Ryan Carlos Sousa Alves da Cunha 3</a> 

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Lucas Gomes Moreira</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Andre Godoi Chiovato</a>


## 📜 Introdução

*O presente projeto tem como objetivo elaborar a primeira máquina agrícula capaz de medir parâmetros através da simulação de sensores Fósforo, Potássio, PH e umidade do solo. Porém nesse documento abordaremos aspectos das operações CRUD e o relacionamento do MER realizados.*

## 📜 Objetivo

*O objetivo deste projeto é simular um sistema de irrigação e monitoramento por sensores que medem a umidade do solo, pH, presença de fósforo e potássio. Com base nessas medições, o sistema decide automaticamente se deve acionar a bomba de água. Além disso, informa o usuário sobre a presença ou ausência dos nutrientes fósforo e potássio, e se o solo está ácido, ideal ou alcalino.
Além disso, os dados são integrados a um banco de dados Oracle, permitindo o gerenciamento completo via Python.*


## 📜 Circuíto no Wokwi

![Circuito Wokwi](workinspace/Fase 3/Cap 1 - Construindo uma máquina agrícola)/assets/circuito limpo.PNG

Acesse o link de compartilhamento do projeto no [Wokwi](https://wokwi.com/projects/431425340498998273).

## 📜 Componentes do Wokwi

*Microcontrolador ESP32
Sensor DHT22: simula a umidade do solo
Sensor LDR: simula o pH do solo por variação de luminosidade
Botão 1: simula a presença/ausência de fósforo
Botão 2: simula a presença/ausência de potássio
LED: simula a bomba de irrigação (ligada/desligada)
*

## 📜 Lógica de Funcionamento


*A umidade é lida pelo DHT22. Caso o valor da umidade seja menor que 40%, então a bomba de irrigação (Led) é acionada automaticamente até que a umidade volte a ser maior ou igual a 40%.
O sensor de PH é simulado pelo LDH. O valor lido é convertido para a escala de pH entre 0 e 14. Foi considerado um pH ácido valores abaixo de 5,5 e pH alcalino valores acima de 7,5. 
Os Sensores de fósforo e potássio foram representados por botões. Caso o botão esteja pressionado então o nutriente é considerado presente. 
Vale ressaltar que para os dados de pH, presença/ausência de fósforo e potássio, o programa apenas avisa ao usuário o que está ocorrendo e sugere ações a serem tomadas.
*

## 📜 Código Wokwi C++

*
#include "DHT.h"

// DEFINIÇÃO DOS PINOS
#define DHTPIN 14            // Pino do sensor DHT22 (umidade)
#define DHTTYPE DHT22 
#define LDRPIN 34           // Pino do sensor LDR (simula pH)
#define FOSFORO_PIN 12      // Botão para fósforo
#define POTASSIO_PIN 13    // Botão para potássio
#define LED_BOMBA 27      // LED representa a bomba de irrigação

DHT dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  dht.begin();

// Configura os modos dos pinos
  pinMode(LDRPIN, INPUT);
  pinMode(FOSFORO_PIN, INPUT_PULLUP);
  pinMode(POTASSIO_PIN, INPUT_PULLUP);
  pinMode(LED_BOMBA, OUTPUT);

  digitalWrite(LED_BOMBA, LOW);
}

void loop() {
  // Leitura da umidade
  float umidade = dht.readHumidity();

  // Leitura dos botões: pressionado = presença, solto = ausência
  bool fosforoPresente = digitalRead(FOSFORO_PIN) == LOW;
  bool potassioPresente = digitalRead(POTASSIO_PIN) == LOW;

  // Leitura do LDR para simular pH
  int ldrValor = analogRead(LDRPIN);
  float ph = map(ldrValor, 0, 4095, 0, 140) / 10.0;
  ph = constrain(ph, 0.0, 14.0);

  // Lógica da bomba (somente umidade)
  bool bombaLigada = (umidade < 40.0);

  digitalWrite(LED_BOMBA, bombaLigada ? HIGH : LOW);

  // Exibir leituras no Serial
  Serial.print("Umidade: ");
  Serial.print(umidade);
  Serial.print(" % | pH: ");
  Serial.print(ph);
  Serial.print(" | Fósforo: ");
  Serial.print(fosforoPresente ? "Presente" : "Ausente");
  Serial.print(" | Potássio: ");
  Serial.print(potassioPresente ? "Presente" : "Ausente");
  Serial.print(" | Bomba: ");
  Serial.println(bombaLigada ? "LIGADA" : "DESLIGADA");

  // Análise de necessidade dos insumos:
  if (!fosforoPresente) {
    Serial.println("→ ATENÇÃO: Necessário corrigir Fósforo no solo.");
  } else {
    Serial.println("→ Fósforo OK.");
  }

  if (!potassioPresente) {
    Serial.println("→ ATENÇÃO: Necessário corrigir Potássio no solo.");
  } else {
    Serial.println("→ Potássio OK.");
  }

  if (ph < 5.5) {
    Serial.println("→ ATENÇÃO: pH ácido! Necessário corrigir.");
  } else if (ph > 7.5) {
    Serial.println("→ ATENÇÃO: pH alcalino! Necessário corrigir.");
  } else {
    Serial.println("→ pH dentro da faixa ideal.");
  }

  Serial.println("-----------------------------");

  delay(2000);
}
*

## 📜 Exemplo do painel do Wokwi com informações passadas ao usuário

*
-----------------------------
Umidade: 50.50 % | pH: 6.40 | Fósforo: Ausente | Potássio: Ausente | Bomba: DESLIGADA
→ ATENÇÃO: Necessário corrigir Fósforo no solo.
→ ATENÇÃO: Necessário corrigir Potássio no solo.
→ pH dentro da faixa ideal.
-----------------------------
Umidade: 50.50 % | pH: 6.40 | Fósforo: Presente | Potássio: Ausente | Bomba: DESLIGADA
→ Fósforo OK.
→ ATENÇÃO: Necessário corrigir Potássio no solo.
→ pH dentro da faixa ideal.
-----------------------------
Umidade: 50.50 % | pH: 6.40 | Fósforo: Ausente | Potássio: Presente | Bomba: DESLIGADA
→ ATENÇÃO: Necessário corrigir Fósforo no solo.
→ Potássio OK.
→ pH dentro da faixa ideal.
-----------------------------
Umidade: 50.50 % | pH: 2.60 | Fósforo: Ausente | Potássio: Ausente | Bomba: DESLIGADA
→ ATENÇÃO: Necessário corrigir Fósforo no solo.
→ ATENÇÃO: Necessário corrigir Potássio no solo.
→ ATENÇÃO: pH ácido! Necessário corrigir.
-----------------------------
Umidade: 42.00 % | pH: 11.90 | Fósforo: Ausente | Potássio: Ausente | Bomba: DESLIGADA
→ ATENÇÃO: Necessário corrigir Fósforo no solo.
→ ATENÇÃO: Necessário corrigir Potássio no solo.
→ ATENÇÃO: pH alcalino! Necessário corrigir.
-----------------------------
Umidade: 27.00 % | pH: 11.90 | Fósforo: Ausente | Potássio: Ausente | Bomba: LIGADA
→ ATENÇÃO: Necessário corrigir Fósforo no solo.
→ ATENÇÃO: Necessário corrigir Potássio no solo.
→ ATENÇÃO: pH alcalino! Necessário corrigir.
-----------------------------
Umidade: 41.00 % | pH: 7.20 | Fósforo: Presente | Potássio: Ausente | Bomba: DESLIGADA
→ Fósforo OK.
→ ATENÇÃO: Necessário corrigir Potássio no solo.
→ pH dentro da faixa ideal.
*
## 📜 Integração em código python e Oracle

*
O código Python conecta-se ao banco de dados Oracle e permite:
    • Inserção de novos dados com base nas simulações do Wokwi
    • Atualização individual de campos (pH, umidade, fósforo, potássio)
    • Exclusão de registros
    • Exibição completa do banco com formatação clara
    • A bomba é calculada automaticamente com base na umidade inserida.
*

## 📜 SQL table Oracle

*
CREATE TABLE sistema_irrigacao (
  id                        NUMBER GENERATED BY DEFAULT ON NULL AS IDENTITY PRIMARY KEY,
  umidade           NUMBER(5,2),
  ph                      NUMBER(4,2),
  fosforo              VARCHAR2(10),
  potassio           VARCHAR2(10),
  bomba             VARCHAR2(10)
);
*
## 📜 Visualização dos dados armazenados na tabela Oracle após algumas manipulações via python:

![Dados](workinspace/Fase 3/Cap 1 - Construindo uma máquina agrícola)/assets/dados.png

*Print do comando SELECT * FROM sistema_irrigacao no Oracle SQL Developer, exibindo os dados armazenados pela integração com o Python.*

## 📜 Vídeos explicativos
Acesse o link do vídeo explicativo do projeto pt1 [Wokwi](https://youtu.be/U5qKTlOQY6w).
Acesse o link do vídeo explicativo do projeto pt2 [Wokwi](https://youtu.be/BLC7gruKot8).
Acesse o link do vídeo explicativo do projeto pt3 [Wokwi](https://youtu.be/cwMhXKpyLPk).

## 📜 Conclusão
*
O projeto desenvolvido simulou com sucesso a aplicação prática de sensores e automação no contexto da irrigação agrícola, utilizando a plataforma Wokwi para simulação do circuito e o ESP32 como microcontrolador. A lógica implementada em C++ permitiu o monitoramento em tempo real da umidade do solo, valor de pH, e presença de nutrientes essenciais como fósforo e potássio, além do acionamento automático da bomba de irrigação.
A segunda parte do projeto envolveu a integração com Python e Oracle, onde os dados gerados foram armazenados, atualizados, consultados e manipulados de forma estruturada. Essa integração possibilitou a simulação de um sistema completo de gerenciamento agrícola inteligente, reunindo conceitos de eletrônica, programação embarcada, bancos de dados e análise de dados.
*

## 🔧 Como executar o código

*
- Python 3.x instalado
- Pacotes:
  - cx_Oracle
  - pandas
- Oracle Instant Client 64-bit (instalado e configurado no Path)
- Conta ativa Oracle FIAP (banco de dados remoto)*

## 🔧 CONEXÃO COM O BANCO ORACLE
*
⚠️ Importante: Este projeto está configurado com os dados do aluno RM562317.
Se outro usuário for testar, é necessário alterar as credenciais no código.

Substitua por seus dados:
username = "SEU_USUARIO"  # Ex: RM123456
password = "SUA_SENHA"
dsn = "oracle.fiap.com.br/orcl"
*


## 🗃 Histórico de lançamentos

* 0.1.0 - 19/05/2025*

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


