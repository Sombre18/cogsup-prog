import expyriment 
from expyriment import design, control, stimuli

exp = expyriment.design.Experiment()
control.set_develop_mode()
control.initialize(exp)

w = exp.screen.size[0]
h = exp.screen.size[1]


square1 = stimuli.Rectangle((w // 20, w // 20), line_width= 1, position = (w//2 - w // 40, h //2 - w // 40), colour='red')
square2 = stimuli.Rectangle((w // 20, w // 20), line_width= 1, position = (((w//2) * -1) + w // 40, h //2 - w // 40), colour='red')
square3 = stimuli.Rectangle((w // 20, w // 20), line_width= 1, position = (w//2 - w // 40, ((h //2) * -1) + w // 40), colour='red')
square4 = stimuli.Rectangle((w // 20, w // 20), line_width= 1, position = (((w//2) * -1) + w // 40, ((h //2) * -1) + w // 40), colour='red')



expyriment.control.start()

square1.present(clear=True, update=False)
square2.present(clear=False, update= False)
square3.present(clear=False, update=False)
square4.present(clear=False, update= True)

exp.keyboard.wait()

expyriment.control.end()