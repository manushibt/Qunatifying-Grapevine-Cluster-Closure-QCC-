library(devtools)
library(drc)
library(aomisc)
library(stats)

#Read csv filed
dfc = read.csv("result.csv")

# Fit asymtotic regression
modelc <- drm(dfc$Clust_Clo ~ dfc$Timestep, fct = DRC.asymReg())

#Print summary of the model
summary(modelc)

#Function to calculate x value
calcluate_x <- function(x1,model,asy){
  X=c(x1)
  Predict <- function(x) predict(model, data.frame(X = x))
  x.at.ymax <- optimize(Predict, range(X), maximum = TRUE)$maximum
  y <- asy
  opt.ed <- uniroot(function(x) Predict(x) - y, c(X[1], x.at.ymax))
  edv <- opt.ed$root
  return(edv)
}

#Enter the asymptotic coef value into the below equation
calcluate_x(dfc$Timestep,modelrc,91)

#Plot the data with reg model
plot(modelr, log="", xlab = "no of weeks", ylab ="%cluster closure",
      ylim=c(0,100),xlim = c(0,7),pch = 1, cex.axis=1.2)
par(new=TRUE)
plot(dfc$Timestep, dfc$Clust_Clo, pch=19,ylim=c(0,100),xlim = c(0,7),xlab = "", ylab ="",yaxt="n")
par(new=TRUE)
abline(v=calcluate_x(dfc$Timestep,modelrc,91), col="red",lwd =1.5)
