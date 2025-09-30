from expyriment import design, control, stimuli

from expyriment.misc.constants import C_GREY

def hermannGrid(sizeSquares = 10, colorSquares = "black", spaceBetween = 2, backgroundColor = C_GREY, rows = 10, columns = 10):
    exp = design.Experiment(name = "Circle", background_colour=backgroundColor)

    control.set_develop_mode()

    control.initialize(exp)

    
    square = stimuli.Rectangle(size = (sizeSquares,sizeSquares), colour=colorSquares,position=((sizeSquares + spaceBetween) * columns / 2 * -1, (sizeSquares + spaceBetween) * rows / 2 * -1))
    
    square.present(update=False,clear=True)

    for r in range(rows):
        for c in range(columns):
            square.present(update=False, clear=False)
            square.move((spaceBetween + sizeSquares,0))
        square.move(((spaceBetween + sizeSquares) * columns * -1,0))
        square.move((0,spaceBetween + sizeSquares))
    square.move((0,(spaceBetween + sizeSquares) * -1))
    square.present(update=True,clear=False)
            
            

    exp.keyboard.wait()
    control.end()

hermannGrid(sizeSquares = 30, colorSquares = "black", spaceBetween = 2, backgroundColor = C_GREY, rows = 10, columns = 20)