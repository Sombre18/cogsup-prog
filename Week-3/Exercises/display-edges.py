import expyriment 
from expyriment import design, control, stimuli

exp = expyriment.design.Experiment()
control.set_develop_mode()
control.initialize(exp)

w, h = exp.screen.size
stim_len = w//10
stim_size = (stim_len, stim_len)

edges = []
for x in (-w, w):
    for y in (-h, h):
        edges.append((x//2, y//2))

rectangle1 = stimuli.Rectangle(size=(int(w**0.05),int(h**0.05)), colour=[250, 0, 0], line_width=1, position=(-w//2+1,h//2-1))


#position=((-(width // 2), -(height // 2))))
#(width**0.05),(height**0.05)

expyriment.control.start()

rectangle1.present(clear=True, update=True)
#rectangle2.present(clear=False, update=True)
#rectangle3.present(clear=True, update=True)
#rectangle4.present(clear=True, update=True)

expyriment.control.end()