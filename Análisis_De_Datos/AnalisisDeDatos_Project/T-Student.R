Zac <- c(8.5, 7.8, 8.2, 9.0, 7.6, 8.9, 7.9, 8.1, 8.3, 7.4, 8.7, 8.0, 8.6)
Dgo <- c(6.5, 7.2, 7.0, 6.8, 6.3, 7.1, 6.9, 6.4, 7.3, 6.7, 6.8, 6.6)

# Promedios
mean(Zac)
mean(Dgo)

# Desviaciones estandr
sd(Zac)
sd(Dgo)

#t.test()
#x = Grupo A
#y = Grupo B
#alternative = c("two.sided", "less", "greater")
# Tipo de prueba
# two.sided = 2 colas
# lees = 1 cola a la izq (A < B)
# greater = 1 cola a la Der (A > B)
# Paried:
# TRUE = Muestras Pareadas
# FALSE = Muestras Indepandintes
# var.equals = False
# La var es igual entre los grupos ? si/no
# Tipicamente var es TRUE
# conf.level = 0.95 Inverso de alpha

t.test(x = Zac, y = Dgo, alternative = "greater", paired = FALSE, var.equal = TRUE)
