roll_die <- function(){
  die <- 1:6
  return(sample(die, size=1))
  }

roll_die()


die_roll_outcomes <- function(){
  a <- replicate(100, roll_die())
  return(a)
  }

die_roll_outcomes()
hist(x = die_roll_outcomes())

sum(die_roll_outcomes())


new_die_roll_outcomes <- function(){
  a <- replicate(1000, roll_die())
  return(a)
}

die_sum <- sum(new_die_roll_outcomes())
hist(x = new_die_roll_outcomes())

