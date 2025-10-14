from expyriment import design, control, stimuli
from expyriment.misc.constants import C_WHITE, C_BLACK, K_SPACE, K_1, K_2, K_DOWN, K_UP, K_LEFT, K_RIGHT

""" Global settings """
exp = design.Experiment(name="Blindspot", background_colour=C_WHITE, foreground_colour=C_BLACK)
exp.add_data_variable_names(["key", "radius", "position"])
control.set_develop_mode()
control.initialize(exp)

keys = [K_1, K_2, K_UP, K_DOWN, K_RIGHT, K_LEFT, K_SPACE]

""" Stimuli """
def make_circle(r, pos=(0,0)):
    c = stimuli.Circle(radius=r, position=pos, anti_aliasing=10)
    c.preload()
    return c

""" Experiment """
def run_trial():
    fixation = stimuli.FixCross(size=(150, 150), line_width=10, position=[300, 0])
    fixation.preload()
    radius = 75
    position= [0,0]

    circle = make_circle(radius, position)
    
    while True:
        fixation.present(clear=True, update=False)
        circle.present(clear=False, update=True)
        
        key, _ = exp.keyboard.wait(keys=keys)
        if key == K_SPACE:
            break
        if key == K_1:
            radius = max(1, radius - 5)
            circle = make_circle(radius, position)
        if key == K_2:
            radius = max(1, radius + 5)
            circle = make_circle(radius, position)
        if key == K_DOWN:
            position = (0, -10)
            circle = make_circle(radius, position)
        if key == K_UP:
            position = (0, +10)
            circle = make_circle(radius, position)
        if key == K_LEFT:
            position = (-10, 0)
            circle = make_circle(radius, position)
        if key == K_RIGHT:
            position = (+10, 0)
            circle = make_circle(radius, position)
    exp.data.add([key, radius, position])
        



control.start(subject_id=1)

run_trial()
    
control.end()