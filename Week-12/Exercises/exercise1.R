a = 3
b <- 5
print(a * b)


truth_value = FALSE
print(!truth_value)
print(truth_value | TRUE)
print(truth_value & TRUE)


x = 2.0
y = 3
z = 3/4
print(x + y + z)


txt = "This is CORE-1."
print(length(txt))
print(nchar(txt))

a = factor("Condition 1")
b = factor("Condition 2")
print(a)
print(b)
print(as.numeric(a))
print(as.numeric(b))

i = 25
if (i > 3){
  print('yes')
} else {
  print('no')
}


square <- function(x){
  squared <- x * x
  return (squared)
}
square(10)


sequence = c(1, 2, 3, 4, 5)

#for (variable in sequence){
  #print(variable)
#}


v1 <- c(10, 0, 0, 7, 6, 6, 2, 5) # Concatenate the numbers and store them in a vector
print(v1)

v2 <- 2:10 # Integer sequence
print(v2)

v3 <- seq(2, 3, by=0.1) # More fine-grained sequence
print(v3)

rep(v1, times=3) # Repeat v1 3 times

rep(v1, each=3) # Repeat each element of v1 3 times

v4 <- rnorm(n=10, mean=0, sd=1) # Sample 10 numbers from a normal distribution with mean 0 and sd 1
print(v4)

v6 <- (1:10)
print(v6)

v6 <- 1:10
print(v6)
v7 <- exp(v6)
v8 <- sapply(v6, exp)

hist(v1)

plot(v6, v7, type="p")
plot(v6, v7, type="l")

plot(v6, v7, type="p")
lines(v6, v7) # Use 'lines' to force R to draw on the already-existing plot

v8 <- seq(1, 10, by=0.01)
plot(v8, exp(v8), type='l')
