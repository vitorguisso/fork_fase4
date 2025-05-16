# Criando os vetores com os dados coletados
carboxina_hectare <- c(1.1, 1.3, 1.2, 1.4, 1.0, 1.2, 1.3, 1.1)  # Valores de Carboxina + Thiram por hectare
metomil_hectare <- c(0.4, 0.6, 0.5, 0.55, 0.45, 0.5, 0.52, 0.48)  # Valores de Metomil por hectare

# Cálculo da média e do desvio padrão para Carboxina + Thiram
media_carboxina <- mean(carboxina_hectare)
desvio_padrao_carboxina <- sd(carboxina_hectare)

# Cálculo da média e do desvio padrão para Metomil
media_metomil <- mean(metomil_hectare)
desvio_padrao_metomil <- sd(metomil_hectare)

# Exibir os resultados
print(paste("Média do consumo de Carboxina + Thiram por hectare:", round(media_carboxina, 2), "kg/hectare"))
print(paste("Desvio padrão do consumo de Carboxina + Thiram:", round(desvio_padrao_carboxina, 2), "kg/hectare"))

print(paste("Média do consumo de Metomil por hectare:", round(media_metomil, 2), "kg/hectare"))
print(paste("Desvio padrão do consumo de Metomil:", round(desvio_padrao_metomil, 2), "kg/hectare"))
