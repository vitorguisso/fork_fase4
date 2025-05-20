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


## 📜 MER
*Porém nesse documento abordaremos aspectos das operações CRUD e o relacionamento do MER realizados.*


*Para a criação do banco utilizamos a seguinte lógica
1 Fazenda tem várias culturas = Fazenda 1:N
1 Cultura tem vários sensores = Cultura 1:N
1 Sensor tem várias leituras = Sensor 1:N
*
![MER](assets/DER.png)


# 📦 CRUD do Sistema de Irrigação

Este arquivo descreve o funcionamento completo do CRUD (Create, Read, Update, Delete) implementado no projeto de irrigação automatizada.

---

## ✅ CREATE – Inserir novo registro

- O usuário fornece os seguintes dados:
  - Umidade (% entre 0 e 100)
  - pH (entre 0 e 14)
  - Fósforo (Presente/Ausente)
  - Potássio (Presente/Ausente)

- A lógica do sistema define automaticamente o status da bomba:
  - Se umidade < 40%, bomba = LIGADA
  - Caso contrário, bomba = DESLIGADA

- Os dados são inseridos na tabela `sistema_irrigacao` do banco Oracle.

---

## 🔍 READ – Visualizar registros

- Mostra todos os registros salvos no banco Oracle.
- Campos exibidos:
  - ID, Umidade, pH, Fósforo, Potássio, Bomba

- A bomba reflete o valor salvo no registro.

---

## 🔁 UPDATE – Atualizar registro

- O usuário informa:
  - ID do registro a ser atualizado
  - Campo a ser alterado (`umidade`, `ph`, `fosforo`, `potassio`)
  - Novo valor (validado pelo sistema)

- Se o campo alterado for `umidade`, a bomba é reavaliada automaticamente com base na nova umidade.

---

## 🗑️ DELETE – Remover registro

- O usuário informa o ID do registro a ser excluído.
- O registro é removido da tabela `sistema_irrigacao`.

---

## 🧩 Observações

- A bomba não é editável diretamente. Seu valor depende da umidade.
- Todos os dados são persistidos no banco de dados Oracle via `cx_Oracle`.
- Script implementado no arquivo `sistema_irrigacao.py`.

---


