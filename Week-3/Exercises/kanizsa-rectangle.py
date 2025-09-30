import expyriment 
from expyriment import design, control, stimuli
from expyriment.misc.constants import C_GREY

exp = expyriment.design.Experiment(background_colour=C_GREY)

def kanizsaRectngle(rectangeAspectRatio = 1, rectangleScalingFactor = 1, circleScalingFactor = 1):
    exp = design.Experiment(name = "Circle", background_colour=C_GREY)

    control.set_develop_mode()
    control.initialize(exp)

    w = exp.screen.size[0]
    h = exp.screen.size[1]
    radius = int(w * 0.05 * circleScalingFactor)
    squareWidth = int(w * 0.25 * rectangleScalingFactor)
    squareLength = squareWidth * rectangeAspectRatio

    circle1 = stimuli.Circle(radius = radius, colour = "black", position=(squareWidth//2,squareLength//2))
    circle2 = stimuli.Circle(radius = radius, colour = "black", position=(squareWidth//2 * -1,squareLength//2)) 
    circle3 = stimuli.Circle(radius = radius, colour = "white", position=(squareWidth//2,squareLength//2 * -1))
    circle4 = stimuli.Circle(radius = radius, colour = "white", position=(squareWidth//2 * -1,squareLength//2 * -1))
    square = stimuli.Rectangle(size = (squareWidth,squareLength), colour=C_GREY)

    expyriment.control.start()
    circle1.present(clear = True, update = False)
    circle2.present(clear = False, update = False)
    circle3.present(clear = False, update = False)
    circle4.present(clear = False, update = False)
    square.present(clear = False, update = True)
    
    exp.keyboard.wait()
    expyriment.control.end()

kanizsaRectngle(rectangleScalingFactor=0.5, rectangeAspectRatio= 0.5, circleScalingFactor= 0.5)