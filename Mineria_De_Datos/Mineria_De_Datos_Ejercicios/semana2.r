library(DescTools)
ca = c(8,9,10,9,8,10,15)
mean(ca)
median(ca)
Mode(ca)
boxplot(ca)
#################
#
# Análisis de AO
#
#################
AO = c(41.75,	114.84,	107.58,	29.93,	73.46,	101.6,	49.47,	40.78,	57.5,	53.24,	57.43,	58.43,	50.56,	47.91,	24.79,	93.85,	54.75,	43.81,	54.17)
mean(AO) #60.83u <- Solicitar análisis adicionales 
median(AO) #54.17u <- 2do descriptor de mi población que corrobora un 2do análisis
Mode(AO) # NA <- Valor continuo
boxplot(AO)# Aparantemente 3 out, mayores a 100
summary(AO)
quantile(AO)
boxplot(AO, horizontal = TRUE, col = "green", main = "Arsénico en Orina", xlab="Microgramos/L")
###############
#
# Arsenico en el Agua
#
##########3
AA = c(36.78,	48.5,	39.42,	24.45,	32.15,	40.46,	43.68,	43.01,	39.2,	39.79,	42.3,	46.63,	44.39,	35.58,	39.2,	38.28,	43.34,	36.69,	41.78)
mean(AA) #39.77 <- Casi 4 veces el límite internacional
median(AA) #39.79 <- No existen datos atípicos
boxplot(AA)
summary(AA)
boxplot(AO,AA, horizontal = TRUE, col = "red")
############
#
# Dispersión
#
###########
sd(AO) #25.7 <-+- prom 35 - 85   <-68%
sd(AA) #40 <-+-1 35 - 45 <- 68% +-2 30 - 50 <-95% +-3 25 - 55 99.7% 

########
# sd pequeña → los datos están concentrados cerca de la media.
# sd grande → los datos están muy dispersos.
#######

# Sesgo
library(e1071)
skewness(AO) # sesgo postitivo 
boxplot(AO, horizontal = TRUE)

skewness(AA)
boxplot(AA, horizontal = TRUE)

# Histogramas 
hist(AO, breaks = 15)
hist(AA, breaks = 15)

# Cuarto momento (Curtosis)
kurtosis(AO) # -> Negativa -0.5527793
kurtosis(AA) # -> Positiva 1.193106


# Funcion 
plotn <- function(x,main="Histograma de frecuencias \ny distribución normal",
                  xlab="X",ylab="Densidad") {
  min <- min(x)
  max <- max(x)
  media <- mean(x)
  dt <- sd(x)
  hist(x,freq=F,main=main,xlab=xlab,ylab=ylab)
  curve(dnorm(x,media,dt), min, max,add = T,col="red") # Genera una curva de distribucion normal
}

plotn(AO)
plotn(AA)


#######################
#
# Correlacion 
#
######################
cor.test(AO,AA) # 0.3119695 
cor.test(AA, AO)  

