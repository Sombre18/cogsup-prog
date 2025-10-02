from expyriment import design, control, stimuli

exp = design.Experiment(name="Square")

control.set_develop_mode()
control.initialize(exp)

def draw(stims):
    stims[0].present(clear=True, update=False)
    for stim in stims[1:-1]:
        stim.present(clear=False, update=False)
    stims[-1].present(clear=False, update=True)


control.start(subject_id=1)


square = stimuli.Rectangle(size=(100, 100), line_width=5)
fixation = stimuli.FixCross()


draw([square, fixation])

exp.keyboard.wait()

control.end()

