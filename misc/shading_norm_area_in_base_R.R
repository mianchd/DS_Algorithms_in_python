shade.norm <- function(x1, x2, mean=0, sd=1) {
     cord.x <- c(x1, seq(x1, x2, 0.01), x2)
     cord.y <- c(-0.012, dnorm(seq(x1, x2, 0.01), mean = mean, sd = sd), -0.012)
     polygon(cord.x, cord.y, col="lightblue")
     }

tempx = seq(-3, 3, 0.01)
plot(tempx, dnorm(tempx), type="l", lwd=3, col="brown")
shade.norm(-2, 0)
