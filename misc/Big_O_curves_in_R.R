x = seq(1, 10, 0.01)
plot(x, rep(0, length(x)), type="l", ylim=c(1, 100), lwd=2)
lines(x, log(x), lwd = 2, col=3)
text(x=9, y=10, labels = "O(log n)", col=3)

lines(x, x * log(x), lwd = 2, col=3)
text(x=8, y=25, labels = "O(n log n)", col=3)

lines(x, x ** 2, lwd = 2, col=4)
text(x=9.5, y=75, labels = "O(n^2)", col=4)

lines(x, 2 ** x, lwd = 2, col=10)
text(x=7.25, y=90, labels = "O(2^n)", col=10)

lines(x, factorial(x), lwd = 2, col=6)
text(x=4, y=90, labels = "O(n!)", col=6)

