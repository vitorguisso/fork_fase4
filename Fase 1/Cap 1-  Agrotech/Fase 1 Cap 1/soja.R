# Criando os vetores com os dados coletados para a soja
sementes_hectare <- c(500000, 520000, 480000, 510000, 530000, 495000, 505000, 525000, 490000, 515000)  # Sementes por hectare
espacamento_sementes <- c(0.20, 0.22, 0.19, 0.21, 0.23, 0.20, 0.21, 0.22, 0.19, 0.21)  # Espaçamento entre sementes em metros

# Cálculo da média e do desvio padrão para a quantidade de sementes por hectare
media_sementes <- mean(sementes_hectare)
desvio_padrao_sementes <- sd(sementes_hectare)

# Cálculo da média e do desvio padrão para o espaçamento entre sementes
media_espacamento <- mean(espacamento_sementes)
desvio_padrao_espacamento <- sd(espacamento_sementes)

# Exibir os resultados no console
cat("Média de sementes por hectare:", round(media_sementes, 2), "sementes/hectare\n")
cat("Desvio padrão das sementes por hectare:", round(desvio_padrao_sementes, 2), "sementes/hectare\n")
cat("Média do espaçamento entre sementes:", round(media_espacamento, 2), "m\n")
cat("Desvio padrão do espaçamento entre sementes:", round(desvio_padrao_espacamento, 3), "m\n")


