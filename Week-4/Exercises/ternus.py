from expyriment import design, control, stimuli
from expyriment.misc.constants import K_SPACE
from utils import *


colors = {

1:"yellow",

2:"red",

3:"green",

4:"yellow"

}

def run_trial(color_tags, ISI):
    c = [make_circle(position= 1, color_tags=color_tags), make_circle(position=2, color_tags=color_tags), make_circle(position=3, color_tags=color_tags), make_circle(position=4, color_tags=color_tags)]
    c1 = c[:3]
    c2 = c[1:]
    load(c1)
    load(c2)
    while True:
        if exp.keyboard.check(K_SPACE): # inside the loop
            break
        present_for(exp, c1, t=500)
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(ISI)
        present_for(exp, c2, t=500)
        exp.screen.clear()
        exp.screen.update()
        exp.clock.wait(ISI)
      

def make_circle(position, color_tags):
    step = 50 * 3 
    pos = ((position -2.5) * step, 0)
    circle = stimuli.Circle(radius=50, colour = "white", position=pos, anti_aliasing=10)
    if color_tags: 
        ct = stimuli.Circle(radius=50/3, position=(0, 0), colour=colors[position], anti_aliasing=10)
        ct.plot(circle)
    return circle
   

#def add_tags()

exp = design.Experiment(name="Ternus")

control.set_develop_mode()
control.initialize(exp)

control.start(subject_id=1)

run_trial(True, ISI=150)

exp.keyboard.wait()

control.end()
