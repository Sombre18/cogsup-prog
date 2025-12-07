#Exercise 2.1
roll_die <- function(){
  die <- 1:6
  return(sample(die, size=1))
  }

roll_die()


#Exercise 2.2 & 2.3
die_roll_outcomes <- function(){
  a <- replicate(100, roll_die())
  return(a)
  }

die_roll_outcomes()
hist(x = die_roll_outcomes())

sum(die_roll_outcomes())


#Exercise 2.4
die_sum <- function(){
  a <- replicate(1000, sum(replicate(10, roll_die())))
  return(a)
}

hist(x = die_sum(), breaks = 30)


#Exercise 2.5
avg_die_roll_outcomes <- function(){
  replicate(1000, mean(replicate(10, roll_die())))
}

hist(avg_die_roll_outcomes(), breaks = 30)

var(1:6)
x <- 1:6
p <- rep(1/6, 6)
av <- sum(x * p)              
variance <- sum((x - av)^2 * p)
variance


#Exercise 2.6
pop_var <- function(x, p = NULL) {
  if (is.null(p)) {
    p <- rep(1/length(x), length(x))  
  }
  mu <- sum(x * p)
  sum((x - mu)^2 * p)
}


pop_sd <- function(x, p = NULL) {
  sqrt(pop_var(x, p))
}


die_var <- pop_var(1:6)
die_sd <- pop_sd(1:6)

die_var  
die_sd    


#Exercise 2.7
sd_mean_die_rolls <- function(n_rolls = 100, n_sim = 1000) {
  averages <- replicate(n_sim, mean(sample(1:6, size = n_rolls, replace = TRUE)))
  sd(averages)
}

sd_mean_die_rolls()


#Exercise 2.8
n_rolls_vec <- seq(1, 100, by = 2)
sd_results <- sapply(n_rolls_vec, sd_mean_die_rolls)
sd_results


#Exercise 2.9
plot(n_rolls_vec, sd_results)


#Exercise 2.10
sd_die <- pop_sd(1:6)        
new_curve <- sd_die / sqrt(n_rolls_vec)

lines(n_rolls_vec, new_curve)

#Exercise 2.11
#Most people are of average height so there is a normal distribution. The more extreme the height is, the less common it is.