library(tidyverse)
library(conflicted)
library(dplyr)

data <- read_csv("data/148338_220209_095045_M057814.csv", skip=2)

education_level <- data %>% pull(response) %>% first()  

data <- data %>%
  # Keep only useful columns
  select(c(rowNo, type, stim1, stim2, stimPos, trialType, response, RT)) %>%
  
  # Keep only useful rows
  filter(type != "form") %>%
  
  # Add demographic and trial-number info, turn trial type to factor
  mutate(
    education_level = education_level, # Add info
    trial_number = row_number(),
    trialType = factor(trialType, levels = c("incongruent", "congruent"))
  ) %>%
  
  # Rename trialType to trial_type
  rename(trial_type = trialType)

head(data)

#

#exercise 11
tidy_data <- data %>%
  select(-rowNo, -type) %>%
  rename(
    stim_left  = stim1,
    stim_right = stim2,
    rt = RT
  ) %>%
  mutate(
    subject_id = 1,
    correct_side = ifelse(str_detect(stim_left, "Small"), "left", "right"),
    correct_key  = ifelse(correct_side == "left", "f", "j"),
    correct      = ifelse(response == correct_key, 1, 0),
    trial_block  = ifelse(trial_number <= 120, 1, 2),
    trial_number = ifelse(trial_number <= 120, trial_number, trial_number - 120)
  ) %>%
  select(
    subject_id, education_level,
    trial_block, trial_number,
    trial_type, stim_left, stim_right, stimPos,
    correct_side, correct_key,
    response, correct, rt
  )


#summary stats
tidy_data %>%
  summarize(rt = mean(rt), accuracy = mean(correct), error = mean(1 - correct))

tidy_data %>%
  mutate(avg_error = mean(1 - correct))

#exercise 12
tidy_data %>%
  summarize(
    rt = mean(rt),
    error = mean(1 - correct),
    .by = trial_type
  )

glimpse(data)

#exercise 13
tidy_data %>%
  summarize(
    rt = mean(rt),
    .by = correct_side
  )

#exercise 14
tidy_data %>%
  summarize(
    rt = mean(rt),
    .by = c(trial_type, correct_side)
  )

# Fetch all the files in the 'data' folder that end in csv
raw_data <- list.files(path = 'data', pattern = ".csv$", full.names = TRUE) %>% 
  
  # Map the read_csv function to all of them, skipping the first 2 rows and creating a new id column called 'id' so that each file gets its own id
  # col_types = cols() just makes explicit that you want tidyverse to do its best to guess the type of each column (string, numeric, etc.)
  map_dfr(read_csv, col_types = cols(), skip = 2, .id = 'id') 

#exercise 15
full_data <- raw_data %>%
  mutate(education_level = first(response), .by = id) %>%
  filter(type != "form") %>%
  select(-rowNo, -type) %>%
  rename(
    stim_left  = stim1,
    stim_right = stim2,
    rt = RT,
    trial_type = trialType
  ) %>%
  
  mutate(
    correct_side = ifelse(str_detect(stim_left, "Small"), "left", "right"),
    correct_key  = ifelse(correct_side == "left", "f", "j"),
    correct      = ifelse(response == correct_key, 1, 0),
    trial_number = row_number(),
    trial_block  = ifelse(trial_number <= 120, 1, 2),
    trial_number = ifelse(trial_number <= 120, trial_number, trial_number - 120)
  ) %>%
  
  ungroup

#exercise 16
excluded_trials <- full_data %>%
  filter(rt < 200 | rt > 1500)

nrow(excluded_trials)

full_data <- full_data %>%
  filter(rt >= 200 & rt <= 1500)

#exercise 17
excluded_subjects <- full_data %>%
  summarize(accuracy = mean(correct), .by = id) %>%
  filter(accuracy < 0.93)

nrow(excluded_subjects)

full_data <- full_data %>%
  summarize(accuracy = mean(correct), .by = id) %>%
  filter(accuracy >= 0.93) %>%
  select(id) %>%
  inner_join(full_data, by = "id")

#exercise 18
full_data %>%
  summarize(
    rt = mean(rt),
    accuracy = mean(correct),
    .by = trial_type
  )

#exercise 19
stroop_data <- full_data %>%
  summarize(
    rt = mean(rt),
    error = mean(1 - correct),
    .by = c(id, trial_type)
  ) %>%
  pivot_wider(
    names_from = trial_type,
    values_from = c(rt, error)
  ) %>%
  mutate(
    stroop_rt    = rt_incongruent - rt_congruent,
    stroop_error = error_incongruent - error_congruent
  )

stroop_data %>% pull(stroop_rt) %>% hist()

#exercise 20
stroop_data %>%
  select(id, stroop_rt, stroop_error) %>%
  pivot_longer(
    cols = c(stroop_rt, stroop_error),
    names_to = "measure",
    values_to = "value"
  )

#data plotting: one possible way to do it
average_data <- full_data %>% summarize(rt = mean(rt), .by = c(id, trial_type)) 

ggplot(average_data, aes(x = trial_type, y = rt, fill = trial_type)) +
  geom_boxplot(width = 0.5, alpha = 0.45) +
  geom_point(size = 2) +
  geom_line(aes(group = id), color = 'gray') +         
  stat_summary(fun.data = mean_se, linewidth = 2, shape = 21, size = 1.5) +
  labs(title = "Average reaction times by trial type (ms)", x = "Trial type", y = "") +
  theme_minimal() + 
  theme(
    legend.position = "none", 
    plot.title = element_text(face = "bold", size = 20),
    axis.title = element_text(size = 18),
    axis.text = element_text(size = 16))
