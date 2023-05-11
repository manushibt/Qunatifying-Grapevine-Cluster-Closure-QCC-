library(devtools)
library(drc)
library(aomisc)
library(stats)

df = read.csv("F:/Cornell/Cluster_closure/2023/Project_Data/results/PGRIS_PSP_Date.csv")
dfc = read.csv("F:/Cornell/Cluster_closure/2023/Project_Data/results/CF_PSP_Date.csv")
dfr = df[df$Cultivar=="Riesling",]
dfpg = df[df$Cultivar=="Pinot gris",]

quantile(dfr$Clust_Clo)  

# drm fit Riesling
modelr <- drm(dfr$Clust_Clo ~ dfr$Timestep, fct = DRC.asymReg())
modelpg <- drm(dfpg$Clust_Clo ~ dfpg$Timestep, fct = DRC.asymReg())
modelc <- drm(dfc$Clust_Clo ~ dfc$Timestep, fct = DRC.asymReg())

summary(modelr)
summary(modelpg)
summary(modelc)

X=dfr$Timestep
Predict <- function(x) predict(modelr, data.frame(X = x))
x.at.ymax <- optimize(Predict, range(X), maximum = TRUE)$maximum
y50 <- 91
opt.ed50 <- uniroot(function(x) Predict(x) - y50, c(X[1], x.at.ymax))
ed50 <- opt.ed50$root

X=dfpg$Timestep
Predict <- function(x) predict(modelpg, data.frame(X = x))
x.at.ymax <- optimize(Predict, range(X), maximum = TRUE)$maximum
y50 <- 94
opt.ed50 <- uniroot(function(x) Predict(x) - y50, c(X[1], x.at.ymax))
ed50 <- opt.ed50$root

X=dfc$Timestep
Predict <- function(x) predict(modelc, data.frame(X = x))
x.at.ymax <- optimize(Predict, range(X), maximum = TRUE)$maximum
y50 <- 81
opt.ed50 <- uniroot(function(x) Predict(x) - y50, c(X[1], x.at.ymax))
ed50 <- opt.ed50$root

calcluate_x <- function(x1,model,asy){
  X=c(x1)
  Predict <- function(x) predict(model, data.frame(X = x))
  x.at.ymax <- optimize(Predict, range(X), maximum = TRUE)$maximum
  y50 <- asy
  opt.ed50 <- uniroot(function(x) Predict(x) - y50, c(X[1], x.at.ymax))
  ed50 <- opt.ed50$root
  return(ed50)
}

calcluate_x(dfr$Timestep,modelr,91)
calcluate_x(dfpg$Timestep,modelpg,94)
calcluate_x(dfc$Timestep,modelrc,81)

plot(modelr, log="", xlab = "no of weeks", ylab ="%cluster closure",
      ylim=c(0,100),xlim = c(0,7),pch = 1)
par(new=TRUE)
plot(dfr$Timestep, dfr$Clust_Clo, pch=19,ylim=c(0,100),xlim = c(0,7),xlab = "", ylab ="",yaxt="n")
par(new=TRUE)
abline(v=calcluate_x(dfr$Timestep,modelr,91), col="red")

plot(modelpg, log="", xlab = "no of weeks", ylab ="%cluster closure",
     ylim=c(0,100),xlim = c(0,7),pch = 1)
par(new=TRUE)
plot(dfpg$Timestep, dfpg$Clust_Clo, pch=19,ylim=c(0,100),xlim = c(0,7),xlab = "", ylab ="",yaxt="n")
par(new=TRUE)
abline(v=calcluate_x(dfpg$Timestep,modelpg,94), col="red")

plot(modelc, log="", xlab = "no of weeks", ylab ="%cluster closure",
     ylim=c(0,100),xlim = c(0,7),pch = 1)
par(new=TRUE)
plot(dfc$Timestep, dfc$Clust_Clo, pch=19,ylim=c(0,100),xlim = c(0,7),xlab = "", ylab ="",yaxt="n")
par(new=TRUE)
#abline(v=ED(modelc,modelc$coefficients[2])[1], col="red")


plot(modelpg, log="",xlab = "", ylab ="",
     ylim=c(0,100),xlim = c(0,7),pch = 0)
par(new=TRUE)
plot(modelc, log="",xlab = "no of weeks", ylab ="%cluster closure",
     ylim=c(0,100),xlim = c(0,7),pch = 2)
legend("bottomright", inset=.02, title="Cultivar", pch = c(1,0, 2),
       c("Riesling","Pinot gris","Cabernet Franc"),lty = c(1, 1,1), cex=0.8)


