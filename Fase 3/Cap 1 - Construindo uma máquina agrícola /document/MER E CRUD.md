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


## 📜 MER
*Porém nesse documento abordaremos aspectos das operações CRUD e o relacionamento do MER realizados.*


*Para a criação do banco utilizamos a seguinte lógica
1 Fazenda tem várias culturas = Fazenda 1:N
1 Cultura tem vários sensores = Cultura 1:N
1 Sensor tem várias leituras = Sensor 1:N
*

![MER](workinspace/Fase 3/Cap 1 - Construindo uma máquina agrícola)/assets/DER.png


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

## 📁 Estrutura de pastas

Dentre os arquivos e pastas presentes na raiz do projeto, definem-se:

- <b>assets</b>: Aqui estão os arquivos relacionados as imagens, do circuíto, DER e logotipo da FIAP presentes no projeto.

- <b>config</b>: Posicione aqui arquivos de configuração que são usados para definir parâmetros e ajustes do projeto.

- <b>document</b>: Aqui encontra se disponívelr.

- <b>scripts</b>: aqui estão arquivos de backup .py, json e SQL.

- <b>src</b>: Aqui estão localizados os arquivos contendo  o arquivo executavel.py e estoque json originais.

- <b>README.md</b>: arquivo que serve como guia e explicação geral sobre o projeto (o mesmo que você está lendo agora).

## 🔧 Como executar o código

*Nesse projeto foram utilizados Oracle SQL Developer, Biblioteca Python cx_Oracle, Oracle Instant Client, Visual Studio.*


## 🗃 Histórico de lançamentos

* 0.1.0 - 19/05/2025*

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


