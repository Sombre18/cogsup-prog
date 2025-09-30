import expyriment 
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

exp = expyriment.design.Experiment(background_colour=C_GREY)
control.set_develop_mode()
control.initialize(exp)

w = exp.screen.size[0]
h = exp.screen.size[1]


radius = int(w * 0.05)

squareWidth = int(w * 0.25)

circle1 = stimuli.Circle(radius = radius, colour = "black", position=(squareWidth//2,squareWidth//2))
circle2 = stimuli.Circle(radius = radius, colour = "black", position=(squareWidth//2 * -1,squareWidth//2)) 
circle3 = stimuli.Circle(radius = radius, colour = "white", position=(squareWidth//2,squareWidth//2 * -1))
circle4 = stimuli.Circle(radius = radius, colour = "white", position=(squareWidth//2 * -1,squareWidth//2 * -1))

square = stimuli.Rectangle(size = (squareWidth,squareWidth), colour=C_GREY)

expyriment.control.start()

circle1.present(clear = True, update = False)
circle2.present(clear = False, update = False)
circle3.present(clear = False, update = False)
circle4.present(clear = False, update = False)
square.present(clear = False, update = True)

exp.keyboard.wait()

expyriment.control.end()