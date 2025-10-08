from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE
import math


FPS = 60 # frames per second
MSPF = 1000 / FPS # milliseconds per frame (more robust than using 16.67)
def to_frames(t):
    return math.ceil(t / MSPF) # Make sure you use consistent rounding
def to_time(num_frames):
    return num_frames * MSPF

def load(stims):
    for stim in stims:
        stim.preload()

def timed_draw(exp, stims):
    if not stims:
        return 0
    t0 = exp.clock.time
    for i, stim in enumerate(stims):
        stim.present(clear=(i == 0), update=(i == len(stims) - 1))
    t1 = exp.clock.time
    return t1 - t0


def present_for(exp, stims, t):
    dt = timed_draw(exp, stims)
    exp.clock.wait(t - dt)
    stims[0].present(clear=True, update=False)
    for stim in stims[1:-1]:
        stim.present(clear=False, update=False)
    stims[-1].present(clear=False, update=True)

