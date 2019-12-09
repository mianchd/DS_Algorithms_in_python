shade.norm <- function(x1, x2){
    cord.x <- c(x1, seq(x1, x2, 0.01), x2)
    cord.y <- c(-0.012, dnorm(seq(x1, x2, 0.01)), -0.012)
    polygon(cord.x, cord.y, col="lightblue") 
  }

