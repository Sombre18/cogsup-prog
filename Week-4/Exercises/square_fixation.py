from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)


def draw(stims):
    fixation = stimuli.FixCross()
    square = stimuli.Rectangle(size=(100, 100), line_width=5)
    fixation.present()
    square.present()
    if not stims:
        raise ValueError("Stimuli list must be nonempty.")
# Clear the back buffer and draw the first stimulus
    stims[0].present(clear=True, update=False)
# Continue drawing the middle stimuli
    for stim in stims[:-1]:
        stim.present(clear=False, update=False)
# Add the last stimulus and swap the buffers
        stims[-1].present(clear=False, update=True)



control.start(subject_id=1)


t0 = exp.clock.time
draw()
dt = exp.clock.time - t0
exp.clock.wait(1000 - dt)


exp.keyboard.wait()

control.end()

