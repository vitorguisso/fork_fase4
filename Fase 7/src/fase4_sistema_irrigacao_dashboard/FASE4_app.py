# ========================
# IMPORTS NECESSÁRIOS
# ========================

import cx_Oracle
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import streamlit as st

# ========================
# CONEXÃO AO BANCO ORACLE
# ========================

username = "RM562317"
password = "100598"
dsn = "oracle.fiap.com.br/orcl"

connection = cx_Oracle.connect(username, password, dsn)
cursor = connection.cursor()

# ========================
# CONSULTA SQL
# ========================

cursor.execute("""
    SELECT umidade, ph, fosforo, potassio, bomba
    FROM sistema_irrigacao
""")

dados = cursor.fetchall()
columns = ["Umidade", "pH", "Fosforo", "Potassio", "Bomba"]

df = pd.DataFrame(dados, columns=columns)

# ========================
# TRATAMENTO DE DADOS
# ========================

# Mapear texto para números
df["Fosforo"] = df["Fosforo"].map({"Presente": 1, "Ausente": 0})
df["Potassio"] = df["Potassio"].map({"Presente": 1, "Ausente": 0})
df["Bomba"] = df["Bomba"].map({"LIGADA": 1, "DESLIGADA": 0})

X = df[["Umidade", "pH", "Fosforo", "Potassio"]]
y = df["Bomba"]

# ========================
# TREINAMENTO DO MODELO
# ========================

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

modelo = RandomForestClassifier()
modelo.fit(X_train, y_train)

y_pred = modelo.predict(X_test)
relatorio = classification_report(y_test, y_pred)

# ========================
# STREAMLIT DASHBOARD
# ========================

st.title("FarmTech Solutions - Dashboard Fase 4")

st.subheader("Dados Coletados")
st.dataframe(df)

st.subheader("Relatório do Modelo")
st.text(relatorio)

st.subheader("Previsão com Novos Dados")

umidade_input = st.slider("Umidade:", min_value=0, max_value=100, value=50)
ph_input = st.slider("pH:", min_value=0, max_value=14, value=7)
fosforo_input = st.selectbox("Fósforo:", ["Presente", "Ausente"])
potassio_input = st.selectbox("Potássio:", ["Presente", "Ausente"])

fosforo_num = 1 if fosforo_input == "Presente" else 0
potassio_num = 1 if potassio_input == "Presente" else 0

input_usuario = [[umidade_input, ph_input, fosforo_num, potassio_num]]
pred = modelo.predict(input_usuario)

st.success(f"Status da Bomba: {'LIGADA' if pred[0] == 1 else 'DESLIGADA'}")

# ========================
# FECHAR CONEXÃO
# ========================

cursor.close()
connection.close()
