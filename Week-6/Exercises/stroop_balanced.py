from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_f, K_g, K_h, K_j
import random
import itertools 

""" Constants """

COLORS = ["red", "blue", "green", "orange"]
COLOR_KEYS = {"red": K_f, "blue": K_g, "green": K_h, "orange": K_j}
KEY_NAMES = {"red": "F", "blue": "G", "green": "H", "orange": "J"}


N_BLOCKS = 8
N_TRIALS_IN_BLOCK = 16

INSTR_START = """
In this task, you have to indicate the colour of each word.
Press:
  F = RED
  G = BLUE
  H = GREEN
  J = ORANGE\n
Press SPACE to continue.
"""
INSTR_MID = """End of block\nTake a break then press SPACE to move on to the next one."""
INSTR_END = """Well done!\nPress SPACE to quit the experiment."""

FEEDBACK_CORRECT = """Correct!"""
FEEDBACK_INCORRECT = """Incorrect!"""

""" Helper functions """
def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(*stims):
    t0 = exp.clock.time
    exp.screen.clear()
    for stim in stims:
        stim.present(clear=False, update=False)
    exp.screen.update()
    t1 = exp.clock.time
    return t1 - t0

def present_for(*stims, t=1000):
    dt = timed_draw(*stims)
    exp.clock.wait(t - dt)

def present_instructions(text):
    instructions = stimuli.TextScreen(text=text, text_justification=0, heading="Instructions")
    instructions.present()
    exp.keyboard.wait()

""" Global settings """
exp = design.Experiment(name="Stroop", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(['block_cnt', 'trial_cnt', 'trial_type', 'word', 'color', 'RT', 'correct'])

control.set_develop_mode()
control.initialize(exp)

""" Stimuli """
fixation = stimuli.FixCross()
fixation.preload()

stims = stims = {w: {c: stimuli.TextLine(w, text_colour=c) for c in COLORS} for w in COLORS}
load([stims[w][c] for w in COLORS for c in COLORS])

feedback_correct = stimuli.TextLine(FEEDBACK_CORRECT)
feedback_incorrect = stimuli.TextLine(FEEDBACK_INCORRECT)
load([feedback_correct, feedback_incorrect])

all_combinations = list(itertools.product(COLORS, COLORS)) 
blocks = []
for _ in range(N_BLOCKS):
    block_trials = all_combinations.copy()
    random.shuffle(block_trials)
    blocks.append(block_trials)


""" Experiment """
def run_trial(block_id, trial_id, word, color):
    stim = stims[word][color]
    present_for(fixation, t=500)
    stim.present()
    key, rt = exp.keyboard.wait(COLOR_KEYS.values())
    correct = key == COLOR_KEYS[color]
    exp.data.add([block_id, trial_id, word, color, rt, correct])
    feedback = feedback_correct if correct else feedback_incorrect
    present_for(feedback, t=1000)

control.start(subject_id=1)

present_instructions(INSTR_START)
trial_index = 0
for block_id, block_trials in enumerate(blocks, start=1):
    for trial_id, (word, color) in enumerate(block_trials, start=1):
        run_trial(block_id, trial_id, word, color)
    if block_id != N_BLOCKS:
        present_instructions(INSTR_MID)
present_instructions(INSTR_END)

control.end()